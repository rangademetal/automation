import mysql.connector


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

