# Collect the first 5 quotes (with author) from quotes.toscrape, and store them in a pure text file.

from bs4 import BeautifulSoup
import requests

url = "http://quotes.toscrape.com/"
result = requests.get(url).text

doc = BeautifulSoup(result, "html.parser")

docbody = doc.body
print(docbody.prettify())

for i in range(5):
    quote = doc.find_all("span", class_="text")[i].text
    author = doc.find_all("small", class_="author")[i].text
    with open("quotes.txt", "a") as file:
        file.write(f"{quote} - {author}\n")

print("Done")





