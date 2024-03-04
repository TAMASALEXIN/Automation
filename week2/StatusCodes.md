# HTTP Status Codes

This document describes how to reproduce different HTTP status codes using the Python `requests` library.
This might not be the intended task, but this was the only way i could get different 200 and 400 status codes back from th request.

| Status Code | HTTP Method | URL | Description |
|-------------|-------------|-----|-------------|
| 200 | GET | https://httpbin.org/get | Standard response for successful HTTP requests |
| 201 | POST | https://httpbin.org/status/201 | The request has been fulfilled, resulting in the creation of a new resource |
| 202 | PUT | https://httpbin.org/status/202 | The request has been accepted for processing, but the processing has not been completed |
| 203 | GET | https://httpbin.org/status/203 | The server is a transforming proxy that received a 200 OK from its origin |
| 204 | GET | https://httpstat.us/204 | The server successfully processed the request and is not returning any content |
| 400 | POST | https://httpbin.org/status/400 | The server could not understand the request due to invalid syntax |
| 401 | GET | https://httpbin.org/basic-auth/undefined/undefined | The client must authenticate itself to get the requested response, and the authentication is invalid|
| 402 | GET | https://httpbin.org/status/402 | This status code is reserved for future use |
| 403 | GET | https://httpbin.org/status/403 | The client does not have access rights to the content |
| 404 | GET | https://httpbin.org/status/404 | The server can not find the requested resource |
| 405 | DELETE | https://httpbin.org/post | The method specified in the request is not allowed for the resource identified by the request URI |
| 500 | GET | https://httpbin.org/redirect-to | I tried to get a 300 error but the server encountered an unexpected condition occured which lead to the error 500 |