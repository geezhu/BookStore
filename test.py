import sqlite3
import csv
conn=sqlite3.connect("Bookstore.db")
cur=conn.cursor()


cur.execute('select * from book ')
rs=cur.fetchall()
all_time = 0
for line in rs:
    all_time += 1
    print(line)
print(all_time)
conn.commit()
conn.close()
