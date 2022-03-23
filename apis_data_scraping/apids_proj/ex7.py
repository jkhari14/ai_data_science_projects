import requests, json
from collections import deque
import matplotlib.pyplot as plt
url = 'https://api.covidtracking.com/v1/states/daily.json'
r = requests.get(url).text
covidDB = json.loads(r)
cases_dict = {"NY": [], "IL": [], "TX": [], "NC": [], "CA": []}
days_axis = []
for i in range(371):
    days_axis.append(i)

for dateDict in covidDB:
    if dateDict["date"] == '20200316' and dateDict['state'] == "UT":
        break
    else:
        if dateDict["state"] in cases_dict:
            cases_dict[dateDict["state"]].append(dateDict["positive"])
ci = 0
color_array = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
for state in cases_dict:
    cases_dict[state].reverse()
    plt.plot([i for i in range(0, len(cases_dict[state]))], cases_dict[state], label=state, color=color_array[ci])
    ci += 1

plt.xlabel("Number of Days since 03-16-2020")
plt.ylabel("Cases (millions)")
plt.title("Daily Positive Cases Trend")
plt.legend()
plt.show()



