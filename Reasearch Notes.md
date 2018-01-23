### Organisational notes
- We need a plan for baseline systems
    - Agile methods can be used at a lower level and for extensions
- Software re-use is key.
- Focus on having working modules
- Interface is very important
- agile
- get prototype done, get feedback

### Guides
- https://chatbotsmagazine.com/creating-a-simple-bot-server-using-python-django-and-django-channels-69fa3b775f2

### Getting data
- Need API to get the numbers
- Need list of ftse 100 companies
- Need to be able tp parse the numbers correctly to return the correct information

#### APIs and Relevant Info
##### general info:
- http://www.hl.co.uk/shares/stock-market-summary/ftse-100
- www.investopedia.com
    - Like an investment-specific Wikipedia

##### APIs:
###### Finance Related
- https://www.quandl.com/tools/api
    - student version available?

- https://www.alphavantage.co/documentation/
    - no FTSE 100
    - nice data
    - key: OZT55085UWDF82LZ
    - slow

- http://www.dxfeed.com/ftse-indices/

- https://support.google.com/docs/answer/3093281?visit_id=1-636512806732941159-2478330061&hl=en-GB&rd=1
    - using Google sheets
    - http://ftse.richardallen.co.uk/ <--- unstable website

- https://developer.yahoo.com/finance/
    - news only
    - need list of ticker symbols of ftse 100 companies

- https://github.com/deanchester/footsie
    - Dean Chester (tutor) python code scrapes data from FTSE 100 feed, shared by Jarvis in forum

- https://arcane-citadel-48781.herokuapp.com
    - RSS feed of FTSE 100 feed (used in Dean Chester's code), updates every 15 minutes

- http://feeds.bbci.co.uk/news/business/rss.xml
- http://feeds.bbci.co.uk/news/uk/rss.xml
- http://www.telegraph.co.uk/business/rss.xml
    - Might be good to also consider more UK-centric feeds

- https://query1.finance.yahoo.com/v8/finance/chart/TSCO.L?range=1d&includePrePost=false&interval=2m&corsDomain=finance.yahoo.com&.tsrc=finance
    - Extracted from Yahoo Finance pages, provides up to date info within 1 minute and very flexible to search ranges, just need to plug in our own options in the ticker part (where it says `TSCO.L`), range and interval.
    - More importantly, provides more information to us than Chester's scrubber, but we need to manually send the requests to yahoo and scrub the data.
    - Shouldn't be too hard as the JSON object arrays of high, low, close and open line up with a returned array of timestamps.
        - These timestamps are in Epoch/Unix Time so it's quite easy to discern when this data was collected.
        
- https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    - Beautiful soup allows nice scrubbing of websites by taking the html doc and storing it in a "Beautiful Soup" object. This object basically nests the strings in a data structure similar to how javascript access nested tags. Should make it easy to find what we need.
 
- https://github.com/deanchester/footsie
    - Scrubs http://www.londonstockexchange.com/ website data for stocks of the FTSE 100.
    - Delayed by 15 minutes consistently.
    - Unclear when the diff/%diff is compartive timewise, probably from when trading opened for the day but unclear.
    - Can use as the base for our own website scrubber (see bs4).

- Yahoo Streamer API
    - https://apimeister.com/2008/12/02/use-yahoo-finance-streaming-api.html
    - https://streamerapi.finance.yahoo.com/streamer/1.0?s=BTC-GBP,CL=F,GBPEUR=X,GBPUSD=X,GC=F,TSCO.L,^DJI,^FCHI,^FTAI,^FTMC,^FTSE,^GDAXI,^GSPC,^HSI,^N225&k=c64,p44,l86,t54,c63,p43,l84,t53&callback=parent.yfs_u1f&mktmcb=parent.yfs_mktmcb&gencallback=parent.yfs_gencb&mu=1&lang=en-GB&region=GB&localize=0
    - More research needed.

###### Language Processing/ChatBot:
- https://cloud.google.com/natural-language/
    - All our language processing needs, testing the API in the window seems to be more optimised for large bodies of text, so maybe use it to analyse news articles to give a gist/summary.

- http://www.nltk.org/
    - Language processing in Python, dream come true.
    - Need to manually analyse the lingustics though, cba.

- https://github.com/gunthercox/ChatterBot
    - Trainable Chatbot AI w/ Deep Learning.
    - Seems a little complex.

- https://www.ibm.com/watson/index.html
    - The Dream
    - Apparently has a free API, needs investigation.
    - Probably most complex.

### Questions
- fairly exhaustive list of financial questions is required to be generated.
- Has to know definitions of trading termonology, more than the average person.
- May need to be programmed to understand "compound" sentences, where more than one thing is asked in one query.
- Understand some questions unrelated to trading, for example asking it to display the result on the screen rather than speak it out.

### AI Learning
- probably should depend only on past queries for predictions rather than data mining, as it's safer and easier to implement.
- proactivity has to be careful, as being bothered about things the chatbox thinks are important but aren't doesn't leave a happy user
- The AI could ask questions from the user to learn if it is on the right track or not, similar to how Siri or Cortana have preferences and settings. https://www.ft.com/content/4f2f97ea-b8ec-11e4-b8e6-00144feab7de
- As asked in one of the bank presentations, should probably keep a list of "favourite" questions so the user doesn't have to ask the same question every day.
- Potentially try and find common industry interests of the user. For example if they are interested in tech companies versus supermarket chains.

### Must haves
- Ability to deal with the data it processes, and present it to the user in an appealing way: voice or visually.
- Interact with user
- Learn from the user

### Could haves
- Look out for a spike in news coverage in areas of interest, as it may indicate something is happening
