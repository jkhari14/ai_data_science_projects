
cities = ['Tuscaloosa', 'Phoenix', 'Los Angeles', 'San Francisco', 'San Diego', 'San Jose', 'Oakland', 'Denver', 'Miami', 'Orlando', 'Tallahassee', 'Atlanta', 'Athens', 'Chicago', 'Indianapolis', 'Louisville', 'New Orleans', 'Baton Rouge', 'Boston', 'Baltimore', 'Detroit', 'Minneapolis', 'St Louis', 'Kansas City', 'Charlotte', 'Newark', 'Las Vegas', 'New York City', 'Buffalo', 'Syracuse', 'Cleveland', 'Cincinnati', 'Columbus', 'Akron', 'Oklahoma City', 'Portland', 'Eugene', 'Providence', 'Nashville', 'Dallas', 'Houston', 'San Antonio', 'Arlington', 'Salt Lake City', 'Seattle', 'Green Bay', 'Milwaukee', 'Montreal', 'Philadelphia', 'Toronto', 'Pittsburgh', 'Washington DC', 'Tampa Bay', 'Edmonton', 'Ottawa', 'Winnipeg', 'Canton', 'Rochester', 'Vancouver', 'Raleigh', 'Tulsa', 'Victoria', 'Calgary', 'Auburn', 'Clemson', 'na']

city_filter = ''
for i in cities:
    if i != 'Tuscaloosa':
        city_filter += f"ELSEIF REGEXP_MATCH([Team], '\W*({i})\W*')"
        city_filter += '\n'
        city_filter += f"THEN '{i}'"
        city_filter += '\n'
    else:
        city_filter += f"IF REGEXP_MATCH([Team], '\W*({i})\W*')"
        city_filter += '\n'
        city_filter += f"THEN '{i}'"
        city_filter += '\n'
city_filter += 'END'
print(city_filter)

