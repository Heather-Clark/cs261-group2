# Software Engineering
## 31/01/18 - Meeting 5

### Minutes

## Requirements Analysis

Glossary 
- Financial data, since we're sending it off to a financial expert. 
Ans: Who else is going to see the data? Tech guys at DB, Jarvis, the stakeholders in the project (Jarvis, DB, US) We own a stake of the pie. Include both technical terms, from programming, but also technical terms. DB won't really know what technical stuff is, Riachrd doesn't know much about stocks. Think about who will be reading the document and make decison on the document. 

Add stakeholders section!

Formatting
- Don't have 1.0, just have 1. 
- Just a stylistic point of view. 

Content 

Can't have IDs has consumer or designer. Seen from customer or designer POV. Better is high level requirements (what consumer will see, versus what designer will see). Good to say what is consumer and what's developer

- Does it have to be explicity said if it's consumer or developer? 
The way some teams have done it is a table, with IDs, requirements, consumer, developer, 
We also missed out priorities, however our keys (C W S) may not be quite enough for priorities. Tables might be preferrable. Table is probably best way to go because it might be less appealling otherwise. 

- Could include things that we aren't doing (like supporting mutliple users
Would be included if it were regularly included in a similar project. There's no point in including if its irrelevant.
Lots of judgement calls on things like these. 

- Should we have a simple state flow?
Yes. 

-Should we have a simple description?
We should have a higher level one in the planning and design. If there's room, high level paragraph detailing what we want. Planning and design is UML and diagrams
We also missed a timeline, which is useful. Latex is good for this. No screenshots in! Screenshots in latex are awful. Overleaf is good for Latex. Has high level graphics editor.



Overall, pretty good. Feel free to move things between planning and deesign.

Mandatory meeting in week 7. Want a meeting beforehand, let him know to book room. If we want to send final versions of RA and PAD, send final version by midday Wednesday. Final point to get things to Richard for readin and feedback. 


## Planning and Design

- Risk Analaysis
Might be better in requirement analysis, because it alters how the program is designed. Subtle jokes are fine (didn't hear from Richard). Can find different risks in different areas. (API goes down? Chatbot doesn't perform as expected?)

- System Architecture
Where we want a flow chart of how each of the different systems will work together. 

- Design
Worth having a considering end of llife cycle. How it is supported in the future, how others can support the code in the future. Since we give the code to DB, they need to know how to suport it. How we'll make it easy for DB to implement, maintain, and extend it if needed. 
List is not NECESSARILY exhaustive. 



We have the right idea, but we have to sort out how it will be done and do it. 



# Questions? 

Jarvis needs to answer an email, if he doesn't reply by Friday. 

- Meaningless statement "Validate using other techniques?"
This is where the developer facing requirements differ wildly. From out end, passing through the API< to the chatbot, etc. User wants to know the information. Can be interpreted different ways. 

- 5 Seconds waiting?
The issue with timings is it is hard to control (especially iwth web based). What if internet goes down? 5 second correspondance fails. Avoiding giving times, or anything you can't reliably say within the project. 

Data should be returned in reasonable amount of time, with with the AIM of returning within 5 seconds. Conscious decision to make it as fast as possible. 

- Words like regularly and often? 
If an actual prject, they might have an issue, but this level they probably won't mind. We can define what we mean by regularily and often. Depends on the case, most of the time it can be inferred but it's up to us. 


Meeting at same time next week (send email)
