import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

def scrape_books(url, counter):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('article', class_='product_pod')

    for book in books:
        title = book.find('h3').find('a').get('title')
        words = re.findall(r'\w+', title.lower())  
        counter.update(words) 
        prices = book.find('p', class_='price_color').text
        

    next = soup.find('li', class_='next')
    if next:
        next_url = next.find('a').get('href')
        base_url = 'https://books.toscrape.com/catalogue/'
        scrape_books(base_url + next_url, counter)

counter = Counter()
scrape_books('https://books.toscrape.com/catalogue/page-1.html', counter)

for word, count in counter.most_common(10):
    print(f'{word}: {count}')