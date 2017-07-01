'''
Created on Jul 1, 2017

@author: Waisum Ton
'''
import urllib2  
from bs4 import BeautifulSoup
import csv  
from datetime import datetime  


# added extra 2 lines in class
from urllib2 import urlparse
from HTMLParser import HTMLParseError

#specify the url
bn_url = "http://www.fly.faa.gov/flyfaa/usmap.jsp"
 
# query the website and return the html to the variable 'page'
page = urllib2.urlopen(bn_url)
 
# parse the html using beautiful soap and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')  
#print soup.body
 
# Take out the <div> of name and get its value
ElmDL = soup.find('dl', attrs={'class':'map', 'id':'usmap'})
#name = name_box.text.strip() # strip() is used to remove starting and trailing  
print ElmDL
print "--------------"
ElmDT = ElmDL.find_all_next('dt')
print len(ElmDT);
ElmDD = ElmDL.find_all('dd')
print len(ElmDD)

for JJ in range(len(ElmDT)):
    lineDT = ElmDT[JJ]
    lineDD = ElmDD[JJ]
    textDD = lineDD.getText()
    lineDTa = lineDT.find('a')
    airport = lineDTa['id']
    # print airport,  textDD
    #offset = lineDT.find("goAirportMap")
    # airport =ElemDT 
    if ('Departure delays are 15 minutes or less' in textDD ):
        print 'NORMAL at', airport 
    else:
        print 'DELAY at', airport  
 