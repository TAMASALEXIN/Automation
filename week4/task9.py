# Scrape job listings for Python developers on LinkedIn.
# Extract details like job title, company, location, and the date the job was posted.

from bs4 import BeautifulSoup
import requests

url = "https://www.linkedin.com/jobs/search/?keywords=python%20developer&location=Worldwide&trk=public_jobs_jobs-search-bar_search-submit&redirect=false&position=1&pageNum=0"

result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

jobs = doc.find_all("li", class_="result-card")
print(jobs)



