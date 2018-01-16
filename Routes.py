from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'


# get num from miaopai. pass the url of personal home page
@app.route('/getNum/miaopai', methods=['GET'])
def get_num_miaopai():
    import getNum.MiaoPai
    url = request.args.get('url')
    if request.args.get('url'):
        crawler = getNum.MiaoPai.MiaoPai(url=url)
    else:
        crawler = getNum.MiaoPai.MiaoPai()
    return jsonify({'lists': crawler.getnum()})


if __name__ == "__main__":
    app.run(debug=True)