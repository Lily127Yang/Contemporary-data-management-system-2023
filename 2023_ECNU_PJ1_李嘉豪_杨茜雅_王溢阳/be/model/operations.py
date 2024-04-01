from be.model import error
from be.model import db_conn
from datetime import datetime

class Operations(db_conn.DBConn):
    def __init__(self):
        db_conn.DBConn.__init__(self)

    def delivery(self, order_id, store_id, store_owner_id, password):
        cur = self.conn["user"]
        # step1 验证登录信息是否正确
        if cur.count_documents({"user_id": store_owner_id, "password": password}) == 0:
            return error.error_authorization_fail()
        # step2 验证店主关系是否成立
        cur = self.conn["user_store"]
        if cur.count_documents({"user_id": store_owner_id, "store_id": store_id}) == 0:
            return 904, "当前用户不是对应店铺的店主"
        # step3 验证当前店铺是否确实存在这笔订单
        cur = self.conn["new_order"]
        if cur.count_documents({"order_id": order_id, "store_id": store_id}) == 0:
            return 905, "订单信息不匹配"
        # step4 查询当前订单的详情信息
        cur = self.conn["new_order_detail"]
        result = cur.find({"order_id": order_id})
        for each in result:
            state = each["state"]
            break
        if state != 1:
            return 907, "只有处于未发货状态才能进行发货"
        # step 5 发货
        result = cur.update_one({"order_id": order_id}, {"$set": {"state": 2, "delivery_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}})
        return 200, "ok"

    def receipt(self, order_id, user_id, password):
        # step1 验证登录信息是否正确
        cur = self.conn["user"]
        if cur.count_documents({"user_id": user_id, "password": password}) == 0:
            return error.error_authorization_fail()
        # step2 验证这个用户是否确实有这个订单
        cur = self.conn["new_order"]
        if cur.count_documents({"user_id": user_id, "order_id": order_id}) == 0:
            return 905, "订单信息不匹配"
        # step3 收货
        cur = self.conn["new_order_detail"]
        result = cur.find({"order_id": order_id})
        for each in result:
            state = each["state"]
            break
        if state != 2:
            return 909, "只有处于已发货、未收货的状态，才能进行本操作"
        result = cur.update_one({"order_id": order_id}, {"$set": {"state": 3, "receipt_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}})
        return 200, "ok"

    def lookup(self, order_id, user_id, password):
        # step1 验证登录信息是否正确
        cur = self.conn["user"]
        if cur.count_documents({"user_id": user_id, "password": password}) == 0:
            return error.error_authorization_fail()
        # step2 验证这个用户是否确实有这个订单
        # 10月31代码更新，现在卖家也可以查询订单
        cur = self.conn["new_order"]
        if_exists_flag = False
        # 以用户的身份进行查找
        if cur.count_documents({"user_id": user_id, "order_id": order_id}) == 0:
            # 代码运行到此处，证明以用户身份查找失败，接下来以店主身份进行查询
            cur = self.conn["user_store"]
            result = cur.find({"user_id": user_id})
            if cur.count_documents({"user_id": user_id}) != 0:  # 只在当前用户存在店铺时，才会进入后续操作
                for each in result:
                    store_id = each["store_id"]
                    cur = self.conn["new_order"]
                    if cur.count_documents({"store_id": store_id, "order_id": order_id}) != 0:  # 以商户身份查找成功
                        if_exists_flag = True
                        break
        else:
            # 以用户身份查找成功
            if_exists_flag = True
        if not if_exists_flag:
            return 905, "订单信息不匹配"
        # step3 查询订单结果并返回
        cur = self.conn["new_order_detail"]
        result = cur.find({"order_id": order_id})
        for each in result:
            return 200, str(each)

    def cancer(self, order_id, user_id, password):
        # step1 验证登录信息是否正确
        cur = self.conn["user"]
        if cur.count_documents({"user_id": user_id, "password": password}) == 0:
            return error.error_authorization_fail()
        # step2 验证这个用户是否确实有这个订单
        cur = self.conn["new_order"]
        if cur.count_documents({"user_id": user_id, "order_id": order_id}) == 0:
            return 905, "订单信息不匹配"
        # step3 查询订单状态，仅仅只有未付款的订单可以取消（后续或可以增加，付款未发货的也可以取消，然后执行退款操作）
        cur = self.conn["new_order_detail"]
        result = cur.find({"order_id": order_id})
        for each in result:
            state = each["state"]
            back_book_id = each["book_id"]  # 书号
            back_count = int(each["count"])  # 购买的数量
            back_price = each["price"]  # 购买的单价
            break
        cur = self.conn["new_order"]
        result = cur.find({"order_id": order_id})
        for each in result:
            back_store_id = each["store_id"]  # 售出的商店id
            back_user_id = each["user_id"]  # 购买的用户id
            break
        if state == 0:  # 订单尚未付款,只需返还数据
            # 首先删除订单信息
            cur = self.conn["new_order_detail"]
            result = cur.delete_one({"order_id": order_id})
            cur = self.conn["new_order"]
            result = cur.delete_one({"order_id": order_id})
            # 书籍返还
            cur = self.conn["store"]
            result = cur.update_one({"store_id": back_store_id, "book_id": back_book_id}, {"$inc": {"stock_level": back_count}})
        elif state == 1:  # 订单已付款，但尚未发货。此时需要退钱
            # 额外需要知道店主是谁
            cur = self.conn["user_store"]
            result = cur.find({"store_id": back_store_id})
            if cur.count_documents({"store_id": back_store_id}) == 0:
                return 919, "店铺不存在"
            for each in result:
                store_owner_id = each["user_id"]
                break
            # 查一下店主钱是否充足，如果店主钱不足，仍然无法完成取消订单
            cur = self.conn["user"]
            result = cur.find({"user_id": store_owner_id})
            if cur.count_documents({"user_id": store_owner_id}) == 0:
                return 920, "店主不存在"
            for each in result:
                seller_balance = each["balance"]
                break
            if seller_balance < back_count * back_price:
                return 921, "店主余额不足，取消订单失败"
            else:
                result = cur.update_one({"user_id": store_owner_id}, {"$set": {"balance": seller_balance - back_count * back_price}})
                if result.matched_count == 0:
                    return 922, "退款失败"
                result = cur.update_one({"user_id": back_user_id}, {"$inc": {"balance": back_count * back_price}})
                if result.matched_count == 0:
                    return 922, "退款失败"
            # 首先删除订单信息
            cur = self.conn["new_order_detail"]
            result = cur.delete_one({"order_id": order_id})
            if result.deleted_count == 0:
                return 912, "取消订单时出错"
            cur = self.conn["new_order"]
            result = cur.delete_one({"order_id": order_id})
            if result.deleted_count == 0:
                return 913, "取消订单时出错"
            # 书籍返还
            cur = self.conn["store"]
            result = cur.update_one({"store_id": back_store_id, "book_id": back_book_id}, {"$inc": {"stock_level": back_count}})
            if result.matched_count == 0:
                return 918, "返还书籍时出错"
            # 退钱
        else:
            return 917, "已发货或已收货的订单无法取消"
        return 200, "ok"

    def global_search(self, keyword):
        if keyword == '':
            return 914, "搜索关键词不能为空"
        cur = self.conn["book"]
        results = cur.find({"$text": {"$search": keyword}}).limit(10)  # 分页，最多返回10条记录
        if cur.count_documents({"$text": {"$search": keyword}}) == 0:
            return 915, "没有找到相关内容"
        return_values = ""
        for result in results:
            return_values += "标题: " + result["title"] + ", 作者: " + result["author"] + ", 介绍: " + result["book_intro"] + ", 出版年份: " + result["pub_year"] + "\n"
        return 200, return_values

    def local_search(self, keyword, store_id):
        if keyword == '':
            return 914, "搜索关键词不能为空"
        cur = self.conn["store"]
        store_info = cur.find({"store_id": store_id})
        if cur.count_documents({"store_id": store_id}) == 0:
            return 916, "该店铺不存在或没有任何在售书籍"
        book_ids = []
        for each in store_info:
            book_ids.append(each["book_id"])
        cur = self.conn["book"]
        results = cur.find({"id": {"$in": book_ids}, "$text": {"$search": keyword}}).limit(10)  # 分页，最多返回10条记录
        if cur.count_documents({"id": {"$in": book_ids}, "$text": {"$search": keyword}}) == 0:
            return 915, "没有找到相关内容"
        return_values = ""
        for result in results:
            return_values += "标题: " + result["title"] + ", 作者: " + result["author"] + ", 介绍: " + result["book_intro"] + ", 出版年份: " + result["pub_year"] + "\n"
        return 200, return_values

    def recommend(self, user_id, password):
        # 首先验证身份，只有用户本人可以进行推荐
        cur = self.conn["user"]
        if cur.count_documents({"user_id": user_id, "password": password}) == 0:
            return error.error_authorization_fail()  # 测试中，改变账号或密码即可引出此处错误
        # 获取用户的所有订单，从中解析书籍
        cur = self.conn["new_order"]
        if cur.count_documents({"user_id": user_id}) == 0:
            return 940, "用户无历史订单"  # 测试中，使用创建好的新账号进行推荐，便可引起此错误
        result = cur.find({"user_id": user_id})
        order_ids = []
        book_ids = []
        for each in result:
            order_ids.append(each["order_id"])
        cur = self.conn["new_order_detail"]
        # 在本次作业中，不可能出现此处查找失败的情况，为了便于测试，此处不添加异常判断。若为生产环境，此处也应添加异常判断语句
        cur = self.conn["new_order_detail"]
        result = cur.find({"order_id": {"$in": order_ids}})
        for each in result:
            book_ids.append(each["book_id"])
        # 同样的，在本次作业中查找书籍不可能出错，书籍必然存在，因此不加异常判断。生产环境此处也应加上判断
        cur = self.conn["book"]
        authors = []
        tags = []
        book_names = []
        result = cur.find({"id": {"$in": book_ids}})
        for each in result:
            authors.append(each["author"])
            tags.extend(each["tags"].split("\n"))
            book_names.append(each["title"])
        tags = list(filter(None, tags))
        authors = list(filter(None, authors))
        cur = self.conn["book"]
        # 便于测试开发，本处不再引入查找结果为空的错误，如果查找结果为空，返回值为""
        return_values = ""
        results = cur.find({"$text": {"$search": " ".join(tags)}}).limit(60)  #  基于tags的推荐，最多返回7条非本书的不同记录
        count = 0
        selected_ids = []
        selected_names = []
        for result in results:  # 避免选中已购买的书籍或者选中重复的书籍，下同
            if (result["id"] not in book_ids and  
                result["id"] not in selected_ids and  
                result["title"] not in book_names and  
                result["title"] not in selected_names and  
                result["title"] is not None and  
                result["author"] is not None and  
                result["book_intro"] is not None):
                return_values += "标题: " + result["title"] + ", 作者: " + result["author"] + ", 介绍: " + result["book_intro"] + "\n"
                selected_ids.append(result["id"])
                selected_ids.append(result["title"])
                count += 1
                if count == 7:
                    break
        results = cur.find({"$text": {"$search": " ".join(authors)}}).limit(30)  # 基于作者的推荐，最多返回3条非本书的记录记录
        count = 0
        for result in results:
            if (result["id"] not in book_ids and  
                result["id"] not in selected_ids and  
                result["title"] not in book_names and  
                result["title"] not in selected_names and  
                result["title"] is not None and  
                result["author"] is not None and  
                result["book_intro"] is not None):
                return_values += "标题: " + result["title"] + ", 作者: " + result["author"] + ", 介绍: " + result["book_intro"] + "\n"
                selected_ids.append(result["id"])
                selected_ids.append(result["title"])
                count += 1
                if count == 3:
                    break
        return 200, return_values