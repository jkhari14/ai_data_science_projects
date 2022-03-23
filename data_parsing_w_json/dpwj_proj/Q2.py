from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import numpy as np

class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)

    # for popping an element based on Priority
    def delete(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i][1] > self.queue[max][1]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()


nomination_years = [i for i in range(1952, 2022)]
nomination_years.remove(1957)
nomination_years.remove(1965)
nominated_shows = {}

for i in nomination_years:
    url = f"https://www.emmys.com/awards/nominees-winners/{str(i)}/outstanding-comedy-series"
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'html.parser')
    nominees = soup.body.find('div', id="noms-wrapper-start").next_sibling.find_all('div')[1]
    for ii in range(len(nominees.find_all('div'))):
        if nominees.find_all('div')[ii].find('div'):
            if len(nominees.find_all('div')[ii].find('div').find_all('div')) > 0:
                nominee = nominees.find_all('div')[ii].find('div').find_all('div')[1].text
                if nominee not in nominated_shows:
                    nominated_shows[nominee] = 1
                else:
                    nominated_shows[nominee] += 1

nomination_leader_board = PriorityQueue()
for show in nominated_shows:
    nomination_leader_board.insert((show, nominated_shows[show]))

top6 = []
for i in range(6):
    top6.append(nomination_leader_board.delete())

index = np.arange(6) + 0.3
for i in range(6):
    plt.bar(i+1, top6[i][1], label=top6[i][0], width=0.8, bottom=None, align='center', data=None)

plt.xlabel("Nominated Shows")
plt.ylabel("Number of Nominations")
plt.title("Top 6 Nominated Shows")
plt.legend()
plt.savefig("Q2.pdf")


