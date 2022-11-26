import csv
import re

name = input()
with open(name, 'r', encoding='utf-8-sig') as f:
    file_massive = list(csv.reader(f))

table_keys = file_massive[0]
file_massive.pop(0)


def check_massive(massive):
    if len(massive) != len(table_keys): return False
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
        string += row[i]
        string = re.sub(spaces, ' ', string)
        print(table_keys[i] + string)
    print('')


for row in column:
    for i in range(0, len(row) - 1):
        if row[i].find(" ") != -1:
            row[i] = delete_spaces(row[i])
        if row[i].find("\n") != -1:
            row[i] = format_strings(row[i])
    format_conclusion(row)