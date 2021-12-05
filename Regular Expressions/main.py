import os.path
import pandas as pd
import numpy as np
import re


class AddressBook:

    def __init__(self, address_book_path: str):
        if os.path.exists(address_book_path):
            self.initial_book_df = pd.read_csv(address_book_path)
            self.normalized_book_df = pd.DataFrame(columns=self.initial_book_df.columns.values)

    def __split_column_by_pattern(self, column_name: str, separation_names: list, pattern: str):
        pattern = re.compile(pattern)
        self.initial_book_df['tmp'] = ''

        for column_name in separation_names:
            self.initial_book_df['tmp'] += self.initial_book_df[column_name].astype(str)

        for idx, row in self.initial_book_df.iterrows():
            parts_of_column = pattern.findall(row['tmp'])

            for i in range(len(parts_of_column), len(separation_names)):
                parts_of_column.append(np.nan)

            for k in range(0, len(separation_names)):
                row[separation_names[k]] = parts_of_column[k]

        self.initial_book_df = self.initial_book_df.drop(columns=['tmp'])

        return True

    def __replace_values_by_pattern(self, column_name: str, pattern: str, repl: str):
        self.initial_book_df[column_name].replace(pattern, repl, inplace=True, regex=True)

    def __union_duplicates(self, keys: list):
        grouped_df = self.initial_book_df.groupby(keys)

        for name, frame in grouped_df:
            united_frame = frame

            if len(frame) > 1:
                united_frame = frame.iloc[0].combine_first(frame.iloc[1])

            self.normalized_book_df = self.normalized_book_df.append(united_frame.loc[:], ignore_index=True)

    def normalize(self):
        # normalize full name
        self.__split_column_by_pattern('lastname', ['lastname', 'firstname', 'surname'], r'[А-Я][а-я]+')

        # normalize phone
        self.__replace_values_by_pattern('phone',
                                         r'(\+7|8)(\s+|\s+\(|\(|)([0-9]{3}|[0-9]{3})(\)\s+|\)|-|)([0-9]{3})'
                                         r'(-|)([0-9]{2})(-|)([0-9]{2})(((\s+\(|\s+)|)(доб\.\s+[0-9]{4}|)(\)|\s+|))',
                                         r'\1(\3)\5-\7-\9\13')

        # union duplicates
        self.__union_duplicates(['lastname', 'firstname'])

        return self.normalized_book_df

    @staticmethod
    def save_book(book, name: str):
        book.to_csv(f'{name}.csv', index=False)


my_disordered_book = AddressBook('phonebook_raw.csv')
my_disordered_book.save_book(my_disordered_book.normalize(), 'normalized_book')
