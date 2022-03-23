import requests, json, sys
import time

file1 = open(f'data4{sys.argv[1]}.txt', 'w')
for i in range(1, 13):
    url = f"https://api.nytimes.com/svc/archive/v1/{sys.argv[1]}/{i}.json?api-key=aIlsEi8OYZECkIemqtuYAHFHGAKN3oN0"
    r = requests.get(url).text
    kw_dict = json.loads(r)
    for kwDictList in kw_dict['response']['docs']:
        for bucket in kwDictList:
            if bucket == "keywords":
                for word in kwDictList[bucket]:
                    file1.write(word["value"])
                    file1.write('\n')
    #time.sleep(6)