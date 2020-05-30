import string
import sqlite3
#余额系统
def recharge(username,mon):#充值
    conn = sqlite3.connect("Bookstore.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users where username = '{}'".format(username))
    rs = cur.fetchall()
    if(rs ==[]):
        print('No such user!')
        conn.commit()
        conn.close()
        return False
    else:
        cur.execute("update users set money =money+'{}' where username = '{}'".format(mon,username))
        conn.commit()
        conn.close()
        return True


def enquiry_mon(username):#余额查询
    conn = sqlite3.connect("Bookstore.db")
    cur = conn.cursor()
    cur.execute("SELECT username,money FROM users where username = '{}'".format(username))
    rs = cur.fetchall()
    if(rs ==[]):
        print('No such user!')
        conn.commit()
        conn.close()
        return False
    else:
        for line in rs:
            print(line)
        conn.commit()
        conn.close()
        return True

def consume(username,mon):#扣费
    conn = sqlite3.connect("Bookstore.db")
    cur = conn.cursor()
    cur.execute("SELECT money FROM users where username = '{}'".format(username))
    rs = cur.fetchone()
    if(rs ==[]):
        print('No such user!')
        conn.commit()
        conn.close()
        return False
    else:
        if(rs[0]<mon):
            print('insufficient balance!')
            conn.commit()
            conn.close()
            return False
        else:
            cur.execute("update users set money =money-'{}' where username = '{}'".format(mon,username))
            conn.commit()
            conn.close()
            return True
'''
enquiry_mon('wfy11')
recharge('wfy11',50)
enquiry_mon('wfy11')
consume('wfy11',10000)
enquiry_mon('wfy11')
consume('wfy11',40)
enquiry_mon('wfy11')
'''
