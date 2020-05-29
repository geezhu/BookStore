import sqlite3
import csv
conn=sqlite3.connect("Bookstore.db")
cur=conn.cursor()


cur.execute("select * from payrecord ")
rs=cur.fetchall()
print(rs)
all_time = 0
for line in rs:
    all_time += 1
    print(line)
print("总共的条目数量:%d"%(all_time))
conn.commit()
conn.close()


