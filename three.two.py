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
        comparison_change(i, row)
        string += row[i]
        string = re.sub(spaces, ' ', string)
        print(name_keys[key[i]] + string)
    print('')

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
    # vacancies.csv