# Python program to retrive lists of anchor tags from an url.

from urllib import request
from bs4 import BeautifulSoup

url = "http://www.dr-chuck.com"

connection = request.urlopen(url)
text_output = connection.read()     # HTML data

soup = BeautifulSoup(text_output, "html.parser")   #soup is an object. It is the parsed HTML Data.
#print (soup)

tags = soup('a')
#print (tags)

for tag in tags:
    print ("tags:", tag.get('href', None))
    print ("contents:", tag.contents[0])       #prints contents within href tag.
