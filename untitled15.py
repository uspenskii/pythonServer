from flask import Flask, request, render_template,url_for
import Database

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('main.html')


@app.route('/api', methods=['GET'])
def test():
    print(request.args)
    if request.args['action'] == "getGoods":
        return Database.getGoods(request.args['type'])

    if request.args['action'] == "search":
        return Database.search(request.args['request'])

    return "Error"

if __name__ == '__main__':
    for i in range(1, 255):
        try:
            app.run(host="192.168.0.{0}".format(i),)
        except Exception:
            pass
