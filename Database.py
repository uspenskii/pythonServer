import os
import sqlite3, json
DATABASE = os.path.dirname(os.path.abspath(__file__)) + "/Shop.sqlite"
print(DATABASE)

def getGoods(typeRec):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.execute("SELECT * FROM Goods WHERE type IS \'{0}\'".format(typeRec))

    data = cursor.fetchall()
    a = []
    print(data)
    for i in range(len(data)):
        a.append({'id': data[i][0], 'text': data[i][1], 'image': data[i][2]})

    return json.dumps({'count': len(a), 'list': a})

def search(searchRequest):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.execute("SELECT * FROM Goods WHERE name LIKE '%{0}%'".format(searchRequest))

    data = cursor.fetchall()
    a = []
    print(data)
    for i in range(len(data)):
        a.append({'id': data[i][0], 'text': data[i][1], 'image': data[i][2]})

    return json.dumps({'count': len(a), 'list': a})
