# Using BeautifulSoup parse HTML page
import urllib.request
#from BeautifulSoup4 import *
from bs4 import BeautifulSoup
url = input("provide the url name to parse")
html_string = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html_string, "html.parser") #soup is object which contains the parsed html page
tags = soup('a') #looks for 'a' tags

for tag in tags:
    print (tag.get('href', None))
