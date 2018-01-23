# Software Engineering
## 15:00 - 16:00, 23/01/18 - Meeting 3
### Agenda
- set production goals
- plan for software
- reports
    - write requirements
    - work out sections
    - split up who is doing what sections
    - start drafting
- future
    - next meeting
    - week 4 meeting with Richard

### Minutes
- requirements - end of week
- 31st draft requirements analysis

#### Functional Requirements
Data collection
- FTSE 100: scrape tickers symbols
- separate tickers into industry
- News: yahoo, more sources

Chatbot
- interface-able: typed input, could have: voice input
- response: cope with any input, including error

AI and data analysis
- User information
- sentiment analysis: google natural language processor
- could have: graphs (is visual representation of data wanted?)
- link trends, industries and news stories to stocks

Q: How much analysis should AI? Should it just be an assistant or should it telling them how to do there job?

#### Non-Functional Requirements
UI
- favourites, customisable: preset
- ability to add portfolio, multiple portfolio - need a data structure - like file system - could have

Q: how do db track or store portfolios? if so how?

keep track of volume (amount of stocks sold)

- responsive: pipelining, quick data get it out fast, analysis happen in the background
- small UI: screen space required - web based for responsive design
- support for phones and pc
- help menus, labels - intuitive chatbot

Q: security - do we need to mention this in the reports?

- performance: internet connection
- error handling
