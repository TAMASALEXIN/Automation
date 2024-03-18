# By starting from the main page of IMDb find all films where Brad Pitt
# and Angelina Jolie have played together. You are allowed to use the top
# search bar to find the full filmography for the given actor (this list will be under the Actor > Previous tab).
# With selenium you can use the following code to open a browser and search for the actors:
# from selenium import webdriver

# For validating your result the Collaborations Search site can be used.

# Note that the IMDb search site returns with a wider list as the actual search results.

import requests
from bs4 import BeautifulSoup
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def init_browser():
    driver = webdriver.Chrome()
    driver.get("http://www.imdb.com")
    return driver


def search_actor(driver, actor):
    search = driver.find_element(By.NAME, "q")
    search.send_keys(actor)
    search.submit()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, actor).click()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div/button[1]').click() # Close the pop-up
        time.sleep(2)
    except:
        pass
    try:
        
        see_all_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "See all")))
        see_all_button.click()
    except:
        pass
    return driver.current_url



def get_movies(url):
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



def main():
    driver = init_browser()
    brad_pitt_url = search_actor(driver, "Brad Pitt")
    brad_pitt_movies = get_movies(brad_pitt_url)
    angelina_jolie_url = search_actor(driver, "Angelina Jolie")
    angelina_jolie_movies = get_movies(angelina_jolie_url)
    driver.quit()
    return set(brad_pitt_movies).intersection(angelina_jolie_movies)

if __name__ == "__main__":
    main()

# Output:
# {'Mr. & Mrs. Smith', 'By the Sea'}

