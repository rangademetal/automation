import mysql.connector


<<<<<<< HEAD
class Database:
    def __init__(self, host, username, password, database):
        self.host = host
        self.username = username
        self.password = password
        self.database = database

    def connection(self):
        return mysql.connector.connect(
            host=self.host,
            user=self.username,
            password=self.password,
            database=self.database)

    def get_column(self, connection, table_name):
        cursor = connection.cursor()
        cursor.execute(f"SHOW COLUMNS FROM {table_name}")
        return [i[0] for i in cursor.fetchall()]
    
    def set_values(self, max_len):
        return ', '.join(['%s' for i in range(0, max_len)])
=======
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
>>>>>>> 4e845a6422ceb710fea665bc55a0bec0f87d39cc

