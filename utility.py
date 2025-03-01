import pymysql

# Establishing a connection to the database
def connect():
    try:
        conn = pymysql.connect(host='localhost', user='root', password='Varun@54', db='reccommendationmodel')
        return conn
    except:
        return False
    
def checkUser(email,password):
    conn = connect()
    if conn:
        cur = conn.cursor()
        cur.execute("select * from users where email=%s and pass=%s",(email,password))
        data = cur.fetchall()
        conn.close()
        if len(data) > 0:
            return True
        else:
            return False
    else:
        return True
    return True
    
def addUser(email,password):
    conn = connect()
    if conn:
        cur = conn.cursor()
        cur.execute("insert into users(email,pass) values(%s,%s)",(email,password))
        conn.commit()
        conn.close()
        return True
    else:
        return False