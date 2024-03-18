from bs4 import BeautifulSoup
import requests

url = "https://www.imdb.com/name/nm0001401/?ref_=fn_al_nm_1"
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
acc_div = soup.find_all("div", class_='ipc-accordion__item__content_inner accordion-content')
movies = []
for divs in acc_div:
    links = divs.find_all('a' , class_='ipc-metadata-list-summary-item__t')
    for link in links:
        movies.append(link.text)

print(movies)







    










