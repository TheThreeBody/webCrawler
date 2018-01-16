from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }]


@app.route('/')
def index():
    return 'Hello World'


@app.route('/getNum/miaopai', methods=['GET'])
def get_num_miaopai():
    import getNum.MiaoPai
    url = request.args.get('url')
    if request.args.get('url'):
        crawler = getNum.MiaoPai.MiaoPai(url=url)
    else:
        crawler = getNum.MiaoPai.MiaoPai()
    return jsonify({'lists': crawler.getnum()})








@app.route('/test')
def get_test():
    return 'Hello'


if __name__ == "__main__":
    app.run(debug=True)