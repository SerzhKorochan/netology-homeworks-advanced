import csv
import numpy as np
import address_book

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

for idx, row in enumerate(contacts_list):
    contacts_list[idx] = [np.nan if val == '' else val for val in row]

my_disordered_book = address_book.AddressBook(contacts_list)
normalized_list = my_disordered_book.get_normalized_list()

with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(normalized_list)

