import sys
from bs4 import BeautifulSoup
import requests

url = f"https://www.archives.gov/electoral-college/"+sys.argv[1]
r = requests.get(url).text
soup = BeautifulSoup(r, 'html.parser')
winner = soup.body.find('table').find_all('tr')[0].find('td').text
runner_up = soup.body.find('table').find_all('tr')[1].find('td').text
winnerCount = soup.body.find('table').find_all('tr')[2].find_all('td')[0].text
runnerUpCount = soup.body.find('table').find_all('tr')[2].find_all('td')[1].text
x = ''
y = ''
for i in range(-3, 0, 1):
    x += winnerCount[i]
    y += runnerUpCount[i]
print(f"{winner}: {x}")
print(f"{runner_up}: {y}")
