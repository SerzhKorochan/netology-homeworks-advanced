import requests
import re
from bs4 import BeautifulSoup

URL = 'https://habr.com/ru/all/'
INDEX_URL = 'https://habr.com'
KEYWORDS = ['дизайн', 'фото', 'web', 'python']
PATTERN = re.compile(r'|'.join([k + '\\W' for k in KEYWORDS]), re.I)

response = requests.get(URL)

html = BeautifulSoup(response.text, 'html.parser')
articles = html.find_all('article')

for article in articles:
    route = article.find('a', class_='tm-article-snippet__title-link').attrs.get('href').strip()
    article_url = INDEX_URL + route

    response = requests.get(article_url)
    article_page = BeautifulSoup(response.text, 'html.parser')
    article_body = article_page.find('div', class_='tm-article-presenter__body')

    founded_keywords = PATTERN.findall(article_body.text)

    if founded_keywords:
        published_date = article_body.find('span', class_ = 'tm-article-snippet__datetime-published').text
        heading = article_body.find('h1', class_ = 'tm-article-snippet__title_h1').text

        print(f"<{published_date}> -- <{heading}> -- <{article_url}>")
