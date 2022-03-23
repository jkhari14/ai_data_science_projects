from bs4 import BeautifulSoup
import requests


url = "https://www.emmys.com/shows/cheers"
r = requests.get(url).text
soup = BeautifulSoup(r, 'html.parser')
years = soup.body.find('section', id="awards").find_all('div')[2].find_all('div')
yearOfDate = '1993'
award_print_arr = []
award_num_arr = []
for83int = 0
for83print = ''
awards = 0
for year in years:
    if year.find('a') and '-' in year.find('a').text:
        #print(year.find('a').text)
        if year.find('a').text[-4:-1]+year.find('a').text[-1] == yearOfDate:
            awards += 1
            for83int = awards
        else:
            #print(yearOfDate + " " + str(int(awards/4)))
            award_print_arr.append(yearOfDate)
            award_num_arr.append(int(awards/4))
            changeDate = int(yearOfDate) - 1
            yearOfDate = str(changeDate)
            for83print = yearOfDate
            awards = 1
            for83int = 1

award_print_arr.append(for83print)
award_num_arr.append(int(for83int/4))

for i in range(len(award_num_arr)-1, -1, -1):
    print(award_print_arr[i] + " " + str(award_num_arr[i]))

