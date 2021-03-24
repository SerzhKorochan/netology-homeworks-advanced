import json


class LinkBuilder:

    def __init__(self, path_to_file: str, default_link: str):
        with open(path_to_file, 'r', encoding='utf-8') as file:
            self.loaded_data = json.load(file)

        self.countries_quantity = len(self.loaded_data)
        self.default_link = default_link
        self.data_to_write = []
        self.counter = 0

    def __generate_link(self, country_name: str):
        country_name = country_name.replace(' ', '_')
        generated_link = self.default_link + country_name

        return generated_link

    def __iter__(self):
        return self

    def __next__(self):
        country_name = self.loaded_data[self.counter]['name']['common']
        link = self.__generate_link(country_name)

        self.data_to_write.append({
            country_name: link
        })

        self.counter += 1

        if self.countries_quantity == self.counter:
            with open('Files/result.json', 'w', encoding='utf-8') as new_file:
                json.dump(self.data_to_write, new_file, indent=4, ensure_ascii=False)

            raise StopIteration
        return self.counter
