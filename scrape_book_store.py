import requests
from bs4 import BeautifulSoup
import time

base_url = base_url = "http://books.toscrape.com/catalogue/category/books/fiction_10/page-{}.html"

with open('books_store.csv', 'w', encoding='UTF-8') as books_file:
    headers = 'title;pricel;stars\n'
    books_file.write(headers)

    for i in range(1, 5):
        r = requests.get(base_url.format(i))
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, 'html.parser')
            # findAll() method returns an iterable
            article_list = soup.findAll(class_='product_pod')
            for article in article_list:
                try:
                    title = article.h3.a['title']
                    price = article.find(class_='price_color').text
                    star_rating = article.p['class'][1]
                    data = f'{title};{price};{star_rating}\n'
                    books_file.write(data)
                except Exception as exp:
                    print(f"Exception with page {i}, article: {article.h3.a['title']}")
                    print(exp)
            print(f'data retrieve successfully for page {i}')
            time.sleep(0.5)