import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mysavdb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)

cur = mysavdb.cursor()

#cur.execute('create database fsds_db')


cur.execute('use fsds_db')

#cur.execute('create table fsds1 (name varchar(40) , roll_no int , mail_id varchar(50))')

cur.execute("insert into fsds1 values('Abhishek' , 4545, 'abrespect7@gmail.com')")

mysavdb.commit()

