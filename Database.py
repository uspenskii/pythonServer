DATABASE = "C:\\untitled15\\Shop.sqlite"
def getGoods():
    import sqlite3,json
    conn = sqlite3.connect(DATABASE)
    cursor = conn.execute("SELECT * FROM Goods WHERE type IS \'{0}\'".format("ass"))
    data = cursor.fetchall()
    a = []
    print(data)
    for i in range(len(data)):
        a.append({'id': data[i][0], 'text': data[i][1], 'image': data[i][2]})

    return json.dumps({'count':len(a),'GoodsList':a})