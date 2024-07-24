import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mysavdb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)

cur = mysavdb.cursor()


cur.execute('select * from fsds_db.fsds1')

for i in cur:
    print(i)
