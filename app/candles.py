# import matplotlib
# matplotlib.use('agg')
# import matplotlib.pyplot as plt
# import os
# import numpy as np
import pygal
import os



def candlesGraph(candles):
    box_plot = pygal.Box()
    # box_plot.y_labels = 5500, 6000, 6500, 7000, 7500, 8000
    box_plot.title = '1-Month Candlestick Graph (USD)'

    # using the value of the variable below for date string in box plot legend
    # date = candles[0]['timestamp'][5:10]

# [::-1] to reverse date order
    count = 0
    for row in candles[-31:-1]:
        box_plot.add(row['timestamp'][0:10], [float(row['low']), float(row['high']), float(row['open']), float(row['close'])])
        count += 1
        if count == 30:
            break

    box_plot.render()

    path = os.path.abspath(os.path.dirname(__file__)) + './static/images/'
    filename = 'candles.svg'
    url = path + filename
    box_plot.render_to_file(url)

    return box_plot
