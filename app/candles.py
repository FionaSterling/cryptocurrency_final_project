# import matplotlib
# matplotlib.use('agg')
# import matplotlib.pyplot as plt
# import os
# import numpy as np
import pygal
import os
from pygal.style import DarkenStyle
darken_style = DarkenStyle('#4CAF50')



def candlesGraph(candles):
    box_plot = pygal.Box(show_legend=False, style=darken_style)
    box_plot.title = '1-Month Candlestick Graph (USD)'


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
