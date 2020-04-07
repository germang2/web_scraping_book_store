import requests
from bs4 import BeautifulSoup

base_url = base_url = "http://books.toscrape.com/catalogue/category/books/fiction_10/page-1.html"

r = requests.get(base_url)

if r.status_code == 200:
    soup = BeautifulSoup(r.text, 'html.parser')
    # findAll() method returns an iterable
    article_list = soup.findAll(class_='product_pod')
    for article in article_list:
        title = article.h3.a['title']
        price = article.find(class_='price_color').text
        star_rating = article.p['class'][1]
        print(f"Title: {title} - Price: {price}, - Stars: {star_rating}")