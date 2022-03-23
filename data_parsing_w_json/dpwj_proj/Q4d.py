import json
import matplotlib.pyplot as plt
from datetime import datetime

with open('tweets_01-08-2021.json', 'r', encoding="UTF-16") as f:
    tweets = json.load(f)

months = {}
for i in range(60+1):
    months[i] = {"Web": 0, "iPhone": 0, "Android": 0}

weekdays = {}
for i in range(7):
    weekdays[i] = 0

hours = {}
for i in range(24):
    hours[i] = 0

for tweet in tweets:
    if int(tweet["date"][0:4]) >= 2016:
        if tweet["isDeleted"] != "f":
            month_string = tweet["date"][0:10]
            current_month = datetime.strptime(month_string, "%Y-%m-%d").month
            current_year = datetime.strptime(month_string, "%Y-%m-%d").year
            month = (current_year - 2016) * 12 + (current_month - 1)
            if "iPhone" in tweet["device"]:
                months[month]["iPhone"] += 1
            if "Android" in tweet["device"]:
                months[month]["Android"] += 1
            if "Web" in tweet["device"]:
                months[month]["Web"] += 1

            weekday_string = tweet["date"][0:10]
            weekday = datetime.strptime(weekday_string, "%Y-%m-%d").weekday()
            weekdays[weekday] += 1

            hour = int(tweet["date"][11:13])
            hours[hour] += 1

# CHARTS
devices = ["Web", "iPhone", "Android"]
ci = 0
color_array = ['#1f77b4', '#ff7f0e', '#2ca02c']
for device in devices:
    deviceTweetsMonthly = []
    for month in months:
        deviceTweetsMonthly.append(months[month][device])
    plt.plot([i for i in range(0, 60+1)], deviceTweetsMonthly, label=device, color=color_array[ci])
    ci += 1
plt.xlabel("Months Since 2016")
plt.ylabel("Number of Tweets")
plt.title("Deleted Monthly Tweets from iPhone vs. Web vs. Android Devices")
plt.legend()
plt.savefig("Q4c-dt.pdf")
plt.clf()


weekday_y_axis = [weekdays[weekday] for weekday in weekdays]
weekday_x_axis = [i for i in range(7)]
plt.hist(x=weekday_x_axis, weights=weekday_y_axis)
plt.xlabel("Weekdays")
plt.ylabel("Number of Tweets")
plt.title("# of Deleted Trump Tweets Made Within Every Weekday since 2016")
plt.savefig("Q4b-dt.pdf")
plt.clf()

hour_y_axis = [hours[hour] for hour in hours]
hour_x_axis = [i for i in range(24)]
plt.hist(x=hour_x_axis, weights=hour_y_axis)
plt.xlabel("Hours of the Day")
plt.ylabel("Number of Tweets")
plt.title("# of Deleted Trump Tweets Made Within Every Hour of the Day since 2016")
plt.savefig("Q4a-dt.pdf")
plt.clf()
