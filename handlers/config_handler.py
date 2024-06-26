from services import db_conn
from services import db_read

# PostgreSQL connection parameters
db_host = 'localhost'
db_name = 'visitors'
db_user = 'postgres'
db_password = 'admin'


def read_visitors(tablename):
    myconn = db_conn.open_conn(db_host, db_name, db_user, db_password)
    if myconn is not None:
        rows = db_read.read_table_data(myconn, tablename)
        db_read.print_table_data(rows)
        myconn.close()
        print("PostgreSQL connection is closed.")


read_visitors("visitors")
