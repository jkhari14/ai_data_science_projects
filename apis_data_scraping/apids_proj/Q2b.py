from bs4 import BeautifulSoup
import requests

url = "https://chicago.craigslist.org/search/zip"
r = requests.get(url).text
soup = BeautifulSoup(r, 'html.parser')
ulArray = soup.body.find('ul', id="search-results").find_all('li')
for li in ulArray:
    print(li.a['href'])