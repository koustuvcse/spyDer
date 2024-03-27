import psycopg2
from psycopg2 import Error


def read_table_data(conn, table_name):
    cursor = conn.cursor()
    try:
        cursor.execute(f"SELECT * FROM {table_name};")
        rows = cursor.fetchall()
        return rows
    except (Exception, Error) as error:
        print(f"Error while reading data from table '{table_name}':", error)
        return None
    finally:
        cursor.close()


def print_table_data(rows):
    if rows is not None:
        print("Reading data from the table:")
        for row in rows:
            print(row)
