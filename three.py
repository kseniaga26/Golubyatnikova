import csv
import re

name_keys = {'name': 'Название',
'description': 'Описание',
'key_skills': 'Навыки',
'experience_id': 'Опыт работы',
'premium': 'Премиум-вакансия',
'employer_name': 'Компания',
'salary_from': 'Нижняя граница вилки оклада',
'salary_to': 'Верхняя граница вилки оклада',
'salary_gross': 'Оклад указан до вычета налогов',
'salary_currency': 'Идентификатор валюты оклада',
'area_name': 'Название региона',
'published_at': 'Дата и время публикации вакансии'}

currency = {"AZN": "Манаты",
"BYR": "Белорусские рубли",
"EUR": "Евро",
"GEL": "Грузинский лари",
"KGS": "Киргизский сом",
"KZT": "Тенге",
"RUR": "Рубли",
"UAH": "Гривны",
"USD": "Доллары",
"UZS": "Узбекский сум"}

work_exp = {"noExperience": "Нет опыта",
"between1And3": "От 1 года до 3 лет",
"between3And6": "От 3 до 6 лет",
"moreThan6": "Более 6 лет"}

name = input()
with open(name, 'r', encoding = 'utf-8-sig') as file:
    file_massive = list(csv.reader(file))

key = file_massive[0]
file_massive.pop(0)

def check_massive(massive):
    if len(massive) != len(key): return False
    for i in massive:
        if i == '': return False
    return True

column = []
for i in file_massive:
    if check_massive(i):
        column.append(i)

clean = re.compile('<.*?>')
spaces = re.compile('\s+')

def delete_spaces(string):
    string = re.sub(clean, '', string)
    return string

def format_strings(string):
    return ', '.join(string.split("\n"))

def format_conclusion(row):
    for i in range(0, len(row)):
        string = ': '
        check_name_keys(i, row)
        if key[i][0:6] == "salary":
            row[i] = f"{int(column[row[i]['salary_from']]):,}"
        string += row[i]
        string = re.sub(spaces, ' ', string)
        print(name_keys[key[i]] + string)
    print('')

def check_name_keys(i, row):
    comparison_change(i, row)
    names_change(i, row, currency, 'salary_currency')
    names_change(i, row, work_exp, 'experience_id')
    salary_gross_change(i, row)

def names_change(variable, row, name_keys, name_variable):
    if key[variable] == name_variable:
        row[variable] = name_keys[row[variable]]

def salary_gross_change(i, row):
    if key[i] == 'salary_gross':
        if row[i] == "Trues": row[i] = "С вычетом налогов"
        if row[i] == "Falses": row[i] = "Без вычета налогов"

def comparison_change(variable, string):
    if string[variable] == "True":
        string[variable] = "Да"
    if string[variable] == "False":
        string[variable] = "Нет"

for string in column:
    for i in range(0, len(string) - 1):
        if string[i].find(" ") != -1:
            string[i] = delete_spaces(string[i])
        if string[i].find("\n") != -1:
            string[i] = format_strings(string[i])
    format_conclusion(string)

