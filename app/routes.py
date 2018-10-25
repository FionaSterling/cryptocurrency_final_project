from app import app
from flask import render_template, jsonify, request
import requests
from config import API_KEY, NEWS_API_KEY
from app.candles import candlesGraph
from app.price_graph import pricesGraph


@app.route('/')
@app.route('/index')
def index():
    url = 'https://api.nomics.com/v1/currencies?key=' + API_KEY

    currencies = requests.get(url).json()

    return render_template('index.html', currencies=currencies)

@app.route('/currency')
@app.route('/currency/<id>', methods=['GET', 'POST'])
def currency(id):
    url_candles = 'https://api.nomics.com/v1/candles?key=' + API_KEY + '&interval=1d' + '&currency=' + id
    url_prices = 'https://api.nomics.com/v1/prices?key=' + API_KEY
    url_prices_history = 'https://api.nomics.com/v1/sparkline?key=' + API_KEY

    candles = requests.get(url_candles).json()
    prices = requests.get(url_prices).json()
    prices_history = requests.get(url_prices_history).json()

    # data = [0, 1, 2, 3, 4, 5]
    candlesGraph(candles)

    pricesGraph(candles)

    return render_template('currency.html', candles=candles, id=id)


@app.route('/news', methods=['GET', 'POST'])
def news():
    url_news = 'https://newsapi.org/v2/top-headlines?sources=crypto-coins-news&apiKey=' + NEWS_API_KEY

    news = requests.get(url_news).json()

    # print(news['articles'][3]['title'])
    # print(news['articles'][0]['urlToImage'])
    return render_template('news.html', news=news)