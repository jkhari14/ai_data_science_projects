import requests, json
import time

for year in range(2010, 2020+1):
    file1 = open(f'data4{year}.txt', 'w')
    for i in range(1, 12+1):
        url = f"https://api.nytimes.com/svc/archive/v1/{year}/{i}.json?api-key=aIlsEi8OYZECkIemqtuYAHFHGAKN3oN0"
        r = requests.get(url).text
        kw_dict = json.loads(r)
        time.sleep(10)
        try:
            for kwDictList in kw_dict.get("response").get("docs"):
                for bucket in kwDictList:
                    if bucket == "keywords":
                        for word in kwDictList[bucket]:
                            # print(word['value'])
                            file1.write(word["value"])
                            file1.write('\n')
        except KeyError:
            print(year, i)
    file1.close()
