from bs4 import BeautifulSoup as bs
import requests

url = requests.get('https://en.wikipedia.org/wiki/List_of_highest-grossing_films')
data = url.content

html_data = bs(data,'lxml')

table = html_data.find('table',{'class':"wikitable sortable plainrowheaders"})

rows = table.tbody.find_all('tr')
td_list = list()
name_list = list()
rows.remove(rows[0])
for row in rows:
    try:
        td = row.find_all('td')
        td_list.append(td)
    except:
        pass
    try:
        th = row.find('th')
        name = th.i.text
        name_list.append(name)
    except:
        pass
#Making the csv file
filename = '50_highest_grossing_movies.csv'
f = open(filename,'w')
headers = "Rank,Peak,Title,WorldWide_Gross,Year\n"
f.write(headers)
for i in range (len(name_list)):
    print(td_list[i][0].text.strip()+','
          +td_list[i][1].text.strip()+','
          +name_list[i]+','
          +td_list[i][2].text.strip()+','
          +td_list[i][3].text.strip()
          )
    f.write(td_list[i][0].text.strip()+','
          +td_list[i][1].text.strip()+','
          +name_list[i]+','
          +td_list[i][2].text.strip().replace(',','')+','
          +td_list[i][3].text.strip()+"\n")
f.close()