# web scapping + yahoo finance
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import bs4 as bs
import pandas as pd
import pandas_datareader.data as web
import pickle
import requests
import os

# Candlestick graphs
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates

#style for matpltolib
style.use('ggplot')

# scrapes tickers for FTSE100 companies
def save_ftse100_tickers():
	resp = requests.get('https://en.wikipedia.org/wiki/FTSE_100_Index')
	soup = bs.BeautifulSoup(resp.text, "lxml")
	table = soup.find('table', {'class': 'wikitable sortable'})
	tickers = []
	for row in table.findAll('tr')[1:]:
		ticker = row.findAll('td')[1].text
		if ticker.endswith('.'):
			ticker = ticker[:-1]
		ticker = ticker.replace('.','-')
		tickers.append(ticker)

	with open("sp500tickers.pickle", "wb") as f:
		pickle.dump(tickers, f)

	print(tickers)

	return tickers

# Fetches data from yahoo based on tickers in directory
def get_data_from_yahoo(reload_ftse100 = False): # change this to True if u want to collect data
	if reload_ftse100:
		tickers = save_ftse100_tickers()
	else:
		with open("ftse100tickers.pickle", "rb") as f:
			tickers = pickle.load(f)

	if not os.path.exists('ftse100tickers'):
		os.makedirs('ftse100tickers')

	# specify dates
	start = dt.datetime(2000, 1, 1)
	end = dt.datetime(2018, 1, 1)

	# check whether ticker exists before fetcing them
	for ticker in tickers:
		print(ticker)
		if not os.path.exists('ftse100tickers/{}.csv'.format(ticker)):
			# replace . with - for some tickers
			df = web.DataReader(ticker+'.L', 'yahoo', start, end)
			df.to_csv('ftse100tickers/{}.csv'.format(ticker))
		else:
			print('Already have {}'.format(ticker))

#get_data_from_yahoo()


# EXAMPLE: BARCLAYS/BARC
# Yahoo uses Barc.L as a ticker
# extract
start = dt.datetime(2000,1,1)
end = dt.datetime(2018,1,1)
df = web.DataReader('BARC.L', 'yahoo', start, end)
df.to_csv('barc.csv')

# 100 day moving average
df = pd.read_csv('barc.csv', parse_dates = True, index_col = 0)
df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()

# re sample open high low close candle stick graphs
df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()
df_ohlc.reset_index(inplace=True)
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

# plot
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex = ax1)
ax1.xaxis_date()

# output
candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)
plt.show()


