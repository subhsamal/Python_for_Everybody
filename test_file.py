form urllib import request

goog_url = "http://chart.finance.yahoo.com/table.csv?s=GOOG&a=2&b=3&c=2017&d=3&e=3&f=2017&g=d&ignore=.csv"

def download_stock_data(csv_url):
    response = request.urlopen(csv_url) #stores the connection in response
    csv = response.read()   #
    csv_str = str(csv)  # csv data converted to string

    lines = csv_str.split("\\n") #breaks the string at new line
    dest_url = r'goog.csv'
