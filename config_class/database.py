from calendar import c
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


# mycursor.execute('''
#     CREATE TABLE insurance_main (
#         Policy integer primary key, 
#         Expiry date not null,
#         Location varchar(20) not null,
#         State varchar(20) not null,
#         Region varchar(20) not null,
#         InsuredValue int not null,
#         Construction varchar(30) not null,
#         BusinessType varchar(30) not null,
#         Earthquake varchar(10)not null,
#         Flood varchar(10) not null
#     )''')

# # with open('extract.json', 'r') as rfile:
# #     json_data = json.load(rfile)
    


# # mycursor.execute("SHOW COLUMNS FROM insurance_main")
 
# # myresult = mycursor.fetchall()
# # column_database = []
# # for x in myresult:
# #       column_database.append(x[0])
# # print(len(column_database))

# # print(', '.join(column_database))

# # string = []
# # for i in column_database:
# #     string.append('%s')
# # print(', '.join(string))

# # sql = f"INSERT INTO in insurance_main values ({', '.join(string)})"
# # print(sql)
# # for i in json_data:
    
    
# #     print('\n\n\n\n\n\n\n')
# #     print(sql)
# #     print(tuple(column_database))
# #     print((tuple(i.values())))
# #     print('\n\n\n\n\n\n\n\n\n\n\n')

# #     mycursor.execute(sql, tuple(i.values(),))
# #     mydb.commit()

# import datetime    
# from datetime import datetime
# now = datetime.now()

# # fields = ('Policy', 'Expiry', 'Location', 'State', 'Region', 'InsuredValue', 'Construction', 'BusinessType', 'Earthquake', 'Flood')
# # values = ('1', datetime.date.today(), 'Urban', 'NY', 'East', '1617630', 'Frame', 'Retail', 'N', 'N', )
# # sql = 'INSERT INTO in insurance_main values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

# # mycursor.execute(sql, values)
# # mydb.commit()

# # mycursor = mydb.cursor()
# mycursor.execute('use insurance')
# mycursor = mydb.cursor()
# sql = "INSERT INTO in insurance_main values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
# val = ('1', '2021-12-27', 'Urban', 'NY', 'East', '1617630', 'Frame', 'Retail', 'N', 'N')
# mycursor.execute("INSERT INTO in insurance_main values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", ('1', now.strftime("%d/%m/%Y"), 'Urban', 'NY', 'East', '1617630', 'Frame', 'Retail', 'N', 'N', ))

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")