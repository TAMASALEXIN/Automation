# You can also automatize the validation part. In that case keep only the valid results,
# i.e., where both actor are listed under the Stars keyword according to ex1.py.

import time
from selenium.webdriver.common.by import By
import selenium.webdriver as webdriver
from ex1 import get_movies, search_actor, init_browser

def validate_movie(driver, movie, actors):
    # Search for the movie
    search = driver.find_element(By.NAME, "q")
    search.clear()
    search.send_keys(movie)
    search.submit()
    time.sleep(2)

    # Click on the movie link
    try:
        driver.find_element(By.LINK_TEXT, movie).click()
        time.sleep(2)
    except:
        print(f"Movie {movie} not found.")
        return False

    # Get the stars of the movie
    try:
        stars = driver.find_element(By.XPATH, '//*[@id="title-overview-widget"]/div[3]/div[1]/div[4]/div[1]').text
    except:
        print(f"Could not find stars for movie {movie}.")
        return False

    # Check if both actors are in the stars
    return all(actor in stars for actor in actors)

def main():
    driver = init_browser()
    actors = ["Brad Pitt", "Angelina Jolie"]
    actor_movies = [search_actor(driver, actor) for actor in actors]
    movies_together = set(actor_movies[0]).intersection(actor_movies[1])

    valid_movies = [movie for movie in movies_together if validate_movie(driver, movie, actors)]
    print(valid_movies)

    driver.quit()

if __name__ == "__main__":
    main()

# The output is:
# {'The Green Mile', 'The Terminal', 'Cast Away'}

