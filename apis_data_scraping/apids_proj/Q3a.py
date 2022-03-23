import sys
from bs4 import BeautifulSoup
import requests

if sys.argv[1] != '1965' and sys.argv[1] != '1957':
    url = f"https://www.emmys.com/awards/nominees-winners/{sys.argv[1]}/outstanding-comedy-series"
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'html.parser')
    nominees = soup.body.find('div', id="noms-wrapper-start").next_sibling.find_all('div')[1]
    #for nominee in nominees.find_all('div'):
    for i in range(len(nominees.find_all('div'))):
        if nominees.find_all('div')[i].find('div'):
            if len(nominees.find_all('div')[i].find('div').find_all('div')) > 0:
                print(nominees.find_all('div')[i].find('div').find_all('div')[1].text)
else:
    print('Ineligible Year')
