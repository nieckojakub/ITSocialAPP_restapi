import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBU"] = True

news = [ {'id': 0,
     'title': 'News Topic',
     'author': 'Author Name',
     'first_sentence': 'This is a test od API news. ~ jn',
     'date_published': 'Today'},]


@app.route('/', methods=["GET"])
def home():
    return "<h1>ITSocialApp</h1>"


@app.route('/newsapi', methods=["GET"])
def newsapi():
    return jsonify(news)

if __name__ == '__main__':
    app.run()


