import os.path
from pprint import pprint
import pandas as pd
import numpy as np
import csv
import re


class AddressBook:

    def __init__(self, address_book_path: str):
        if os.path.exists(address_book_path):
            self.initial_book_df = pd.read_csv(address_book_path)

    def split_column_by_pattern(self, column_name: str, separation_names: list, pattern = r'[А-Я][а-я]+'):
        pattern = re.compile(pattern)
        self.initial_book_df.insert(2, 'tmp', np.nan)
        # for column_name in separation_names:
        #     self.initial_book_df['tpm'] += self.initial_book_df[column_name]

        return True


my_disordered_book = AddressBook('phonebook_raw.csv')
my_disordered_book.split_column_by_pattern('lastname', ['lastname', 'firstname', 'surname'])
pprint(my_disordered_book.initial_book_df)


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
# with open("phonebook.csv", "w") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)

# regex_patterns = {
#         'name': r'[А-Я][а-я]+',
#         'phone_num':
#             r'(\+7|8)(\s+|\s+\(|\(|)([0-9]{3}|[0-9]{3})(\)\s+|\)|-|)([0-9]{3})'
#             r'(-|)([0-9]{2})(-|)([0-9]{2})(((\s+\(|\s+)|)(доб\.\s+[0-9]{4}|)(\)|\s+|))',
#     }