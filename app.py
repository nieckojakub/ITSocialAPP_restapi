import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBU"] = True

news = [ {'id': 0,
     'title': 'Queen Elizabeth II has died',
     'text': 'Queen Elizabeth II, the UKs longest-serving monarch, has died at Balmoral aged 96, after reigning for 70 years. She died peacefully on Thursday afternoon at her Scottish estate, where she had spent much of the summer.',
     'date_published': '08.09.2022',
    'img': 'https://ichef.bbci.co.uk/news/976/cpsprodpb/50D5/production/_124939602_queen_index_976x549_v3.png.webp'},

    {'id': 1,
     'title': 'Poland ousts USA from FIVB Men’s World Championship',
     'text': 'The FIVB Men’s World Championship semifinals are set. Poland plays Brazil and Italy faces Slovenia.',
     'date_published': '09.09.2022',
        'img':'https://volleyballmag.com/wp-content/uploads/2022/09/Polands-Bartocz-Kurek-goes-over-TJ-DeFalco-and-David-Smith-9-8-22-Volleyball-World-photo-2048x1365.jpeg'},

        {'id': 2,
     'title': 'Zelensky claims significant gains in northeastern Ukraine as key city retaken',
     'text': 'Ukrainian officials say the military has made sweeping gains in a counteroffensive in the northeastern Kharkiv region, with President Volodymyr Zelensky asserting that a key city in the region has been reclaimed by Ukrainian forces and that Russian offensives across the country are being repelled.',
     'date_published': '09.09.2022',
        'img':'https://legaartis.pl/blog/wp-content/uploads/2022/08/zelensky.jpeg'}
          
          ]


@app.route('/', methods=["GET"])
def home():
    return "<h1>ITSocialApp</h1>"


@app.route('/newsapi', methods=["GET"])
def newsapi():
    return jsonify(news)

if __name__ == '__main__':
    app.run()

