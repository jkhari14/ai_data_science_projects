import json
import matplotlib.pyplot as plt
from datetime import datetime

with open('tweets_01-08-2021.json', 'r', encoding="UTF-16") as f:
    tweets = json.load(f)
weekdays = {}
for i in range(7):
    weekdays[i] = 0
for tweet in tweets:
    if int(tweet["date"][0:4]) >= 2016:
        weekday_string = tweet["date"][0:10]
        weekday = datetime.strptime(weekday_string, "%Y-%m-%d").weekday()
        weekdays[weekday] += 1

weekday_y_axis = [weekdays[weekday] for weekday in weekdays]
weekday_x_axis = [i for i in range(7)]
plt.hist(x=weekday_x_axis, weights=weekday_y_axis)
plt.xlabel("Weekdays")
plt.ylabel("Number of Tweets")
plt.title("# of Total Trump Tweets Made Within Every Weekday since 2016")
plt.savefig("Q4b.pdf")





