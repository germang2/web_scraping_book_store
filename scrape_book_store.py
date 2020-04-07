import requests
from bs4 import BeautifulSoup
import time

base_url = base_url = "http://books.toscrape.com/catalogue/category/books/fiction_10/page-{}.html"


for i in range(1, 5):
    r = requests.get(base_url.format(i))
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        # findAll() method returns an iterable
        article_list = soup.findAll(class_='product_pod')
        for article in article_list:
            try:
                title = article.h3.a['title']
                price = article.find(class_='price_color').text
                star_rating = article.p['class'][1]
                print(f"Page{i} - Title: {title} - Price: {price}, - Stars: {star_rating}")
            except Exception as exp:
                print(exp)
        time.sleep(0.5)