
import json
from urllib.request import urlopen
# example reading
response = urlopen("http://127.0.0.1:5000/api?action=getGoods").read().decode('utf8')
obj = json.loads(response)
for i in  obj['GoodsList']:
    print(i['image'])