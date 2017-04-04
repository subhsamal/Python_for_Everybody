from urllib import request
from bs4 import BeautifulSoup

url = "http://python-data.dr-chuck.net/known_by_Sanaa.html"

position =int(input ("enter position"))
count = int(input ("enter count"))

for i in range(count):

    connection = request.urlopen(url)
    html = connection.read()

    soup = BeautifulSoup(html, "html.parser")
#print (soup)

    tags = soup('a')
#print (tags)



    url = (tags[position -1].get("href",None))

print (tags[position -1])
