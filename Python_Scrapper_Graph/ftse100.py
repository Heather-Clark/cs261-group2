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
import json

# Graphs + Data
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates
import urllib2 # use urllib.request for python 3
import decimal

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
	end = dt.datetime.now()

	# check whether ticker exists before fetcing them
	for ticker in tickers:
		print(ticker)
		if not os.path.exists('ftse100tickers/{}.csv'.format(ticker)):
			# replace . with - for some tickers
			df = web.DataReader(ticker+'.L', 'yahoo', start, end)
			df.to_csv('ftse100tickers/{}.csv'.format(ticker))
		else:
			print('Already have {}'.format(ticker))

################################################## Basic Statistics
def get_current_spot_price(ticker):
	df = pd.read_csv("ftse100tickers/"+ticker+".csv")
	price = df.iloc[-2,4]
	return price

print("Current Spot Price of BARC is ", get_current_spot_price("BARC"))

def get_current_trading_volume(ticker):
	df = pd.read_csv("ftse100tickers/"+ticker+".csv")
	volume = df.iloc[-2,6]
	return volume

print("Current Trading Volume for BARC is", get_current_trading_volume("BARC"))

def get_percentage_change_daily(ticker):
	df = pd.read_csv("ftse100tickers/"+ticker+".csv")
	yesterday_close = df.iloc[-3,5]
	today_close = df.iloc[-2,5]
	return (today_close - yesterday_close) * 100 / today_close

print("Percentage Change daily is %", get_percentage_change_daily("BARC"))

def get_specific_spot_price(ticker, date):
	df = pd.read_csv("ftse100tickers/"+ticker+".csv")
	row = df[df['Date'] == date]
	price = row.iloc[0,4]
	return price

print("Specific spot price in year 2000 is", get_specific_spot_price("BARC", '2000-02-01'))

def get_specific_trading_volume(ticker, date):
	df = pd.read_csv("ftse100tickers/"+ticker+".csv")
	row = df[df['Date'] == date]
	volume = row.iloc[0,6]
	return volume

print("Specific trading volume in year 2000 is", get_specific_trading_volume("BARC", '2000-02-01'))

def get_profit_period(ticker):
	response = urllib2.urlopen("https://query2.finance.yahoo.com/v10/finance/quoteSummary/"+ticker+".L?modules=financialData")
	data = json.load(response)
	profitMargins = json.dumps(data['quoteSummary']['result'][0]['financialData']['profitMargins']['raw'])
	revenue = json.dumps(data['quoteSummary']['result'][0]['financialData']['totalRevenue']['raw'])
	profit = float(profitMargins) - float(revenue)
	return profit

print("Profit in 2017 is", get_profit_period("BARC"))

def get_eps_year(ticker):
	response = urllib2.urlopen("https://query2.finance.yahoo.com/v10/finance/quoteSummary/"+ticker+".L?modules=defaultKeyStatistics")
	data = json.load(response)
	trailingEps = json.dumps(data['quoteSummary']['result'][0]['defaultKeyStatistics']['trailingEps']['raw'])
	forwardEps = json.dumps(data['quoteSummary']['result'][0]['defaultKeyStatistics']['forwardEps']['raw'])
	return (trailingEps, forwardEps)

print("Trailing EPS and forward EPS is", get_eps_year("BARC"))

# OK this is probably wrong.... idk how to calculate div per share
def get_dividend_per_share(ticker):
	response = urllib2.urlopen("https://query2.finance.yahoo.com/v10/finance/quoteSummary/"+ticker+".L?modules=cashflowStatementHistory,defaultKeyStatistics")
	data = json.load(response)
	dividends = json.dumps(data['quoteSummary']['result'][0]['cashflowStatementHistory']['cashflowStatements'][0]['dividendsPaid']['raw'])
	outstandingShares = json.dumps(data['quoteSummary']['result'][0]['defaultKeyStatistics']['sharesOutstanding']['raw'])
	dps = -float(dividends) / float(outstandingShares)
	return dps

print("Dividend per share in 2017 is", get_dividend_per_share("BARC"))

################################################## Group Statistics
# Helper Function
def get_tickers(industry):
	resp = requests.get('https://en.wikipedia.org/wiki/FTSE_100_Index')
	soup = bs.BeautifulSoup(resp.text, "lxml")
	table = soup.find('table', {'class': 'wikitable sortable'})
	tickers = []
	for row in table.findAll('tr')[1:]:
		if(row('td')[2].text == industry):
			ticker = row('td')[1].text
			if ticker.endswith('.'):
				ticker = ticker[:-1]
			ticker = ticker.replace('.','-')
			tickers.append(ticker)

	with open("sp500tickers.pickle", "wb") as f:
		pickle.dump(tickers, f)
	return tickers

def get_industry_trend(industry):
	tickers = get_tickers(industry)
	industry = 0;
	for ticker in tickers:
		df = pd.read_csv("ftse100tickers/"+ticker+".csv")
		dayOne = df.iloc[-5,4]
		dayFive = df.iloc[-1,4]
		percentageChange = (dayFive - dayOne) / dayOne * 100
		industry = industry + percentageChange

	industry = industry / len(tickers)

	return industry

print("Trend (5 days) for companies in 'Industrial Metals & Mining' industry is ", get_industry_trend("Industrial Metals & Mining"))

def get_industry_trend_today(industry):
	tickers = get_tickers(industry)
	industry = 0;
	for ticker in tickers:
		df = pd.read_csv("ftse100tickers/"+ticker+".csv")
		dayOne = df.iloc[-2,4]
		dayFive = df.iloc[-1,4]
		percentageChange = (dayFive - dayOne) / dayOne * 100
		industry = industry + percentageChange

	industry = industry / len(tickers)

	return industry

print("Trend (today) for companies in 'Industrial Metals & Mining' industry is ", get_industry_trend_today("Industrial Metals & Mining"))

def get_companies_industry_trend(industry, trend): # True - Rising, False - Falling
	tickers = get_tickers(industry)
	data = []
	for ticker in tickers:
		df = pd.read_csv("ftse100tickers/"+ticker+".csv")
		dayOne = df.iloc[-5,4]
		dayFive = df.iloc[-1,4]
		percentageChange = (dayFive - dayOne) / dayOne * 100

		if(trend):
			if(percentageChange > 0):
				data.append(ticker)
		else:
			if(percentageChange < 0):
				data.append(ticker)
	return data

print("Company tickers that are rising (5 day trend) are:", get_companies_industry_trend("Banks", False))

################################################## News related stuff.
def get_news_industry(industry):
	tickers = get_tickers(industry)
	signal = False

	# beautiful soup
	sauce = urllib2.urlopen("http://feeds.reuters.com/reuters/UKBankingFinancial").read() # yahoo rss finance not availabe. use reuters instead
	soup = bs.BeautifulSoup(sauce, 'xml')

	sentence = ""

	# web scrapping
	for url in soup.find_all('item'):
		title = url.title.text
		desc = url.description.text

		sentence = title + desc

		for ticker in tickers:
			if ticker in sentence:
				signal = True

	return(signal)

print("Is this industry in the news?", get_news_industry("Banks"))

def get_sentiment_analysis(industry):
	get_tickers(industry)
	# TODO: news_scrapper.py here

################################################## Comparative queries.
def get_compare_tickers_weekly(tickers, Trend = True):
	
	currentTicker = 0;
	currentPercentage = -100;

	#tickers is an array of ticker #Trend
	for ticker in tickers:
		df = pd.read_csv("ftse100tickers/"+ticker+".csv")
		dayOne = df.iloc[-5,4]
		dayFive = df.iloc[-1,4]
		percentageChange = (dayFive - dayOne) / dayOne * 100
		# print(ticker, percentageChange)
		if(percentageChange > currentPercentage):
			currentTicker = ticker

	return currentTicker

print("Best Ticker weekly is:", get_compare_tickers_weekly(["BARC","HSBA"]))

def get_compare_tickers_daily(tickers, Trend = True):
	
	currentTicker = 0;
	currentPercentage = -100;

	#tickers is an array of ticker #Trend
	for ticker in tickers:
		df = pd.read_csv("ftse100tickers/"+ticker+".csv")
		dayOne = df.iloc[-2,4]
		dayFive = df.iloc[-1,4]
		percentageChange = (dayFive - dayOne) / dayOne * 100
		# print(ticker, percentageChange)
		if(percentageChange > currentPercentage):
			currentTicker = ticker

	return currentTicker

print("Best Ticker daily is:",get_compare_tickers_daily(["BARC","HSBA"]))

def get_compare_tickers_monthly(tickers, Trend = True):
	
	currentTicker = 0;
	currentPercentage = -100;

	#tickers is an array of ticker #Trend
	for ticker in tickers:
		df = pd.read_csv("ftse100tickers/"+ticker+".csv")
		dayOne = df.iloc[-30,4]
		dayFive = df.iloc[-1,4]
		percentageChange = (dayFive - dayOne) / dayOne * 100
		# print(ticker, percentageChange)
		if(percentageChange > currentPercentage):
			currentTicker = ticker

	return currentTicker

print("Best Ticker monthly is:",get_compare_tickers_monthly(["BARC","HSBA"]))

################################################## Subjective queries
# def get_tickers_to_invest(): IDK, this is hard

def get_best_ticker_in_industry(industry):
	tickers = get_tickers(industry)

	currentTicker = 0;
	currentPercentage = -100;

	#tickers is an array of ticker #Trend
	for ticker in tickers:
		df = pd.read_csv("ftse100tickers/"+ticker+".csv")
		dayOne = df.iloc[-365,4]
		dayFive = df.iloc[-1,4]
		percentageChange = (dayFive - dayOne) / dayOne * 100
		# print(ticker, percentageChange)
		if(percentageChange > currentPercentage):
			currentTicker = ticker

	return currentTicker

print("Best ticker in this industry over 365 days is", get_best_ticker_in_industry("Banks"))