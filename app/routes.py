from app import app
from flask import render_template, jsonify, request
import requests
# from config import API_KEY, NEWS_API_KEY
from app.candles import candlesGraph
from app.price_graph import pricesGraph


@app.route('/')
@app.route('/index')
def index():
    url = 'https://api.nomics.com/v1/currencies?key=' + app.config['API_KEY']

    currencies = requests.get(url).json()

    return render_template('index.html', currencies=currencies)

@lru_cache(5)
@app.route('/currency')
@app.route('/currency/<id>', methods=['GET', 'POST'])
def currency(id):
    url_candles = 'https://api.nomics.com/v1/candles?key=' + app.config['API_KEY'] + '&interval=1d' + '&currency=' + id
    url_prices = 'https://api.nomics.com/v1/prices?key=' + app.config['API_KEY']
    url_prices_history = 'https://api.nomics.com/v1/sparkline?key=' + app.config['API_KEY']
    url_news = 'https://newsapi.org/v2/top-headlines?sources=crypto-coins-news&apiKey=' + app.config['NEWS_API_KEY']

    news = requests.get(url_news).json()
    candles = requests.get(url_candles).json()
    prices = requests.get(url_prices).json()
    prices_history = requests.get(url_prices_history).json()

    def getPrice(prices):
        for coin in prices:
            if coin['currency'] == id:
                return coin['price']


    candlesGraph(candles)

    pricesGraph(candles)

    current_price = getPrice(prices)

    return render_template('currency.html', candles=candles, id=id, news=news, current_price=current_price)


@app.route('/news', methods=['GET', 'POST'])
def news():
    url_news = 'https://newsapi.org/v2/top-headlines?sources=crypto-coins-news&apiKey=' + app.config['NEWS_API_KEY']

    news = requests.get(url_news).json()

    # print(news['articles'][3]['title'])
    # print(news['articles'][0]['urlToImage'])
    return render_template('news.html', news=news)
