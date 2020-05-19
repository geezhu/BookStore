import sqlite3
import numpy as np
import CF
isbn = []
isbn_num = {}
conn=sqlite3.connect("Bookstore.db")
cur=conn.cursor()
cur.execute('select ISBN from book')

rs=cur.fetchall()

for line in rs:
    #print(line)
    isbn.append(line[0])
print(isbn)
i = 0
for num in isbn:
    isbn_num[num] = i
    i += 1
print(isbn_num)
username = []
username_num = {}
cur.execute('select username from users')

rs=cur.fetchall()

for line in rs:
    #print(line)
    username.append(line[0])
print(username)
i = 0
for num in username:
    username_num[num] = i
    i += 1
print(username_num)
evalution = []
cur.execute('select username,ISBN,score from payrecord')

rs=cur.fetchall()

for line in rs:
    #print(line)
    evalution.append([line[0],line[1],line[2]])

print(evalution)
conn.commit()
conn.close()

data = np.full([len(username),len(isbn)],0.0)
for evale in evalution:
    try:
        data[username_num[evale[0]]][isbn_num[evale[1]]] = evale[2]
    except:
        print(evale)

print(data)
cf = CF.CF_knearest(k=3)
print(cf.fit(data))


