import mysql.connector
import json


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Sad1996.",
  database='insurance'
)

mycursor = mydb.cursor()


mycursor.execute("SHOW COLUMNS FROM insurance_main")


myresult = mycursor.fetchall()
column_database = []
for x in myresult:
    column_database.append(x[0])
column_field = ','.join(column_database)
print(column_field)

string = []
for i in column_database:
    string.append('%s')
string = ','.join(string)
print(string)

with open('extract.json', 'r') as rfile:
    json_data = json.load(rfile)

for i in json_data:
    print(tuple(i.values()))
    sql = f"INSERT INTO insurance_main ({column_field}) values ({string})"  

    mycursor.execute(sql, tuple(i.values())) 
    mydb.commit() 

