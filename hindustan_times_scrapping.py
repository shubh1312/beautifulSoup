import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.hindustantimes.com/')
data = r.content

html_data = BeautifulSoup(data,'html.parser')

divisions = html_data.find_all("div",{"class":"news-area newtop-block mb-5 mt-10"})
division = divisions[0].find_all("div")
headings = list()

for div in division:
    try:
        h2 = div.find('h2').text.strip('\n')
        headings.append(h2)
    except:
        h2=None
final = set(headings)
final = list(filter(None,final))

print(*final,sep='\n')