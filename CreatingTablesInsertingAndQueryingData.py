#Create & Access SQLite database using Python
import sqlite3

#Create connection object
conn = sqlite3.connect('INSTRUCTOR.db')

#Create cursor object
cursor_obj = conn.cursor()

#Drop the table if already exist
cursor_obj.execute("DROP TABLE IF EXISTS INSTRUCTOR")

#Creating table
table = "CREATE TABLE IF NOT EXISTS INSTRUCTOR(ID INTEGER PRIMARY KEY NOT NULL, FNAME VARCHAR(20), LNAME VARCHAR(20), CITY VARCHAR(20), CCODE CHAR(2));"
 
cursor_obj.execute(table)
 
print("Table is Ready")

#Insert 3 rows in the table
cursor_obj.execute("insert into INSTRUCTOR values (1, 'Rav', 'Ahuja', 'TORONTO', 'CA')")

cursor_obj.execute("insert into INSTRUCTOR values (2, 'Raul', 'Chong', 'Markham', 'CA'), (3, 'Hima', 'Vasudevan', 'Chicago', 'US')")

#Query data in the table with the fetchall() method
statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement)
print("All the data")
output_all = cursor_obj.fetchall()
for row_all in output_all:
  print(row_all)


#Fetch few rows from the table with fetchmany(numberofrows)
statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement)
print("Fetch the 2 first rows")
output_many = cursor_obj.fetchmany(2) 
for row_many in output_many:
  print(row_many)

# Fetch only FNAME from the table
statement = '''SELECT FNAME FROM INSTRUCTOR'''
cursor_obj.execute(statement)
  
print("Fetch only FNAME from the table")
output_column = cursor_obj.fetchall()
for fetch in output_column:
  print(fetch)

conn.commit()


#Retrieve data into Pandas
import pandas as pd
conn = sqlite3.connect('INSTRUCTOR.db')

df = pd.read_sql_query("select * from instructor", conn)

print(df)

#print just the LNAME for first row in the pandas data frame
print(df.LNAME[0:2])
#Shape
print(df.shape)

# Close the connection
conn.close()

