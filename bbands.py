import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""visualizing Bollinger bands"""
def bband(df):
    plt.style.use('ggplot')
    ax = df[['Closing Price','upperband','lowerband','SMA 20']].plot(color=["crimson", "darkgray", "darkgray", "dodgerblue"], style=['-','-','-','--'])
    x_axis = df.index.get_level_values(0)
    ax.fill_between(x_axis, df['upperband'], df['lowerband'], color='lightgray')
    plt.xlabel('Time And Date')
    plt.ylabel('Price In USD ($)')
    plt.title('Bollinger Bands')
    plt.show()
