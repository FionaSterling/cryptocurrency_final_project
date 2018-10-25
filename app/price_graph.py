from datetime import datetime, timedelta, date
import pygal
import os


def getDateTime(s):
    year = int(s[0:4])
    month = int(s[5:7])
    day = int(s[8:10])
    print(year, type(year), month, type(month), day, type(day))
    return datetime(year, month, day)


def pricesGraph(candles):
    date_chart = pygal.Line(x_label_rotation=20)
    date_chart.title = '10-Day Price Graph (USD)'

    count = 0
    closings = []
    dates = []

    for row in candles[-11:-1]:
        dates.append(getDateTime(row['timestamp'][0:10]))
        closings.append(float(row['close']))
        count += 1
        if count == 10:
            break

    date_chart.x_labels = map(lambda d: d.strftime('%Y-%m-%d'), dates)
    date_chart.add("Closing Prices", closings)


    path = os.path.abspath(os.path.dirname(__file__)) + './static/images/'
    filename = 'prices.svg'
    url = path + filename
    date_chart.render_to_file(url)

    return date_chart
