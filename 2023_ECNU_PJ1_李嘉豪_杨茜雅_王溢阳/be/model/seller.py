import sqlite3 as sqlite
from be.model import error
from be.model import db_conn
import json


class Seller(db_conn.DBConn):
    def __init__(self):
        db_conn.DBConn.__init__(self)

    def add_book(self, user_id, store_id, book_id, book_info, stock_level):
        try:
            if not self.user_id_exist(user_id):
                return error.error_non_exist_user_id(user_id)
            if not self.store_id_exist(store_id):
                return error.error_non_exist_store_id(store_id)
            if self.book_id_exist(store_id, book_id):
                return error.error_exist_book_id(book_id)
            cur = self.conn["store"]
            cur.insert_one({
                "store_id": store_id,
                "book_id": book_id,
                "price": json.loads(book_info).get("price"),
                "stock_level": stock_level
            })
        except sqlite.Error as e:
            return 528, "{}".format(str(e))
        except BaseException as e:
            return 530, "{}".format(str(e))
        return 200, "ok"

    def add_stock_level(self, user_id: str, store_id: str, book_id: str, add_stock_level: int):
        try:
            if not self.user_id_exist(user_id):
                return error.error_non_exist_user_id(user_id)
            if not self.store_id_exist(store_id):
                return error.error_non_exist_store_id(store_id)
            if not self.book_id_exist(store_id, book_id):
                return error.error_non_exist_book_id(book_id)
            cur = self.conn["store"]
            result = cur.update_one({"store_id": store_id, "book_id": book_id}, {"$inc": {"stock_level": add_stock_level}})
            if result.matched_count == 0:
                return 922, "新增库存中，stock_level更新错误"
        except sqlite.Error as e:
            return 528, "{}".format(str(e))
        except BaseException as e:
            return 530, "{}".format(str(e))
        return 200, "ok"

    def create_store(self, user_id: str, store_id: str):
        try:
            if not self.user_id_exist(user_id):
                return error.error_non_exist_user_id(user_id)
            if self.store_id_exist(store_id):
                return error.error_exist_store_id(store_id)
            cur = self.conn["user_store"]
            cur.insert_one({
                "store_id": store_id,
                "user_id": user_id
            })
        except sqlite.Error as e:
            return 528, "{}".format(str(e))
        except BaseException as e:
            return 530, "{}".format(str(e))
        return 200, "ok"