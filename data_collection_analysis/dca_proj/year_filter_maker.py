year_filter = ''
for i in range(2000, 2020 + 1):
    if i > 2000:
        year_filter += f"ELSEIF REGEXP_MATCH([Team], '\W*({i})\W*')"
        year_filter += '\n'
        year_filter += f"THEN '{i}'"
        year_filter += '\n'
    else:
        year_filter += f"IF REGEXP_MATCH([Team], '\W*({i})\W*')"
        year_filter += '\n'
        year_filter += f"THEN '{i}'"
        year_filter += '\n'
year_filter += 'END'
print(year_filter)