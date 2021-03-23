import iterator as itr


if __name__ == '__main__':
    wiki_link = 'https://en.wikipedia.org/wiki/'
    path_to_countries_data = 'Files/countries.json'

    linkbuilder = itr.LinkBuilder(path_to_countries_data, wiki_link)

    for item in linkbuilder:
        pass
