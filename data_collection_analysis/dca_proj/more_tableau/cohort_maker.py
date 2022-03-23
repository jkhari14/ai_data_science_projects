import xlrd
loc = r"C:\Users\13369\Downloads\report1645030093028.xls"
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
cohort_dict = {'No Cohorts': []}
for i in range(1, sheet.nrows):
    if sheet.cell_value(i, 1) == '':
        cohort_dict['No Cohorts'].append(sheet.cell_value(i, 0))
    else:
        if sheet.cell_value(i, 1) != sheet.cell_value(i-1, 1):
            cohort_dict[sheet.cell_value(i, 1)] = []
            cohort_dict[sheet.cell_value(i, 1)].append(sheet.cell_value(i, 0))
        else:
            cohort_dict[sheet.cell_value(i, 1)].append(sheet.cell_value(i, 0))

actual_code = ''

for cohort in cohort_dict:
    for school in cohort_dict[cohort]:
        if cohort != 'No Cohorts':
            if school == cohort_dict[cohort][0]:
                actual_code += f'\n ELSEIF( [school_name] == "{school}"'
            else:
                actual_code += f'\n OR([school_name] == "{school}")'
        else:
            if school == cohort_dict[cohort][0]:
                actual_code += f'\n IF( [school_name] == "{school}" '
            else:
                actual_code += f'\n OR([school_name] == "{school}")'
    actual_code += f'\n ) THEN "{cohort}"'
actual_code += "\n END"

text_file = open("cohort_tableau_code.txt", "wt")
text_file.write(actual_code)  # was: n = text_file.write(actual_code)
text_file.close()
#print(f"{cohort}: {cohort_dict[key]}")

new_code = ''
new_code += 'CASE [school_name]\n'
for cohort in cohort_dict:
    for school in cohort_dict[cohort]:
        new_code += f'WHEN "{school}" \n'
        new_code += f'THEN "{cohort}" \n'
new_code += 'ELSE Null END'

text_file = open("new_cohort_tableau_code.txt", "wt")
text_file.write(new_code)  # was: n = text_file.write(actual_code)
text_file.close()

