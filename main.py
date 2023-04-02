import mysql.connector
from mysql.connector import Error

class Connection:
    def __init__(self, ):

        try:
            self.conn = mysql.connector.connect(host="localhost",
                                                user="root",
                                                password="Mehulvs@99",
                                                database="sql_tutorial")
        except Error as E:
            print(E)
    def create_table(self, table_name_, scheme_):
        query = "CREATE TABLE IF NOT EXISTS {} ({})".format(table_name_, scheme_)
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print("Table created")

    def inserted_into_table(self, table_name_, scheme_, value_):
        st = scheme_.split(",")
        s = ""
        for i in st:
            print(i)
            b = i.split(" ")
            print(b)
            s = s+b[0]+","
        scheme_ = s[:len(s)-1]

        query_insert_data = "INSERT INTO {0}({1}) VALUES ({2})".format(table_name_, scheme_, value_)
        cur = self.conn.cursor()
        cur.execute(query_insert_data)
        self.conn.commit()
        print("Inserted Data")

    def select(self, table_name_, select_column):
        query_select = "SELECT {1} FROM {0}".format(table_name_, select_column)
        cur = self.conn.cursor()
        cur.execute(query_select)
        row = cur.fetchall()
        for i in row:
            print(i)
        print("table is selected")

    def update(self,table_name_, set_condition, filter_condition):
        query_update = "UPDATE {0} SET {1} WHERE {2}".format(table_name_, set_condition, filter_condition)
        cur = self.conn.cursor()
        cur.execute(query_update)
        self.conn.commit()

    def delete(self,table_name_, delete_condition):
        query_delete = "DELETE FROM {} WHERE {}".format(table_name_, delete_condition)
        cur = self.conn.cursor()
        cur.execute(query_delete)
        self.conn.commit()


c = Connection()
table_name = "Employee"
scheme = "ID int,Name Varchar(50)"
value = "1, 'Mehul'"
select_column = "ID, Name"
set_condition = "ID=4"
filter_condition = "ID=1"
delete_condition = "ID=4"
c.create_table(table_name, scheme)

c.inserted_into_table(table_name, scheme, value)
c.select(table_name, select_column)
c.update(table_name, set_condition, filter_condition)
c.delete(table_name, delete_condition)