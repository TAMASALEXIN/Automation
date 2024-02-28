# This script checks if the HTML structure of a file is valid or not.

from bs4 import BeautifulSoup

with open('c:/Users/atomi/Documents/Automation/movies.html', 'r') as file:
    html_content = file.read()

is_valid = BeautifulSoup(html_content, 'html.parser').find() is not None

if is_valid:
    print("The HTML structure is valid.")
else:
    print("The HTML structure is not valid.")