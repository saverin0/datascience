import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mysavdb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)

cur = mysavdb.cursor()

cur.execute('create database fsds_db')
