from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
republican_votes = []
democratic_votes = []
for i in range(1916, 2021, 4):
    url = f"https://www.archives.gov/electoral-college/"+str(i)
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'html.parser')
    winner = soup.body.find('table').find_all('tr')[0].find('td').text
    runner_up = soup.body.find('table').find_all('tr')[1].find('td').text
    winnerCount = soup.body.find('table').find_all('tr')[2].find_all('td')[0].text
    runnerUpCount = soup.body.find('table').find_all('tr')[2].find_all('td')[1].text
    x = ''
    y = ''
    for ii in range(-3, 0, 1):
        x += winnerCount[ii]
        y += runnerUpCount[ii]
    if '[D]' in winner:
        democratic_votes.append(int(x.replace("*", "")))
        republican_votes.append(int(y.replace("*", "")))
    else:
        democratic_votes.append(int(y.replace("*", "")))
        republican_votes.append(int(x.replace("*", "")))

plt.plot([i for i in range(1916, 2021, 4)], republican_votes, label='Republican Electoral Votes', color='#d62728')
plt.plot([i for i in range(1916, 2021, 4)], democratic_votes, label='Democratic Electoral Votes', color='#1f77b4')
plt.xlabel("Presidential Elections since 1916")
plt.ylabel("Republican vs. Democratic Votes")
plt.title("Daily Positive Cases Trend")
plt.legend()
plt.savefig("Q1.pdf")
