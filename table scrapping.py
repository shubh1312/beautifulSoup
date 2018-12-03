import pandas as pd
from bs4 import BeautifulSoup as bs
import requests

url = requests.get('https://en.wikipedia.org/wiki/List_of_highest-grossing_films')
data = url.content
data = bs(data,'lxml')

dfs  = pd.read_html('https://en.wikipedia.org/wiki/List_of_highest-grossing_films')
for df in dfs:
    print(df)



#table = data.table
table = data.find('table')
table_row = table.find_all('tr')
for tr in table_row:
    td = tr.find_all('td')
    row = [i for i in td]
    #print(row)

#with pandas it is very easy