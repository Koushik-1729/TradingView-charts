import plotly.graph_objs as go
import pandas as pd
import numpy as np
import random
import time
from plotly.subplots import make_subplots

def generate_tick_data(initial_price=100, num_ticks=100):
    prices = [initial_price]
    for _ in range(num_ticks):
        prices.append(prices[-1] + random.uniform(-1, 1))
    return prices

def detect_swings(prices, window=3):
    swing_highs = []
    swing_lows = []
    for i in range(window, len(prices) - window):
        if prices[i] == max(prices[i-window:i+window+1]):
            swing_highs.append((i, prices[i]))
        if prices[i] == min(prices[i-window:i+window+1]):
            swing_lows.append((i, prices[i]))
    return swing_highs, swing_lows


initial_price = 100
prices = generate_tick_data(initial_price, num_ticks=50)
swing_highs, swing_lows = detect_swings(prices)

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=list(range(len(prices))),
    y=prices,
    mode='lines',
    name='Price'
))

swing_high_x, swing_high_y = zip(*swing_highs) if swing_highs else ([], [])
swing_low_x, swing_low_y = zip(*swing_lows) if swing_lows else ([], [])

fig.add_trace(go.Scatter(
    x=swing_high_x,
    y=swing_high_y,
    mode='markers',
    marker=dict(color='red', size=10),
    name='Swing High'
))

fig.add_trace(go.Scatter(
    x=swing_low_x,
    y=swing_low_y,
    mode='markers',
    marker=dict(color='green', size=10),
    name='Swing Low'
))

fig.update_layout(
    title='Real-Time TradingView-like Chart with Swing Highs and Lows',
    xaxis_title='Time',
    yaxis_title='Price',
    showlegend=True
)
fig.show()
while True:

    new_price = prices[-1] + random.uniform(-1, 1)
    prices.append(new_price)

    swing_highs, swing_lows = detect_swings(prices)

    fig.data[0].y = prices
    fig.data[1].x, fig.data[1].y = zip(*swing_highs) if swing_highs else ([], [])
    fig.data[2].x, fig.data[2].y = zip(*swing_lows) if swing_lows else ([], []) 
    fig.update_xaxes(range=[0, len(prices)])
    time.sleep(1)