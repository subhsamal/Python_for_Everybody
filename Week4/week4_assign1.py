from urllib import request
from bs4 import BeautifulSoup

url = "http://python-data.dr-chuck.net/comments_338090.html"

connection = request.urlopen(url)
html = connection.read()

soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
#print (tags)

list = []

for tag in tags:
    list.append(tag.contents[0])

#print (list)

total = 0
for i in range(len(list)):
    total += int(list[i])

print (total)
