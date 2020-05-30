import CF_two
import sqlite3

conn = sqlite3.connect("Bookstore.db")
cur = conn.cursor()
try:
    cur.execute("drop table recommend")
except:
    print("该表原本就不存在")

cur.execute("create table recommend(username varchar(20) , result varchar(200),FOREIGN KEY(username) REFERENCES users(username))")
d = {}
d = CF_two.recommend()

for key , value in d.items():
    value_str = ""
    value_str = "|".join(value)
    sql = "insert into recommend values ('{}','{}')".format(key,value_str)
    print(sql)
    cur.execute(sql)

conn.commit()
conn.close()
'''
cur.execute("select * from recommend")

rs=cur.fetchall()
for line in rs:
    print(line)
'''