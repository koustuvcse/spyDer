import json
from services import db_conn
from services import db_crud


filepath = 'G://codebase/spyDer/data/file.json'


def json_handler(path):
    with open(path) as file:
        data = json.load(file)
    for i in data:
        if i.get("operation") == 'insert':
            db_crud.insertion(i)
        elif i.get("operation") == 'update':
            db_crud.updation(i)
        elif i.get("operation") == 'delete':
            db_crud.deletion(i)
        else:
            print("Unknown Operation. Skipping Below")
            print(i)




json_handler(filepath)
