from services import db_conn

# PostgreSQL connection parameters
db_host = 'localhost'
db_name = 'visitors'
db_user = 'postgres'
db_password = 'admin'

def insertion(record, self=None):
    myconn = db_conn.open_conn(db_host, db_name, db_user, db_password)
    cur =myconn.cursor()
    print("To Be Inserted")
    print(record)
    oppop = record.pop('operation')
    columns = ', '.join(record.keys())
    placeholders = ', '.join(['%s' for _ in range(len(record))])
    insert_query = f"INSERT INTO visitors ({columns}) VALUES ({placeholders})"
    datavalues = tuple(record.values())
    cur.execute(insert_query, datavalues)
    myconn.commit()
    cur.close()
    myconn.close()

def updation(record):
    myconn = db_conn.open_conn(db_host, db_name, db_user, db_password)
    cur = myconn.cursor()
    print("To Be Updated")
    print(record)
    oppop = record.pop('operation')
    vis_id = record.get('visitor_id')


    #### Insert logic here

    update_query = f"UPDATE visitors {params} WHERE visitor_id = {vis_id}"
    cur.execute(update_query)
    myconn.commit()
    cur.close()
    myconn.close()

def deletion(record):
    myconn = db_conn.open_conn(db_host, db_name, db_user, db_password)
    cur = myconn.cursor()
    print("To Be Deleted")
    print(record)
    record.pop('operation')
    vis_id = record.get('visitor_id')
    delete_query = f"DELETE FROM visitors WHERE visitor_id = {vis_id}"
    cur.execute(delete_query)
    myconn.commit()
    cur.close()
    myconn.close()