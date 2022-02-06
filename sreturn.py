import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""visualizing backtest results"""


def sreturn(df1):
    ax1 = plt.subplot(1, 2, 1)
    plt.plot(df1[['Market_Log_Return']].cumsum().apply(
        np.exp), label='Market Return')
    plt.plot(df1[['Strategy_Return']].cumsum().apply(
        np.exp), label='Strategy Return')
    plt.legend(loc=4)
    plt.xticks(rotation=15)
    plt.xlabel('Time And Date', fontsize=14)
    plt.ylabel('Return Rate', fontsize=14)
    plt.title('Merket Return vs Strategy Return')
    plt.subplot(1, 2, 2)
    plt.plot(df1[['portfolio_total']])
    plt.xticks(rotation=15)
    plt.xlabel('Time And Date', fontsize=14)
    plt.ylabel('Price In USD ($)', fontsize=14)
    plt.title('portfolio total overtime')
    plt.suptitle('Strategy Performance')
    plt.show()
