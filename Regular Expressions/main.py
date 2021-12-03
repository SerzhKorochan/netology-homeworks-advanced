import re
from pprint import pprint
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# corrected_phone_book = [contacts_list.pop(0)]


class AddressBook:
    regex_patterns = {
        'name': r'[А-Я][а-я]+',
        'phone_num':
            r'(\+7|8)(\s+|\s+\(|\(|)([0-9]{3}|[0-9]{3})(\)\s+|\)|-|)([0-9]{3})'
            r'(-|)([0-9]{2})(-|)([0-9]{2})(((\s+\(|\s+)|)(доб\.\s+[0-9]{4}|)(\)|\s+|))',
    }

    def __init__(self, address_book: list):
        self.address_book = address_book
        self.regex_patterns_obj = {}
        self.revised_book = []
        self.book_fields = address_book.pop(0)

        self.revised_book.append(self.book_fields)

        for key, value in self.regex_patterns.items():
            self.regex_patterns_obj[key] = re.compile(value)

    def __get_full_name_by_pattern(self, full_name: str):
        quantity_of_names = 3
        parts_of_full_name = self.regex_patterns_obj['name'].findall(full_name)

        for i in range(len(parts_of_full_name), quantity_of_names):
            parts_of_full_name.append('')

        return parts_of_full_name

    def __get_phone_number_by_pattern(self, phone_number: str):
        layout_for_main_phone = r'\1(\3)\5-\7-\9\13'

        return self.regex_patterns_obj['phone_num'].sub(layout_for_main_phone, phone_number)

    def revise(self):
        for note in self.address_book:
            full_name = ''
            person = []

            if len(note) <= len(self.book_fields):
                for idx, info in enumerate(note):
                    field_name = self.book_fields[idx]

                    if field_name == 'lastname' or field_name == 'firstname':
                        full_name += info
                    elif field_name == 'surname':
                        person = self.__get_full_name_by_pattern(full_name)
                    elif field_name == 'phone':
                        person.append(self.__get_phone_number_by_pattern(info))
                    else:
                        person.append(info)

                self.revised_book.append(person)

    def get_revised_book(self):
        return self.revised_book

my_disordered_book = AddressBook(contacts_list)
my_disordered_book.revise()
pprint(my_disordered_book.get_revised_book())
a =1
b = 2

#
# def get_prepared_name(name: str):
#     pattern = re.compile("[А-Я][а-я]+")
#
#     prepared_name = pattern.findall(name)
#
#     if len(prepared_name) < 3:
#         for i in range(len(prepared_name), 3):
#             prepared_name.append('')
#
#     return prepared_name


# def get_num_by_layout(main_phone_num: str):
#     pattern = re.compile(r'(\+7|8)(\s+|\s+\(|\(|)([0-9]{3}|[0-9]{3})(\)\s+|\)|-|)([0-9]{3})(-|)([0-9]{2})(-|)([0-9]{2})')
#
#     layout = r"\1(\3)\5-\7-\9"
#
#     result = pattern.sub(layout, main_phone_num)
#
#     print(result)
#
#
# for item in contacts_list:
#     name = ''
#     person = []
#     phone_num = ''
#
#     for idx, field in enumerate(item):
#         if idx < 3: name += field
#
#         if idx == 3:
#             person = get_prepared_name(name)
#             corrected_phone_book.append(person)
#
#         if idx == 5:
#             phone_num += field
#             get_num_by_layout(phone_num)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
# with open("phonebook.csv", "w") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)
