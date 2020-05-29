import string
import sqlite3

def registered(username,password):#注册
    conn = sqlite3.connect("Bookstore.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users where username = '{}'".format(username))
    rs = cur.fetchall()
    if(rs == []):
        row = [username,password,"0","0.0"]
        sql = "insert into users values('{0[0]}','{0[1]}','{0[2]}'" \
              ",'{0[3]}')".format(row)
        print(sql)
        try:
            cur.execute(sql)
        except:
            conn.commit()
            conn.close()
            return False
        '''
        cur.execute("select * from users where username ='5DFB8AAM'")
        rs = cur.fetchall()
        print(rs)
        '''
        conn.commit()
        conn.close()
        return True

    else:
        conn.commit()
        conn.close()
        return False

def checkpassword(username,password):
    conn = sqlite3.connect("Bookstore.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users where username = '{}' and password = '{}'".format(username,password))
    rs = cur.fetchall()
    if(rs ==[]):
        conn.commit()
        conn.close()
        return False
    else:
        conn.commit()
        conn.close()
        return True
#print(checkpassword('5DFB8AAH','80764540'))
def join_membership(username):
    conn = sqlite3.connect("Bookstore.db")
    cur = conn.cursor()
    cur.execute("update users set level ='1' where username = '{}'".format(username))
    cur.execute("select * from users where username ='{}' and level = '{}'".format(username,"1"))
    rs = cur.fetchall()
    if(rs ==[]):
        conn.commit()
        conn.close()
        return False
    else:
        #print(rs)
        conn.commit()
        conn.close()
        return True

#print(join_membership('5DFB8AAH'))

def checkvip(username):
    conn = sqlite3.connect("Bookstore.db")
    cur = conn.cursor()
    cur.execute("select * from users where username ='{}' and level = '{}'".format(username, "1"))
    rs = cur.fetchall()
    if (rs == []):
        conn.commit()
        conn.close()
        return False
    else:
        # print(rs)
        conn.commit()
        conn.close()
        return True