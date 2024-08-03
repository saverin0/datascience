import mysql.connector

mysavdb = mysql.connector.connect(
    host = "localhost",
    user = "abc",
    password = "password"
)
print(mysavdb)

mycursor = mysavdb.cursor()

mycursor.execute("""insert into ineuron.fsds values(123, 'Abhishek' , 'Singh', '2024-07-04' , 'sql' , 'fsds'),
(123, 'Abhishek' , 'Singh', '2024-07-04' , 'sql' , 'fsds'),
(123, 'arha' , 'rara', '2024-07-04' , 'sql' , 'fsds'),
(124, 'See' , 'wai', '2024-07-04' , 'sql' , 'fsds'),
(125, 'Jolene' , 'vanessa', '2024-07-04' , 'sql' , 'fsds'),
(126, 'Sarah' , 'jane', '2024-07-04' , 'sql' , 'fsds'),
(127, 'Quanh' , 'Anh', '2024-07-04' , 'sql' , 'fsds'),
(128, 'Seph' , 'bulan', '2024-07-04' , 'sql' , 'fsds'),
(129, 'korra' , '37', '2024-07-04' , 'sql' , 'fsds'),
(130, 'jo' , 'minecrafter', '2024-07-04' , 'sql' , 'fsds'),
(131, 'jas' , 'jasmine', '2024-07-04' , 'sql' , 'fsds'),
(132, 'lav' , 'cecilia', '2024-07-04' , 'sql' , 'fsds'),
(133, 'sally' , 'salvator', '2024-07-04' , 'sql' , 'fsds'),
(134, 'bri' , 'bri', '2024-07-04' , 'sql' , 'fsds'),
(135, 'sav' , 's.averino', '2024-07-04' , 'sql' , 'fsds')""")


mysavdb.commit()

mycursor.execute("select * from ineuron.fsds")

for i in mycursor:
    print(i)