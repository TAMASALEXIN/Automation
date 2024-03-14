#Task 2 - Amazon (Kindle Products)
#Collect all the product names, ratings, and prices from 
#this page: https://www.amazon.com/s?k=kindle

from bs4 import BeautifulSoup
import requests


url = "https://www.amazon.com/s?k=kindle"


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept-Language": "en-US,en;q=0.9"
}

result = requests.get(url, headers=headers).text


doc = BeautifulSoup(result, "html.parser")

# Find all div elements with the class name that contains product names
product_divs = doc.find_all('div', {'class': 'sg-col-inner'})

# find all the product names, rating and price
products = {}

for div in product_divs:
    try:
        name = div.find('span', {'class': 'a-size-medium a-color-base a-text-normal'}).text
        rating = div.find('span', {'class': 'a-icon-alt'}).text
        price = div.find('span', {'class': 'a-price-whole'}).text
        products[name] = {'rating': rating, 'price': price}
    except:
        pass

print(products)





