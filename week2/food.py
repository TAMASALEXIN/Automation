import requests

url = "https://api.punkapi.com/v2/beers/1"
response = requests.get(url)
data = response.text
print(data)