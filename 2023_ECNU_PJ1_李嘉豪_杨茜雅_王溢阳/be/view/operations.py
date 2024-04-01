from flask import Blueprint
from flask import request
from flask import jsonify
from be.model import operations
import json

bp_operations = Blueprint("operations", __name__, url_prefix="/operations")

# 用于卖家发货
@bp_operations.route("/delivery", methods=["POST"])
def set_delivery():
    order_id = request.json.get("order_id")
    store_id = request.json.get("store_id")
    store_owner_id = request.json.get("store_owner_id")
    password = request.json.get("password")
    o = operations.Operations()
    code, message = o.delivery(order_id, store_id, store_owner_id, password)
    return jsonify({"message": message}), code

# 用于买家收货
@bp_operations.route("/receipt", methods=["POST"])
def set_receipt():
    order_id = request.json.get("order_id")
    user_id = request.json.get("user_id")
    password = request.json.get("password")
    o = operations.Operations()
    code, message = o.receipt(order_id, user_id, password)
    return jsonify({"message": message}), code

# 用于买家查询订单
@bp_operations.route("/lookup", methods=["POST"])
def order_lookup():
    order_id = request.json.get("order_id")
    user_id = request.json.get("user_id")
    password = request.json.get("password")
    o = operations.Operations()
    code, message = o.lookup(order_id, user_id, password)
    return jsonify({"message": message}), code

# 用于取消订单
@bp_operations.route("/cancer", methods=["POST"])
def order_cancer():
    order_id = request.json.get("order_id")
    user_id = request.json.get("user_id")
    password = request.json.get("password")
    o = operations.Operations()
    code, message = o.cancer(order_id, user_id, password)
    return jsonify({"message": message}), code

# 搜索
@bp_operations.route("/search", methods=["POST"])
def book_search():
    keyword = request.json.get("keyword")
    how = request.json.get("how")  # 全局搜索还是局部搜索
    o = operations.Operations()
    if how == "local":
        store_id = request.json.get("store_id")
        code, message = o.local_search(keyword, store_id)
        return jsonify({"message": message}), code
    else:
        code, message = o.global_search(keyword)
        return jsonify({"message": message}), code

# 相似推荐 v1
@bp_operations.route("/recommend", methods=["POST"])
def book_recommend():
    """
    第一版推荐系统，在不改变原有数据表设计的条件下，根据用户历史订单推荐相似的书籍。
    由于这是一个玩具项目，也没有实际的用户，因此各类协同过滤算法无法应用于该项目。故在此采用基于规则的推荐，根据作者和tags来进行推荐。具体来说，基于作者推荐三本；基于tags推荐七本

    """
    user_id = request.json.get("user_id")
    password = request.json.get("password")
    o = operations.Operations()
    code, message = o.recommend(user_id, password)
    return jsonify({"message": message}), code