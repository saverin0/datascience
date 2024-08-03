import mysql.connector

mysavdb = mysql.connector.connect(
    host = "localhost",
    user = "abc",
    password = "password"
)
print(mysavdb)

mycursor = mysavdb.cursor()
mycursor.execute('alter table ineuron.fsds add last_name varchar(50)')