import bs4 as bs
import urllib.request
import json

#from nltk.sentiment.util import *
#from nltk.sentiment.vader import SentimentIntensityAnalyzer

# mkdir ./nltk_data
# python -m nltk.downloader
# Set Download Directory in GUI
#nltk.data.path.append('./nltk_data/')

#ticker = raw_input("Enter Stock Ticker Symbol (i.e. AAPL, FB, TSLA):\n")
#ticker = "FB"

# beautiful soup
def get_news(ticker):
	with urllib.request.urlopen("https://feeds.finance.yahoo.com/rss/2.0/headline?s="+ticker+".L") as url:
		sauce = url.read().decode()
	soup = bs.BeautifulSoup(sauce, 'xml')

	data = []
	sentences = []

	# web scrapping
	for url in soup.find_all('item'):
		title = url.title.text
		desc = url.description.text
		link = url.link.text
		pubDate = url.pubDate.text
		article = {
					"title": title,
					"desc": desc,
					"link": link,
					"pubDate": pubDate
				  }
		data.append(article)
		sentences.append(title + ". " + desc)
	
	# dump data into json file
	# data = json.dumps(data)
	data = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
	print(data[0])
	return data

# Sentiment Intensity Analysis for each individual news article title + brief description
# can be improved if entire article is used instead?
#sid = SentimentIntensityAnalyzer()
#for sentence in sentences:
#	print(sentence)
#	ss = sid.polarity_scores(sentence)
#	for k in sorted(ss):
#		print('{0}: {1}, '.format(k, ss[k]))
#	print()