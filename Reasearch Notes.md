### Organisational notes
- agile
- get prototype done, get feedback 

### Getting data
- Need API to get the numbers
- Need list of ftse 100 companies
- Need to be able tp parse the numbers correctly to return the correct information

#### APIs and Relevant Info
general info:
- http://www.hl.co.uk/shares/stock-market-summary/ftse-100

APIs:
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
