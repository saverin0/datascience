import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mysavdb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mysavdb.is_connected())

cur = mysavdb.cursor()

cur.execute("show databases")

for i in cur:
    print(i)
