#!/usr/bin/env python3

import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re  

my_url = "https://twitter.com/realDonaldTrump?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")


tweets = page_soup.findAll("p",{"class":"TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"})
time_stamp = page_soup.find_all("a",{"class":"tweet-timestamp"})


#open file for write
myfile = open("trump-tweets.txt","w")


#Loop through latest tweets with timestamps
i = 0
for tweet in tweets:
	stamp = time_stamp[i]
	print(re.findall(r'[0-9]+\s\w+|\w+\s[0-9]+', stamp.get_text())) 
	i+=1
	print('---------------------------------------------------------------------')
	print(tweet.get_text())
	print('\n')
	myfile.write("Does this work?")
myfile.close()	



#find only clinton tweets 
#Use regex to get rid of "8h8 hours ago" make more readable 
#Save each iteration of loop to file 
#Add clinton funcionality
#Add clock
#Add clock  reset each time he uses diversions with clinton 
