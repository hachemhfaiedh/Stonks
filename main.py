#!/usr/bin/python3
import requests
from datetime import datetime
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

strategy = __import__('strategy').strategy
bband = __import__('bbands').bband
sreturn = __import__('sreturn').sreturn

"""load data from API"""
api_key = "c17o1nf48v6tsmoj9ge0"
symbol = "AMZN"
initial_capital = 100000
indicator = 0
initial_timestamp = "1565363399"
end_timestamp = "1568041799"
url = 'https://finnhub.io/api/v1/indicator?symbol={}&resolution=1&from={}&to={}&nbdevup=2&nbdevdn=2&timeperiod=20&indicator=bbands&token={}'.format(
    symbol, initial_timestamp, end_timestamp, api_key)
res = requests.get(url)
data= json.dumps(res.json())

"""store data in dataframe"""
pd.options.mode.chained_assignment = None
pd.set_option('display.max_columns', None)
df = pd.read_json(data)
df = df.set_index('t')
df = df.drop(df.index [ [i for i in range(0,20) ] ])
df = df.rename(columns={'c': 'Closing Price'})
df = df.rename(columns={'middleband': 'SMA 20'})
df.drop(['h', 'l', 'v','o'], axis=1, inplace=True)

"""converting timestamp to datetime format"""
timestamp_list=[]
for index in df.index:
    timestamp_list.append(datetime.fromtimestamp(index))
df.index = timestamp_list

"""strategy logic"""
strategy(df)

"""Create a portfolio dataframe for series of positions, allocated against a cash component"""
df1 = df.copy()
df1.drop(['upperband','lowerband','SMA 20','s'], axis=1, inplace=True)
df1['pos_diff'] = df1['Position'].diff()
df1['number_of_shares'] = (initial_capital -(df1['Closing Price']*2)) / df1['Closing Price']
df1.loc[df1['pos_diff'] != 1,'number_of_shares'] = None
df1['number_of_shares'].iloc[0] = 0
df1['number_of_shares'].fillna(method='ffill',inplace=True)
df1['number_of_shares']= df1['number_of_shares'].astype(int)

df1['holdings'] = df1['Position'] * df1['Closing Price'] * df1['number_of_shares']
df1['cash'] = initial_capital - (df1['pos_diff'] * df1['number_of_shares'] * df1['Closing Price']).cumsum()
df1['cash'].iloc[0] = initial_capital
df1['portfolio_total'] =df1['cash'] + df1['holdings']
return_on_investment = (((-initial_capital + df1['portfolio_total'].iloc[-1]) / initial_capital ) * 100)


"""computing strategy performance using the cumulative sum of log-returns"""
df1['Market_Log_Return'] = np.log(df1['Closing Price'] / df1['Closing Price'].shift())
df1['Strategy_Return'] = (df1['Market_Log_Return'] * df1['Position'].shift(1))

"""visualizing data"""
"""technical indicators"""
bband(df)
"""strategy performance"""
sreturn(df1)
