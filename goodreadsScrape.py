from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import json

# Set up the Selenium driver
driver = webdriver.Chrome()  # Or use another browser driver like Chrome

# Send HTTP request to the Goodreads book page
url = "https://www.goodreads.com/book/show/4671.To_Kill_a_Mockingbird"
driver.get(url)

# Wait for the genre buttons to be present in the DOM
wait = WebDriverWait(driver, 10)
genre_buttons = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "BookPageMetadataSection__genreButton")))

# Parse the HTML content
soup = BeautifulSoup(driver.page_source, "html.parser")

# Extract the list of genres
genres = [button.text.strip() for button in genre_buttons]

# Write the extracted genre information to a JSON file
data = {"genres": genres}
with open("genres.json", "w") as file:
    json.dump(data, file)

# Close the Selenium driver
driver.quit()