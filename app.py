import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

news = [
    {
        'id': 0,
        'source_name': 'WorldNews',
        'source_img': 'https://images.pexels.com/photos/87651/earth-blue-planet-globe-planet-87651.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500',
        'date_published': '08.09.2022',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
        'news_url': '',
        'news_img': 'https://ichef.bbci.co.uk/news/976/cpsprodpb/50D5/production/_124939602_queen_index_976x549_v3.png.webp',
        'source_url': 'worldnews.com',
        'title': 'Queen Elizabeth II has died',
        'subtitle': 'Queen Elizabeth II, the UKs longest-serving monarch, has died at Balmoral aged 96, after reigning for 70 years.'},
    {
        'id': 1,
        'source_name': 'WorldNews',
        'source_img': 'https://images.pexels.com/photos/87651/earth-blue-planet-globe-planet-87651.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500',
        'date_published': '09.09.2022',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
        'news_url': '',
        'news_img': 'https://volleyballmag.com/wp-content/uploads/2022/09/Polands-Bartocz-Kurek-goes-over-TJ-DeFalco-and-David-Smith-9-8-22-Volleyball-World-photo-2048x1365.jpeg',
        'source_url': 'worldnews.com',
        'title': 'Poland ousts USA from FIVB Men’s World Championship',
        'subtitle': 'The FIVB Men’s World Championship semifinals are set. Poland plays Brazil and Italy faces Slovenia.'},
    {
        'id': 2,
        'source_name': 'WorldNews',
        'source_img': 'https://images.pexels.com/photos/87651/earth-blue-planet-globe-planet-87651.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500',
        'date_published': '09.09.2022',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
        'news_url': '',
        'news_img': 'https://legaartis.pl/blog/wp-content/uploads/2022/08/zelensky.jpeg',
        'source_url': 'worldnews.com',
        'title': 'Zelensky claims significant gains in northeastern Ukraine as key city retaken',
        'subtitle': 'Ukrainian officials say the military has made sweeping gains in a counteroffensive in the northeastern Kharkiv region, with President Volodymyr Zelensky asserting that a key city in the region has been reclaimed by Ukrainian forces and that Russian offensives across the country are being repelled.'},
]

@app.route('/', methods=["GET"])
def home():
    return "<h1>ITSocialApp</h1>"


@app.route('/newsapi', methods=["GET"])
def newsapi():
    return jsonify(news)

if __name__ == '__main__':
    app.run()

