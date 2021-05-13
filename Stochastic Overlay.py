import pandas_datareader as pdr
import datetime as dt
import matplotlib.pyplot as plt

ticker = pdr.get_data_yahoo("AAPL", dt.datetime(2020, 1, 1), dt.datetime.now())
ticker['H14'] = ticker['High'].rolling(14).max()
ticker['L14'] = ticker['Low'].rolling(14).min()
ticker['%K'] = (ticker['Close'] - ticker['L14'])*100/(ticker['H14'] - ticker['L14'])
ticker['%D'] = ticker['%K'].rolling(3).mean()
ax = ticker[['%K', '%D']].plot(); ax.set_title('Stochastic Oscillator')

ticker['Adj Close'].plot(ax=ax, secondary_y=True)

ax.axhline(20, linestyle='--', color="r")
ax.axhline(80, linestyle='--', color="r")