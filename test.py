import sqlite3
import csv
conn=sqlite3.connect("Bookstore.db")
cur=conn.cursor()


cur.execute('select * from book ')
rs=cur.fetchall()
all_time = 0
for line in rs:
    all_time += 1
print("总共的条目数量:%d"%(all_time))
conn.commit()
conn.close()
