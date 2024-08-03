import mysql.connector
import pandas as pd

mysavdb = mysql.connector.connect(
    host = "localhost",
    user = "abc",
    password = "password"
)
print(mysavdb)

mycursor = mysavdb.cursor()

# ------------------- results displaying using pandas-----------------------------
# query = 'SELECT * FROM ineuron.fsds'
# df = pd.read_sql(query, con=mysavdb)
# print(df)
# ------------------- results displaying using pandas-----------------------------

# ------------------- code to update table --------------------------------------
# # Display the data
# print("Before update:")
# print(df)

# query = "UPDATE ineuron.fsds SET first_name = 'SAV',  last_name = 'SAV' WHERE first_name = 'Abhishek' LIMIT 1"

# # Execute the query
# mycursor.execute(query)

# # Commit the changes
# mysavdb.commit()

# # Verify the update
# select_query = "SELECT * FROM ineuron.fsds WHERE student_id = 123 AND registration_date = '2024-07-04'"
# df_updated = pd.read_sql(select_query, con=mysavdb)
# print("Updated rows:")
# print(df_updated)

# query = 'SELECT * FROM ineuron.fsds'
# df = pd.read_sql(query, con=mysavdb)

# # Display the data
# print("After update whole table:")
# print(df)
# ------------------- end of code to update table --------------------------------------


mycursor.execute("select * from ineuron.fsds")

for i in mycursor:
    print(i)

print('---------------NEW QUERY RESULTS BELOW------------------------')

mycursor.execute("select student_id,first_name from ineuron.fsds")

for i in mycursor:
    print(i)
    
print('---------------NEW QUERY RESULTS BELOW------------------------')
    
mycursor.execute("select * from ineuron.fsds where student_id = 130")

for i in mycursor:
    print(i)

print('---------------NEW QUERY RESULTS BELOW------------------------')

mycursor.execute("select * from ineuron.fsds where student_id > 130")

for i in mycursor:
    print(i)


print('---------------NEW QUERY RESULTS BELOW------------------------')

mycursor.execute("select * from ineuron.fsds where first_name ='sally' and class = 'sql' ")

for i in mycursor:
    print(i)

 