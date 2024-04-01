import jwt
import time
import logging
import sqlite3 as sqlite
from be.model import error
from be.model import db_conn


def jwt_encode(user_id: str, terminal: str) -> str:
    encoded = jwt.encode(
        {"user_id": user_id, "terminal": terminal, "timestamp": time.time()},
        key=user_id,
        algorithm="HS256",
    )
    return encoded.encode("utf-8").decode("utf-8")



# decode a JWT to a json string like:
#   {
#       "user_id": [user name],
#       "terminal": [terminal code],
#       "timestamp": [ts]} to a JWT
#   }
def jwt_decode(encoded_token, user_id: str) -> str:
    decoded = jwt.decode(encoded_token, key=user_id, algorithms="HS256")
    return decoded


class User(db_conn.DBConn):
    token_lifetime: int = 3600  # 3600 second

    def __init__(self):
        db_conn.DBConn.__init__(self)

    def __check_token(self, user_id, db_token, token) -> bool:
        try:
            if db_token != token:
                return False
            jwt_text = jwt_decode(encoded_token=token, user_id=user_id)
            ts = jwt_text["timestamp"]
            if ts is not None:
                now = time.time()
                if self.token_lifetime > now - ts >= 0:
                    return True
        except jwt.exceptions.InvalidSignatureError as e:
            logging.error(str(e))
            return False

    
    def register(self, user_id, password):
        try:
            terminal = "terminal_{}".format(str(time.time()).replace(".", "_"))
            token = jwt_encode(user_id, terminal)
            cur = self.conn["user"]
            if cur.count_documents({"user_id": user_id}) != 0:
                return 931, "该账号已被注册"
            cur.insert_one({
                "user_id": user_id,
                "password": password,
                "balance": 0,
                "token": token,
                terminal: terminal
            })
        except Exception as e:
            return 901, "{}".format(e)
        return 200, "ok"


    def check_token(self, user_id: str, token: str):
        cur = self.conn["user"]
        result = cur.find({"user_id": user_id})
        if cur.count_documents({"user_id": user_id}) == 0:
            return error.error_authorization_fail()
        for each in result:
            db_token = each["token"]
            break
        if not self.__check_token(user_id, db_token, token):
            return error.error_authorization_fail()
        return 200, "ok"


    def check_password(self, user_id: str, password: str):
        cur = self.conn["user"]
        result = cur.find({"user_id": user_id})
        if cur.count_documents({"user_id": user_id}) == 0:
            return error.error_authorization_fail()
        for each in result:
            this_password = each["password"]
            break
        if password != this_password:
            return error.error_authorization_fail()

        return 200, "ok"


    def login(self, user_id: str, password: str, terminal: str):
        token = ""
        try:
            code, message = self.check_password(user_id, password)
            if code != 200:
                return code, message, ""
            token = jwt_encode(user_id, terminal)
            cur = self.conn["user"]
            result = cur.update_one({"user_id": user_id}, {"$set": {"token": token, "terminal": terminal}})
            if result.matched_count == 0:
                return error.error_authorization_fail() + ("",)
        except BaseException as e:
            return 530, "{}".format(str(e)), ""
        return 200, "ok", token


    def logout(self, user_id: str, token: str) -> bool:
        try:
            code, message = self.check_token(user_id, token)
            if code != 200:
                return code, message

            terminal = "terminal_{}".format(str(time.time()))
            dummy_token = jwt_encode(user_id, terminal)

            cur = self.conn["user"]
            result = cur.update_one({"user_id": user_id}, {"$set": {"token": dummy_token, "terminal": terminal}})
            if result.matched_count == 0:
                return error.error_authorization_fail()
        except BaseException as e:
            return 530, "{}".format(str(e))
        return 200, "ok"


    def unregister(self, user_id: str, password: str):
        try:
            code, message = self.check_password(user_id, password)
            if code != 200:
                return code, message

            cur = self.conn["user"]
            result = cur.delete_one({"user_id": user_id})
            count = result.deleted_count
            if count == 0:
                return error.error_authorization_fail()
        except BaseException as e:
            return 530, "{}".format(str(e))
        return 200, "ok"

    def change_password(
        self, user_id: str, old_password: str, new_password: str
    ) -> bool:
        try:
            code, message = self.check_password(user_id, old_password)
            if code != 200:
                return code, message

            terminal = "terminal_{}".format(str(time.time()).replace(".", "_"))
            token = jwt_encode(user_id, terminal)
            cur = self.conn["user"]
            result = cur.update_one({"user_id": user_id}, {"$set": {"password": new_password, "token": token, "terminal": terminal}})
            if result.matched_count == 0:
                return error.error_authorization_fail()
        except BaseException as e:
            return 530, "{}".format(str(e))
        return 200, "ok"

