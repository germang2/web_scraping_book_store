import requests
from bs4 import BeautifulSoup

base_url = base_url = "http://books.toscrape.com/catalogue/category/books/fiction_10/page-1.html"

r = requests.get(base_url)

if r.status_code == 200:
    soup = BeautifulSoup(r.text, 'html.parser')
    print(soup.prettify())