# choose any public api
# try to get as many different http status codes as you can
# document everything in an .md file so that they can be reproduced
# zip any code and the .md and upload the archive to this channel by 18:45 CET

import requests
import json

# 0. 418 I'm a teapot (april fools joke)
# url = 'https://httpbin.org/status/418'
# response = requests.get(url)
# print(response.status_code)

# 1. 200 OK

# create a header
# headers = {
#     'User-Agent': 'mazsikafan@gmail.com'
# }
# company_tickers = requests.get('https://sec.gov/files/company_tickers.json',headers=headers)
# 
# print(company_tickers.status_code)
# # 2. 404 Not Found
# 
# url = 'https://api.github.com/users/asdasdasdadsdas893429349882394'
# response = requests.get(url)
# print(response.status_code)
# 
# 3. 403 Forbidden

# company_tickers = requests.get('https://sec.gov/files/company_tickers.json')
# print(company_tickers.status_code)

# 4. 401 Unauthorized
# url = 'https://api.github.com/user/emails'
# response = requests.get(url)
# print(response.status_code)
# 

# 5. 502 Bad Gateway # thunder client ????
# url = 'https://httpbin.org/status/502'
# response = requests.get(url)
# print(response.status_code)

# 500? 

# 6. 201 Created with posting
# data = {
#     "name": "Balint",
#     "profession": "analyst"
# }
# response = requests.post('https://jsonplaceholder.typicode.com/posts', data=json.dumps(data))
# print(response.status_code)

# 7. using publicapi
# Status code : 405 Method Not Allowed

# url = 'https://api.publicapis.org/entries'
# response = requests.post(url)
# print(response.status_code)


# 8. 204 No Content
# url = 'https://httpbin.org/status/204'
# response = requests.get(url)
# print(response.status_code)

# 9. 301 Moved Permanently
# url = 'https://httpbin.org/status/301'
# response = requests.get(url)
# print(response.status_code)

# 10. 302 Found
# url = 'https://github.com/settings/profile'
# response = requests.get(url,allow_redirects=False)
# print(response.status_code)


# !!!!!!
# 11. 429 Too Many Requests # DO NOT TRY!!!!!!! YOU WILL GET BANNED
# for i in range(500000):
#     response = requests.get('https://api.publicapis.org/entries')
#     print(response.status_code)
# !!!!!!!!!!!!!!!!!!!!!

# with httpbin it is possible to get almost all status codes



