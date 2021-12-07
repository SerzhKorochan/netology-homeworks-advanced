import requests
from bs4 import BeautifulSoup

URL = 'https://habr.com/ru/all/'

KEYWORDS = {'дизайн', 'фото', 'web', 'python'}

response = requests.get(URL)

html = BeautifulSoup(response.text, 'html.parser')
articles = html.find_all('article')
index_url = 'https://habr.com'

for article in articles:
    route = article.find('a', class_='tm-article-snippet__title-link').attrs.get('href').strip()
    article_url = index_url + route

    print(article_url)
