import re
from pprint import pprint
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
corrected_phone_book = [contacts_list.pop(0)]


def get_prepared_name(name: str):
    pattern = re.compile("[А-Я][а-я]+")

    prepared_name = pattern.findall(name)

    if len(prepared_name) < 3:
        for i in range(len(prepared_name), 3):
            prepared_name.append('')

    return prepared_name


for item in contacts_list:
    name = ''
    person = []

    for idx, field in enumerate(item):
        if idx < 3: name += field

        if idx == 3:
            person = get_prepared_name(name)
            corrected_phone_book.append(person)


print(corrected_phone_book)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
# with open("phonebook.csv", "w") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)
