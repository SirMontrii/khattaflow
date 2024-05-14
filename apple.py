import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='root', password='MOntry@3456',database='db1')
print(mydb.connection_id)

# to execute the sql commands we have to connect cursor first
cur=mydb.cursor()

'''
to create db
cur.execute("CREATE DATABASE db1")
'''

'''
to create table
s="CREATE TABLE book(bookid integer(4),title varchar(20),prize float(5.2))"
cur.execute(s)
'''

'''
s="INSERT INTO book (bookid,title,prize) VALUES(%s,%s,%s)"
b1=(1,'Python3',345)
cur.execute(s,b1)
mydb.commit()
'''

'''
s="INSERT INTO book (bookid,title,prize) VALUES(%s,%s,%s)"
books=[(2,'PHP',345),(3,'SoloLeveling',450)]
cur.executemany(s,books)
mydb.commit()
'''

'''
s="SELECT * from book"
cur.execute(s)
result = cur.fetchall()
for rec in result:
    print(rec)
'''

s="UPDATE book SET prize=prize+10 WHERE prize>200"
cur.execute(s)
mydb.commit()

 