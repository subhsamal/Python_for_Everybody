# Using BeautifulSoup parse HTML page
import urllib.request
import re
#from BeautifulSoup4 import *
from bs4 import BeautifulSoup
url = input("provide the url name to parse")
html_string = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html_string, "html.parser") #soup is object which contains the parsed html page
tags = soup('span') #looks for 'span' tags

sum = 0
my_list = []
my_list1 = []
for tag in tags:
    #print ('Tag:', tag)
    my_list.append(tag.contents[0])
    #print ('TAG.text:', tag.text)
    #for x in re.findall ('[0-9]+', tag.text): retrieving number using regex
        #my_list.append(int(x))

    sum += int(tag.contents[0])   #can directly make sum here
#print (my_list)
#for item in my_list:
    #my_list1.append(int(item))
#for i in my_list1:
    #sum = sum + i
print ('total: ' "%d" % sum)
