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
from selenium.webdriver.common.keys import Keys

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
    return driver.current_url




def get_movies(driver, url):
    movies = []

    try :
        previous_movies = driver.find_element(By.XPATH, '//*[@id="actor-previous-projects"]/div[1]/label')
        previous_movies.send_keys(Keys.ENTER)
    except:
        pass
    time.sleep(2)

    try :
        see_all = driver.find_element(By.XPATH, '//*[@id="accordion-item-actress-previous-projects"]/div/div/span/button')
        see_all.send_keys(Keys.ENTER)
    except:
        pass
    time.sleep(2)

    try:
        all_title = driver.find_elements(By.XPATH, "//*[@id='accordion-item-actor-previous-projects']/div/ul/li/div[2]/div[1]/a")
        time.sleep(2)
        for title in all_title:
            movies.append(title.text)
    except:
        pass

    try:
        all_title = driver.find_elements(By.XPATH, '//*[@id="accordion-item-actress-previous-projects"]/div/ul/li/div[2]/div[1]/a')
        time.sleep(2)
        for title in all_title:
            movies.append(title.text)
    except:
        pass

    return movies



def main():
    driver = init_browser()
    brad_pitt_url = search_actor(driver, "Brad Pitt")
    brad_pitt_movies = get_movies(driver,brad_pitt_url)
    angelina_jolie_url = search_actor(driver, "Angelina Jolie")
    angelina_jolie_movies = get_movies(driver, angelina_jolie_url)
    driver.quit()
    movies_together = set(brad_pitt_movies).intersection(angelina_jolie_movies)
    print(movies_together)

if __name__ == "__main__":
    main()

# Output:
# {'Mr. & Mrs. Smith', 'By the Sea'}


