# hackerNewsBackend


### Project Background

this project acts as a backend source for news articles and stories pertaining to hacker culture, the project exposes public api's that can be used to fetch data
stored in the database, create new data and also delete data from the db once nescessary condtions are met. 

the project gets it data from **https://hacker-news.firebaseio.com**, which it syncs with every 10 mins and to retrieve data.

### THINGS TO NOTE
1.) the application is hosted on heroku using thier free tier. thier free tier only allows 10,000 rows of data in thier database, once it exceeds 10,000 you
run the risk of losing your data or having service denied to you.  
2.) in order to achieve the specified goal of having the project sync with hackernews every 5 mins, since no particular technology was specified, the author
took advantage of the free heroku scheduler add-on that heroku offers. a custom manage.py command was created and then that command was set to run every 10
mins by the heroku scheduler.  

* The django app is currently hosted at **https://hacker-news-clone-1.herokuapp.com/** *

*Thanks for reading.*
