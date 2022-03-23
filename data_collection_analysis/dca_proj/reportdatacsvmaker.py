import json
import csv


class Finalist:
    def __init__(self, finalist_id, city, gdp, population, year, sport, champ ):
        self.finalist_id = finalist_id
        self.city = city
        self.gdp = gdp
        self.population = population
        self.year = year
        self.sport = sport
        self.champ = champ


def sport_identifier(sportIdentifierArray, sftDictKey):
    identified_sport = 'No Sport Found'  # debugging tool AND return value
    for s in sportIdentifierArray:
        if s in sftDictKey:
            identified_sport = s
            return identified_sport


def champion(sftDictKey):
    return "Champ" in sftDictKey


def gdp_pop_key_error_check(currentCityDict, year, stat, stat_range):
    ran = 0
    correct_year_found = False
    year_int = int(year)
    year_string = year
    stat_year_offset = 0
    while not correct_year_found:
        try:
            currentCityDict[stat][year_string]
        except KeyError:
            if year_string != "2000":
                year_int -= 1
                stat_year_offset -= 1
                year_string = str(year_int)
            else:
                year_int += 1
                stat_year_offset += 1
                year_string = str(year_int)
            if year_int > 2020 or year_int < 2000:
                raise Exception(f"{stat} for {year} in {currentCityDict} not found")
            ran += 1
            if ran > 2000:
                print(currentCityDict["City"], year, stat)
                return
                # raise Exception("Edge Case Missed")
        else:
            correct_year_found = True
            if stat_range == "20yrPopDiff":
                return currentCityDict[stat][year_string] + currentCityDict[stat_range]*stat_year_offset/20
            elif stat_range == "20yrGDPDiff":
                return currentCityDict[stat][year_string] + currentCityDict[stat_range] * stat_year_offset / 20


sports_identifier_arr = ['NBA', 'NFL', 'MLB', 'NHL', 'MLS', 'CF']
finalists_arr = []
csv_file = open('data2csv3_jjm.csv', 'w', encoding='UTF8')
writer = csv.writer(csv_file)
header = ['Finalist ID', 'City', 'GDP,', 'City Population', 'Year', 'Sport', 'Champion Status']
teamHeader = ['Team', 'Finals Appearances', 'Finals Wins', 'Finals Losses', 'GDP', 'Population', 'Champion Status']
writer.writerow(teamHeader)
with open('data2.json', encoding="utf8") as f:
    city_dict = json.loads(f.read())
finalist_id_incrementer = 0
teams = []
cities = []
for city_i in city_dict:
    cities.append(city_i["City"])
    runner_up_sum = 0
    champ_sum = 0
    sports_dict = city_i["Sports"]
    for ru_c_num in sports_dict:
        if isinstance(sports_dict[ru_c_num], int) and "Runnerup" in ru_c_num:
            runner_up_sum += sports_dict[ru_c_num]
        elif isinstance(sports_dict[ru_c_num], int) and "Champ" in ru_c_num:
            champ_sum += sports_dict[ru_c_num]
    for sport_finalist_type in sports_dict:
        if isinstance(sports_dict[sport_finalist_type], list):
            finalist_years = sports_dict[sport_finalist_type]
            sport_arg = sport_identifier(sports_identifier_arr, sport_finalist_type)
            champ_status_arg = champion(sport_finalist_type)
            for finalist_year in finalist_years:
                print(finalist_id_incrementer, city_i["City"],
                      gdp_pop_key_error_check(city_i, finalist_year, "GDP", "20yrGDPDiff"),
                      gdp_pop_key_error_check(city_i, finalist_year, "Pop", "20yrPopDiff"),
                      finalist_year, sport_arg, champ_status_arg)

                finalist_id_incrementer += 1

                finalist_instance = Finalist(finalist_id_incrementer, city_i["City"],
                                             gdp_pop_key_error_check(city_i, finalist_year, "GDP", "20yrGDPDiff"),
                                             gdp_pop_key_error_check(city_i, finalist_year, "Pop", "20yrPopDiff"),
                                             finalist_year, sport_arg, champ_status_arg)
                team = f'{finalist_instance.city}/{finalist_instance.year}/{finalist_instance.sport}'
                writer.writerow([team, f'{champ_sum + runner_up_sum}', f'{champ_sum}', f'{runner_up_sum}',
                                 f'{gdp_pop_key_error_check(city_i, finalist_year, "GDP", "20yrGDPDiff")}',
                                 f'{gdp_pop_key_error_check(city_i, finalist_year, "Pop", "20yrPopDiff")}',
                                 f'{champ_status_arg}'])
                #finalist_id_incrementer += 1
                finalists_arr.append(finalist_instance)


print(cities)
csv_file.close()



