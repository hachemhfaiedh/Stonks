import pandas as pd
import numpy as np

"""we go long  (buy and hold) when the price hits the lower band, and short (sell) when it hits the upper band
our position is 1 (buy and hold) otherwise 0"""
def strategy(df):
    df['Position'] = None
    for row in range(len(df)):
        if (df['Closing Price'].iloc[row] > df['upperband'].iloc[row]) and (df['Closing Price'].iloc[row-1] < df['upperband'].iloc[row-1]):
            df['Position'].iloc[row] = 0
        if (df['Closing Price'].iloc[row] < df['lowerband'].iloc[row]) and (df['Closing Price'].iloc[row-1] > df['lowerband'].iloc[row-1]):
            df['Position'].iloc[row] = 1
    df['Position'].fillna(method='ffill',inplace=True)
    df['Position'].iloc[0] = 0
    df.dropna(inplace=True)
