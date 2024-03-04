#choose any public api
#try to get as many different http status codes as you can
#document everything in an .md file so that they can be reproduced
import requests

    

# 200 OK
response = requests.get('https://httpbin.org/get')
print("200 OK: ", response.status_code)

# 201 Created
response = requests.post('https://httpbin.org/status/201', data={"key":"value"})
print("201 Created: ", response.status_code)

# 202 Accepted
response = requests.put('https://httpbin.org/status/202', data={"key":"value"})
print("202 Accepted: ", response.status_code)

# 203 Non-Authoritative Information
response = requests.get('https://httpbin.org/status/203')
print("203 Non-Authoritative Information: ", response.status_code)

# 204 No Content
response = requests.get('https://httpstat.us/204')
print("204 No Content: ", response.status_code)


# 400 Bad Request
# Send a POST request with invalid JSON data to trigger a 400 Bad Request
response = requests.post('https://httpbin.org/status/400', json={"key":"value"})
print("400 Bad Request: ", response.status_code)

# 401 Unauthorized
response = requests.get('https://httpbin.org/basic-auth/undefined/undefined)', auth=('undefined', 'undefined'))
print("401 Unauthorized: ", response.status_code)

# 402 Payment Required
response = requests.get('https://httpbin.org/status/402')
print("402 Payment Required: ", response.status_code)

# 403 Forbidden
response = requests.get('https://httpbin.org/status/403')
print("403 Forbidden: ", response.status_code)


# 404 Not Found
response = requests.get('https://httpbin.org/status/404')
print("404 Not Found: ", response.status_code)

#405 Method Not Allowed

response = requests.delete('https://httpbin.org/post')
print("405 Method not allowed: ", response.status_code)

# 500 Internal Server Error

response = requests.get('https://httpbin.org/redirect-to', allow_redirects=False)
print("500 Internal Server Error: ", response.status_code)