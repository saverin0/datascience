import mysql.connector

mysavdb = mysql.connector.connect(
    host = "localhost",
    user = "abc",
    password = "password"
)
print(mysavdb)

mycursor = mysavdb.cursor()
# mycursor.execute('create table ineuron.fsds(student_id int, first_name varchar(50) ,  registration_date DATE , class varchar(20) , course_name varchar(50))')

mycursor.execute('create table ineuron.fsds(student_id int, first_name varchar(50) ,last_name varchar(50) ,  registration_date DATE , class varchar(20) , course_name varchar(50))')
