This contains some python programs to connect to a web server
using socket and urllib. 
The program is written using python 3.4.

In python 3.* print is used as a function rather than a command.
Send and receive requests have to be encoded and decoded.
eg: send.encode(), recv.decode()

URLLIB: urllib is renamed to urllib.request.

BeautifulSoup: There are some changes in Beautifulsoup 4 and python3.
raw_input changed to input
soup = BeautifulSoup(html_string) should be written as soup = BeautifulSoup(html_string, "html.parser")
from BeautifulSoup import * should be from bs4 import BeautifulSoup