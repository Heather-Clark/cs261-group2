# Situation Analysis - Needs Major Cleaning
# Understanding of Specification
## Access and Interface with FTSE 100 Stocks
- Stock Data within 1 minute interval
- Multi-stock support in terms of Sector/Industry
	- Keep in a de facto portfolio as such for extension
	- Keep a list of which stocks in the FTSE 100 are in which sector
- Graphs
- A note on comparison to Indexes such as the FTSE 100 and DOW
	- Actual value is a relative to what it opened as.
	- The calculation for the FTSE Index is Market Cap
	- Market Cap = Closing Price * Number of Shares
		- https://en.wikipedia.org/wiki/Market_capitalization
- Also include comparison against the GBP, Euro, Dollar and Yen.
- Specific Stock Data (try this: https://query1.finance.yahoo.com/v8/finance/chart/GOOG?range=5d&includePrePost=false&interval=1d&corsDomain=finance.yahoo.com&.tsrc=finance)
	- High/Low
	- Change incl %
	- Open/Close
	- Volume i.e. amount traded in a set period of time

## Queries from Users
- Simple user interface to search for exactly what they want, so they don't have to rely on just the language processing module.
- Info on stocks over periods of time.
- Info on groups of stocks.
	- Sector
	- Industry
	- Customized Groups incl. a Portfolio
- Info on major currencies
	- Especially in comparison to the pound
	- Note - a lot of FTSE 100 companies gain revenue overseas, so if the pound is weak, their stock value will shoot up more due to currency conversion.
- News data on companies/industries
	- Use of Yahoo Finance News feed is useful here.
	- Sentiment Analysis - Basically quantitative analysis of public opinion and news surrounding different industries/companies.
- Alpha: Your profit relative to the stock market i.e. you percentage gain compared to the FTSE 100 in our case.

## AI/Chatbot
- Adapt to news
- Predict changes in stocks using trends
	- Also stealing rating data from other sites
- Provide automated notifications at set time periods or when something drastic occurs
- Summary Data/Digest on Stocks
	- Trading Opening
	- Trading Closing
	- Anything drastic happening overnight
- Provide advice for buying, selling and holding
- Language Processing
	- Start with simple, non-compound statements. Basic APIs from Google can deconstruct and select the keywords we need.

# Group Management Decisions

Split the team into specific roles:
- project manger = Heather
- business analysis = Adam
- Financial analysis  = Jay
- lead developer - AI + chat bot = Amber
- quality assurance and testing = Suzy
- web master = Ash

These are more the area where each person will take a lead, as we will be using plan based so the project will be split up.

plan based approach for core specification requirements:
- design
- seek customer feedback
- implementation
- testing
- prototype
- show prototype to customer for feedback
- incorporate feedback

For optional requirements a more agile approach will be taken

Reasons;
- inexperience with software projects
- allow for research time and to become familiar with the technology available
- optional requirements will be started later in the project when group is more familiar with how and what to do
- plan based fits well with giving every member a role
- allows for flexible approach if client modifies specifications of project

Weekly meetings at minimum, further optional meetings later into the project when there are more concrete tasks being allocated, allowing for group work. Allow for more efficient working.
