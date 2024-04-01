# 载入所需的包
import sqlite3
import pymongo


def user_data_construct(line):
    one_data = {
        "user_id": line[0],
        "password": line[1],
        "balance": line[2],
        "token": line[3],
        "terminal": line[4]
    }
    return one_data


def user_store_data_construct(line):
    one_data = {
        "user_id": line[0],
        "store_id": line[1],
    }
    return one_data

# 数据库初始化连接

sqlite_db = sqlite3.connect("./fe/data/be.db")
cur_s = sqlite_db.cursor()
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['bookstore']
user = db['user']
user_store = db['user_store']

# user表初始化
sql = "select user_id, password, balance, token, terminal from user"
result = cur_s.execute(sql)
data_list = []  # 储存即将插入mongo的数据
for row in result:
    data_list.append(user_data_construct(row))
user.insert_many(data_list)

# user_store表初始化
sql = "select user_id, store_id from user_store"
result = cur_s.execute(sql)
data_list = []
for row in result:
    data_list.append(user_store_data_construct(row))
user_store.insert_many(data_list)