from django.http import HttpResponse
from django.shortcuts import render
from django.utils.html import escape

from history import models

import requests
import json
import os
import datetime
import cs261.utility as util


# Where the magic happens.
# i.e. this is where we interface with the app logic.
def query(request):
    q_text = request.GET.get('q', 'No query')

    params = {
        'query': q_text,
        'sessionId': '1',
        'v': '20150910',
        'lang': 'en'
    }

    headers = {
        'Authorization': 'Bearer b1d37306df854c57a511e912233cc845'# + os.environ['BOT_TOKEN']
    }

    r = requests.get('https://api.dialogflow.com/v1/query', params=params, headers=headers)

    try:
        resp = r.json()
        text = process(resp)
    except KeyError:
        text = 'Something went wrong. Please try again.'

    # store history and file log
    #with open('logs/' + datetime.datetime.now().strftime('%Y-%m-%d-T%H-%M-%S.json'), 'w+') as f:
    #    f.write(json.dumps(r.json(), indent=2))

    intent = None
    try:
        intent = r.json()['result']['metadata']['intentName']
        entities = r.json()['result']['parameters']
        for i in entities:
            if (type(entities[i]) != list):
                continue

            q = models.Query(text=q_text, intent=intent)
            q.save()
            for j in entities[i]:
                entity, created = models.Entity.objects.get_or_create(entity_type=i, name=j)
                q.entities.add(entity)
            q.save()
    except:
        print('error')

    # make response
    context = {
        'message': text
    }

    return render(request, 'cs261/response.html', context=context)


# 1) Identify intent and parameters
# 2) Process query
# 3) return text
def process(resp):
    intent = resp['result']['metadata']['intentName']
    print(json.dumps(resp, indent=2))
    print(intent)

    # HOW IT WORKS:
    # use util functions to process data based on the intent
    # use pass to use default output from dialogflow
    # Switch equivalent for intents
    
    # DONE
    if intent == 'SpotPrice':
        ticker = resp['result']['parameters']['FTSE100'][0]
        ticker = ticker[:-2]
        text = str(round(util.get_close_spot_price(ticker),2))
        text = "The current spot price of " + ticker + " is " + text + " GBP"

    # DONE
    elif intent == 'SpotPrice - AfterOther':
        ticker = resp['result']['parameters']['FTSE100'][0]
        ticker = ticker[:-2]
        text = str(round(util.get_close_spot_price(ticker),2))
        text = "The current spot price of " + ticker + " is " + text + " GBP"

    # DONE
    elif intent == 'StockHigh':
        ticker = resp['result']['parameters']['FTSE100'][0]
        ticker = ticker[:-2]
        text = str(round(util.get_high_spot_price(ticker),2))
        text = "The current high price of " + ticker + " is " + text + " GBP"

    # DONE
    elif intent == 'StockHigh - AfterOther':
        ticker = resp['result']['parameters']['FTSE100'][0]
        ticker = ticker[:-2]
        text = str(round(util.get_high_spot_price(ticker),2))
        text = "The current high price of " + ticker + " is " + text + " GBP"

    # DONE
    elif intent == 'StockLow':
        ticker = resp['result']['parameters']['FTSE100'][0]
        ticker = ticker[:-2]
        text = str(round(util.get_low_spot_price(ticker),2))
        text = "The current low price of " + ticker + " is " + text + " GBP"

    # DONE
    elif intent == 'StockLow - AfterOther':
        ticker = resp['result']['parameters']['FTSE100'][0]
        ticker = ticker[:-2]
        text = str(round(util.get_low_spot_price(ticker),2))
        text = "The current low price of " + ticker + " is " + text + " GBP"

    # DONE
    elif intent == 'OpenPrice':
        ticker = resp['result']['parameters']['FTSE100'][0]
        ticker = ticker[:-2]
        text = str(round(util.get_open_spot_price(ticker),2))
        text = "The current open price of " + ticker + " is " + text + " GBP"

    # DONE
    elif intent == 'OpenPrice - AfterOther':
        ticker = resp['result']['parameters']['FTSE100'][0]
        ticker = ticker[:-2]
        text = str(round(util.get_open_spot_price(ticker),2))
        text = "The current open price of " + ticker + " is " + text + " GBP"

    elif intent == 'PriceRatio':
        text = resp['result']['fulfillment']['speech']
        pass

    elif intent == 'PriceRatio - AfterOther':
        text = resp['result']['fulfillment']['speech']
        pass

    # DONE
    elif intent == 'VolumeTraded':
        ticker = resp['result']['parameters']['FTSE100'][0]
        ticker = ticker[:-2]
        text = str(round(util.get_trading_volume(ticker), 2))
        text = "The current volume of " + ticker + " is " + text

    # DONE
    elif intent == 'VolumeTraded - AfterOther':
        ticker = resp['result']['parameters']['FTSE100'][0]
        ticker = ticker[:-2]
        text = str(round(util.get_trading_volume(ticker), 2))
        text = "The current volume of " + ticker + " is " + text

    # DONE
    elif intent == 'AverageVolume':
        ticker = resp['result']['parameters']['FTSE100'][0]
        ticker = ticker[:-2]
        text = str(round(util.get_average_trading_volume(ticker), 2))
        text = "The average volume (weekly) of " + ticker + " is " + text

    # DONE
    elif intent == 'AverageVolume - AfterOther':
        ticker = resp['result']['parameters']['FTSE100'][0]
        ticker = ticker[:-2]
        text = str(round(util.get_average_trading_volume(ticker), 2))
        text = "The average volume (weekly) of " + ticker + " is " + text

    elif intent == 'isRising':
        text = resp['result']['fulfillment']['speech']
        pass

    elif intent == 'isRising - AfterOther':
        text = resp['result']['fulfillment']['speech']
        pass

    elif intent == 'isFalling':
        text = resp['result']['fulfillment']['speech']
        pass

    elif intent == 'isFalling - AfterOther':
        text = resp['result']['fulfillment']['speech']
        pass

    # DONE
    elif intent == 'PercentChange':
        ticker = resp['result']['parameters']['FTSE100'][0]
        ticker = ticker[:-2]
        text = str(round(util.get_percentage_change(ticker), 2))
        text = "The percentage change of " + ticker + " is " + text + "%"

    # DONE
    elif intent == 'PercentChange - AfterOther':
        ticker = resp['result']['parameters']['FTSE100'][0]
        ticker = ticker[:-2]
        text = str(round(util.get_percentage_change(ticker), 2))
        text = "The percentage change of " + ticker + " is " + text + "%"

    # DONE
    elif intent == 'ValueChange':
        ticker = resp['result']['parameters']['FTSE100'][0]
        ticker = ticker[:-2]
        text = str(round(util.get_value_change(ticker), 2))
        text = "The value change of " + ticker + " is " + text

    # DONE
    elif intent == 'ValueChange - AfterOther':
        ticker = resp['result']['parameters']['FTSE100']
        ticker = ticker[:-2]
        text = str(round(util.get_value_change(ticker), 2))
        text = "The value change of " + ticker + " is " + text

    # DONE
    # TODO: Think of what to do with news object
    elif intent == 'NewsIntent':
        ticker = resp['result']['parameters']['FTSE100']
        ticker = ticker[:-2]
        articles = []
        news = util.get_news_stock(ticker)
        for i in range(0,len(news)):
            # TODO: find a way to show this
            news[i].desc 
            news[i].link
            news[i].pubDate
            news[i].title
            articles.append(news[i].title)

        text = articles

    # DONE
    elif intent == 'SpotPriceDate':
        ticker = resp['result']['parameters']['FTSE100']
        ticker = ticker[:-2]
        date = resp['result']['parameters']['date']
        text = str(round(util.get_spot_price_date(ticker, date), 2))
        text = "The spot price of " + ticker + " in " + date + " is " + text + " GBP"

    # DONE
    elif intent == 'VolumeTradedDate':
        ticker = resp['result']['parameters']['FTSE100']
        ticker = ticker[:-2]
        date = resp['result']['parameters']['date']
        text = str(round(util.get_trading_volume_date(ticker, date), 2))
        text = "The volume traded, " + ticker + " in " + date + " is " + text

    # DONE
    elif intent =='StockProfit':
        ticker = resp['result']['parameters']['FTSE100']
        ticker = ticker[:-2]
        text = str(round(util.get_profit(ticker), 2))
        text = "The raw profit margin of " + ticker + " is " + text

    # DONE
    elif intent == 'StockEPS':
        ticker = resp['result']['parameters']['FTSE100']
        ticker = ticker[:-2]
        text = str(util.get_eps(ticker))
        text = "The trailing/forward EPS of " + ticker + " is " + text + " GBP"

    # DONE
    elif intent == 'StockDividend':
        ticker = resp['result']['parameters']['FTSE100']
        ticker = ticker[:-2]
        text = str(round(util.get_dividend(ticker), 2))
        text = "The latest stock dividends of " + ticker + " is " + text

# TODO: use web scrapper to get percentage of industry
    #DONE
    elif intent == 'IndustryIsRising':
        industry = resp['result']['parameters']['Sectors']
        trend = util.get_industry_trend_weekly(industry)
        if trend >= 0:
            text = "Yes, the industry " + industry + " is rising"
        else: 
            text = "No, the industry " + industry + " is falling"

    # DONE
    elif intent == 'IndustryPercentChange':
        industry = resp['result']['parameters']['Sector']
        text = str(round(util.get_industry_trend_daily(industry), 2))
        text = "The percentage change of industry: " + industry + " is " + text + "%"

    # DONE
    elif intent == 'IndustryRisingStock':
        industry = resp['result']['parameters']['Sectors']
        text = str(util.get_tickers_industry_trend(industry, True))
        text = "Rising tickers in " + industry + " are " + text

    # DONE
    elif intent == 'IndustryFallingStock':
        industry = resp['result']['parameters']['Sectors']
        text = util.get_tickers_industry_trend(industry, False)
        text = str(text)
        text = "Falling tickers in " + industry + " are " + text

    # DONE
    elif intent == 'IndustryNews':
        industry = resp['result']['parameters']['Sectors']
        text = util.get_news_industry(industry)
        if text == True:
            text = "Yes, ask me more about the industry."
        else:
            text = "No. But Food and Drugs Retailer is in the news (When i was being tested). Try asking me this again"

    elif intent == 'StockNews':
        ticker = resp['result']['parameters']['FTSE100']
        ticker = ticker[:-2]
        text = util.get_sentiment_analysis(ticker)


    elif intent == 'SentimentAnalysisStock':
        ticker = resp['result']['parameters']['FTSE100']
        ticker = ticker[:-2]
        text = util.get_sentiment_analysis(ticker)

    # DONE
    elif intent == 'CompareStockBetter':
        tickers = []

        # is this?
        first = resp['result']['parameters']['FTSE100']
        first = first[:-2]
        tickers.append(first)

        # better than that?
        second = resp['result']['parameters']['FTSE1001']
        second = second[:-2]
        tickers.append(second)

        if(util.get_compare_tickers_weekly(tickers) == first):
            text = "Yes, it is doing better."
        else:
            text = "No, it is doing worse." 

    # DONE
    elif intent == 'CompareStockWeekly':
        tickers = []

        # is this?
        first = resp['result']['parameters']['FTSE100']
        first = first[:-2]
        tickers.append(first)

        # better than that?
        second = resp['result']['parameters']['FTSE1001']
        second = second[:-2]
        tickers.append(second)

        text = str(util.get_compare_tickers_weekly(tickers))
        text = text + " is doing better. (5 day trend)"

    # DONE
    elif intent == 'CompareStockToday':
        tickers = []

        # is this?
        first = resp['result']['parameters']['FTSE100']
        first = first[:-2]
        tickers.append(first)

        # better than that?
        second = resp['result']['parameters']['FTSE1001']
        second = second[:-2]
        tickers.append(second)

        text = str(util.get_compare_tickers_daily(tickers))
        text = text + " is performing better today. (daily)"

    # DONE
    elif intent == 'CompareStockMonthly':
        tickers = []

        # is this?
        first = resp['result']['parameters']['FTSE100']
        first = first[:-2]
        tickers.append(first)

        # better than that?
        second = resp['result']['parameters']['FTSE1001']
        second = second[:-2]
        tickers.append(second)

        print(first, second, tickers)
        text = str(util.get_compare_tickers_monthly(tickers))
        text = text + " is doing better. (monthly)"

    # DONE
    elif intent == 'BestIndustryTicker':
        industry = resp['result']['parameters']['Sectors']
        text = str(util.get_best_ticker_in_industry(industry))
        text = "The best YTD ticker in industry [" + industry + "] is " + text

    # DONE
    elif intent == 'ShouldInvest':
        text = "No you shouldn't. You should consult a professional instead of a Chatbot, but you can ask me which ticker is the best performing in any industry or get news sentiment!"
    
    # DEFAULT FOR SMALL TALK
    else: 
        text = resp['result']['fulfillment']['speech']

    # IF text is empty, throw exception

    return text