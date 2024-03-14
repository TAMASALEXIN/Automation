# Extract information about the Python programming language
# from its Wikipedia page. Retrieve details such as:

# Year of creation
# Developer(s)
# Latest stable release version and date
# Paradigm(s)
# Typing discipline

# Use the following URL: https://en.wikipedia.org/wiki/Python_(programming_language)

from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")
tbody = doc.tbody
#print(tbody.prettify())


trs = tbody.contents
#print (trs[2].prettify())

paradigm = trs[1].find('td' , {'class': 'infobox-data'}).text
print(paradigm)

designer = trs[2].find('td' , {'class': 'infobox-data'}).text
developer = trs[3].find('td' , {'class': 'infobox-data'}).text
print(f"Designed by: {designer}, Developed by: {developer}")

year = trs[4].find('td' , {'class': 'infobox-data'}).text
print(year)

latest_stable_release = trs[6].find('td' , {'class': 'infobox-data'}).text
print(f"Latest stable release: {latest_stable_release}")

discipline = trs[8].find('td' , {'class': 'infobox-data'}).text
print(discipline)








    


