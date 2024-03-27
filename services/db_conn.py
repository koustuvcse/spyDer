import psycopg2
from psycopg2 import Error


def open_conn(db_host, db_name, db_user, db_password):
    try:
        conn = psycopg2.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_password
        )
        print("Connected to PostgreSQL successfully!")
        return conn
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL:", error)
        return None


def close_conn(conn):
    # Close the database connection
    conn.close()
    print("Connection closed successfully!")