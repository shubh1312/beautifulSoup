from bs4 import BeautifulSoup
import requests

r = requests.get('http://pythonhow.com/example.html')
c = r.content

soup = BeautifulSoup(c,'html.parser')

#print(soup.prettify())
#to display the html content in a arranged way

#extracting the code inside the div section
all = soup.find_all("div",{"class":"cities"})
# print(all)
city = list()
for heading in all:
    city.append(heading.find('h2').text)

print(city)