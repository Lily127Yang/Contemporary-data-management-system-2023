import sqlite3 as sqlite
import uuid
import json
import logging
from be.model import db_conn
from be.model import error
from datetime import datetime

class Buyer(db_conn.DBConn):
    def __init__(self):
        db_conn.DBConn.__init__(self)

    def new_order(
        self, user_id, store_id, id_and_count):
        order_id = ""
        try:
            if not self.user_id_exist(user_id):
                return error.error_non_exist_user_id(user_id) + (order_id,)
            if not self.store_id_exist(store_id):
                return error.error_non_exist_store_id(store_id) + (order_id,)
            uid = "{}_{}_{}".format(user_id, store_id, str(uuid.uuid1()))
            order_id = uid
            for book_id, count in id_and_count:
                cur = self.conn["store"]
                result = cur.find({"store_id": store_id, "book_id": book_id})
                if cur.count_documents({"store_id": store_id, "book_id": book_id}) == 0:
                    return error.error_non_exist_book_id(book_id) + (order_id,)
                for each in result:
                    stock_level = each["stock_level"]
                    price = each["price"]
                    break
                if stock_level < count:
                    return error.error_stock_level_low(book_id) + (order_id,)
                result = cur.update_one({"store_id": store_id, "book_id": book_id, "stock_level": stock_level}, {"$set": {"stock_level": stock_level - count}})
                if result.matched_count == 0:
                    return error.error_stock_level_low(book_id) + (order_id,)
                cur = self.conn["new_order_detail"]
                cur.insert_one({
                    "order_id": order_id, 
                    "book_id": book_id, 
                    "count": count,
                    "price": price, 
                    "state": 0,
                    "order_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "payment_time": None,
                    "delivery_time": None,
                    "receipt_time": None
                })
                cur = self.conn["new_order"]
                cur.insert_one({
                    "order_id": order_id,
                    "store_id": store_id,
                    "user_id": user_id,
                    "payment_time": None
                })
        except sqlite.Error as e:
            logging.info("528, {}".format(str(e)))
            return 528, "{}".format(str(e)), ""
        except BaseException as e:
            logging.info("530, {}".format(str(e)))
            return 530, "{}".format(str(e)), ""

        return 200, "ok", order_id

    def payment(self, user_id: str, password: str, order_id: str):
        try:
            cur = self.conn["new_order"]
            result = cur.find({"order_id": order_id})
            if cur.count_documents({"order_id": order_id}) == 0:
                return error.error_invalid_order_id(order_id)
            for each in result:
                order_id = each["order_id"]
                buyer_id = each["user_id"]
                store_id = each["store_id"]
                break

            if buyer_id != user_id:
                return error.error_authorization_fail()
            
            # 新功能需要，付款前先验证订单状态
            cur = self.conn["new_order_detail"]
            result = cur.find({"order_id": order_id})
            if cur.count_documents({"order_id": order_id}) == 0:
                return error.error_invalid_order_id(order_id)
            for each in result:
                state_code = each["state"]
                break
            if state_code != 0:
                return 912, "只有未付款的订单才能执行该操作"
            cur = self.conn["user"]
            result = cur.find({"user_id": buyer_id})
            if cur.count_documents({"user_id": buyer_id}) == 0:
                return error.error_non_exist_user_id(buyer_id)
            for each in result:
                balance = each["balance"]
                this_password = each["password"]
                break
            if password != this_password:
                return error.error_authorization_fail()
            cur = self.conn["user_store"]
            result = cur.find({"store_id": store_id})
            if cur.count_documents({"store_id": store_id}) is None:
                return error.error_non_exist_store_id(store_id)
            for each in result:
                seller_id = each["user_id"]
                break
            if not self.user_id_exist(seller_id):
                return error.error_non_exist_user_id(seller_id)
            cur = self.conn["new_order_detail"]
            result = cur.find({"order_id": order_id})
            if cur.count_documents({"order_id": order_id}) == 0:
                return 903, "查询new_order_detail表出错"
            total_price = 0
            for each in result:
                count = each["count"]
                price = each["price"]
                total_price = total_price + price * count
            if balance < total_price:
                return error.error_not_sufficient_funds(order_id)

            cur = self.conn["user"]
            result = cur.update_one({"user_id": buyer_id}, {"$set": {"balance": balance - total_price}})
            if cur.matched_count == 0:
                return error.error_non_exist_user_id(buyer_id)
            result = cur.update_one({"user_id": seller_id}, {"$inc": {"balance": total_price}})
            if result.matched_count == 0:
                return error.error_non_exist_user_id(seller_id)
            # """
            # cur = self.conn["new_order"]
            # result = cur.delete_one({"order_id": order_id})
            # if result.deleted_count == 0:
            #     return error.error_invalid_order_id(order_id)
            # 根据新功能需要，付款后不再删除订单信息
            # """
            #
            # """
            # cur = self.conn["new_order_detail"]
            # result = cur.delete_one({"order_id": order_id})
            # if result.deleted_count == 0:
            #     return error.error_invalid_order_id(order_id)
            # 调整为修改state
            # """
            cur = self.conn["new_order_detail"]
            result = cur.update_one({"order_id": order_id}, {"$set": {"state": 1, "payment_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}})
            if result.matched_count == 0:
                return error.error_invalid_order_id(order_id)
            cur = self.conn["new_order"]
            result = cur.update_one({"order_id": order_id}, {"$set": {"payment_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}})
            if result.matched_count == 0:
                return error.error_invalid_order_id(order_id)
        except sqlite.Error as e:
            return 528, "{}".format(str(e))

        except BaseException as e:
            return 530, "{}".format(str(e))

        return 200, "ok"

    def add_funds(self, user_id, password, add_value):
        try:
            cur = self.conn["user"]
            result = cur.find({"user_id": user_id})
            if cur.count_documents({"user_id": user_id}) == 0:
                return error.error_authorization_fail()
            for each in result:
                saved_password = each["password"]
                balance = each["balance"]
            if saved_password != password:
                return error.error_authorization_fail()

            cur = self.conn["user"]
            result = cur.update_one({"user_id": user_id}, {"$set": {"balance": balance + add_value}})
            if result.matched_count == 0:
                return error.error_non_exist_user_id(user_id)

        except sqlite.Error as e:
            return 528, "{}".format(str(e))
        except BaseException as e:
            return 530, "{}".format(str(e))

        return 200, "ok"