# 商品系统
import Balance_System
import sqlite3
import datastruct
import re

def to_float(str):
    st=str
    try:
        #print(st)
        float(st)
        return float(st)
    except ValueError as ex1: #报类型错误，说明不是整型的
        try:
            print(ex1)
            float(st) #用这个来验证，是不是浮点字符串
            return int(float(st))
        except ValueError:  #如果报错，说明即不是浮点，也不是int字符串。   是一个真正的字符串
            print("error")
        
def query_price(username,isbn):#查询价格
    conn=sqlite3.connect("Bookstore.db")
    cur=conn.cursor()
    cur.execute("select level from users where username='{}'".format(username))
    level=cur.fetchall()#看是哪个用户
    #print(level)
    cur.execute("select price from book where isbn='{}'".format(isbn))
    rs = cur.fetchall()
    price = rs[0][0]
    price = float(re.sub("[^0-9.]", "", price))
    try:
        if(to_float(str(level[0][0]))!=0):
            price*=0.8#如果VIP的话打折
            conn.commit()
            conn.close()
            return price
        conn.commit()
        conn.close()
        return price
    except Exception as ex:
        print("未找到,可能没有这本书")
        print(ex)
        conn.commit()
        conn.close()
        return 0
#print(query_price("5DFFFB7H","9787108017444"))


def get_title(isbn):#获取标题
    conn=sqlite3.connect("Bookstore.db")
    cur=conn.cursor()
    cur.execute("select title from book where isbn='{}'".format(isbn))
    title=cur.fetchall()
    conn.commit()
    conn.close()
    #print(title[0][0])
    return title[0][0]
#print(get_title("9787108017444"))


def query_addr(title):#获取图片地址
    return "./cover/{}.png".format(title)

#print(query_addr('sdasd'))

def get_book(isbn):#查询内容
    conn=sqlite3.connect("Bookstore.db")
    cur=conn.cursor()
    cur.execute("select * from book where isbn='{}'".format(isbn))
    info=cur.fetchall()
    #print(info)
    abook=datastruct.book(info[0][0],info[0][1],info[0][2],info[0][3],info[0][4],
               info[0][5],info[0][6],info[0][7],info[0][8],
               info[0][9],info[0][10])#构造函数
    conn.commit()
    conn.close()
    return abook
#print(get_book("9787108017444"))


def come_out_comment(username,isbn,comment,score):#发表评价
    conn=sqlite3.connect("Bookstore.db")
    cur=conn.cursor()
    try:
        sql="insert into payrecord values('"+username+"','"+isbn+"','"+comment+"',"+str(score)+")"
        print(sql)
        cur.execute("insert into payrecord values('"+username+"','"+isbn+"','"+comment+"',"+str(score)+")")

        conn.commit()
        conn.close()
        return True
    except Exception as ex:
        print(ex)
        conn.commit()
        conn.close()
        return False
'''
print(come_out_comment("5DFFFB7H","9787108017444","very good!",90.0))
conn=sqlite3.connect("Bookstore.db")
cur=conn.cursor()
cur.execute("select * from payrecord where score=90.0")
print(cur.fetchall())
'''

def buy_book(username,isbn):#购买书籍
    price = query_price(username,isbn)
    return Balance_System.consume(username,price)

def Fuzzy_search(title,limit,offset):#模糊查询
    title_list = list(title)

    for i in range(len(title_list) + 1):
        title_list.insert(i * 2, '%')

    title = ''.join(title_list)
    conn = sqlite3.connect("Bookstore.db")
    cur = conn.cursor()
    sql = "select ISBN from book where title like '{}' order by ISBN desc " \
          "limit '{}' offset '{}'".format(title,str(limit),str(offset))

    cur.execute(sql)
    rs = cur.fetchall()
    isbn = set()

    for line in rs:
        isbn.add(line[0])
    conn.commit()
    conn.close()
    return isbn

#print(Fuzzy_search('人',3,0))

def Book_recycling(username,ISBN):#二手书籍回收
    conn = sqlite3.connect("Bookstore.db")
    cur = conn.cursor()
    cur.execute("select price from book where ISBN ='{}'".format(ISBN))
    rs = cur.fetchall()
    price = rs[0][0]
    price = float(re.sub("[^0-9.]","",price))
    print(price)
    Balance_System(username,price*0.5)
    conn.commit()
    conn.close()

#Book_recycling('ss','9789865710965')

def query_evalue(ISBN,limit,offset):#查询评价
    conn = sqlite3.connect("Bookstore.db")
    cur = conn.cursor()
    cur.execute("select * from payrecord where ISBN ='{}' order by ISBN desc "
                "limit '{}' offset '{}'".format(ISBN,str(limit),str(offset)))

    brief = set()
    rs = cur.fetchall()
    for line in rs:
        brief.add(datastruct.userevalue(line[0],line[2],line[3]))
    conn.commit()
    conn.close()
    return brief
#query_evalue('9787510048623',3,0)

def recommend(username):#推荐书籍
    conn = sqlite3.connect("Bookstore.db")
    cur = conn.cursor()
    cur.execute("select result from recommend where username ='{}'".format(username))
    result = set()
    rs = cur.fetchall()
    for line in rs:
        line_list = line[0].split("|")
        for i in line_list:
            result.add(i)

    return result

#print(recommend('ZZ99TLD2'))