import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds123003.mlab.com:23003/projectdb

host = "ds123003.mlab.com"
port = 23003 # cong vao
db_name = "projectdb"
user_name = "admin"
password = "admin1"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())