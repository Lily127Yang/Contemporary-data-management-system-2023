# 载入所需的包
import sqlite3
import pymongo


def data_construct(line):  
    one_data = {  
        "id": line[0],  
        "title": line[1],  
        "author": line[2],  
        "publisher": line[3],  
        "original_title": line[4],  
        "translator": line[5],  
        "pub_year": line[6],  
        "pages": line[7],  
        "price": line[8],  
        "currency_unit": line[9],  
        "binding": line[10],  
        "isbn": line[11],  
        "author_intro": line[12],  
        "book_intro": line[13],  
        "content": line[14],  
        "tags": line[15],
        "picture": line[16]
    }  
    return one_data


# 数据库初始化连接

# sqlite初始化
sqlite_db = sqlite3.connect("./fe/data/book.db")
cur_s = sqlite_db.cursor()

# 芒果初始化
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['bookstore']
cur_m = db['book']

sql = "select id, title, author, publisher, original_title, translator, pub_year, pages, price, currency_unit, binding, isbn, author_intro, book_intro, content, tags, picture from book"
result = cur_s.execute(sql)
book_data = []  # 储存即将插入mongo的数据
for row in result:
    book_data.append(data_construct(row))
cur_m.insert_many(book_data)