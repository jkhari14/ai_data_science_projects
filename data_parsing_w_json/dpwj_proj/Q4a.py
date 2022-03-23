import json
import matplotlib.pyplot as plt

with open('tweets_01-08-2021.json', 'r', encoding="UTF-16") as f:
    tweets = json.load(f)
hours = {}
for i in range(24):
    hours[i] = 0
for tweet in tweets:
    if int(tweet["date"][0:4]) >= 2016:
        hour = int(tweet["date"][11:13])
        hours[hour] += 1


hour_y_axis = [hours[hour] for hour in hours]
hour_x_axis = [i for i in range(24)]
plt.hist(x=hour_x_axis, weights=hour_y_axis)
plt.xlabel("Hours of the Day")
plt.ylabel("Number of Tweets")
plt.title("# of Total Trump Tweets Made Within Every Hour of the Day since 2016")
plt.savefig("Q4a.pdf")





