This is a simple URL shortener application built with Flask and SQLAlchemy.

## Features

- Shorten URL: You can shorten your URL by sending a POST request to the `/shorten` endpoint with the URL in the request body. You can optionally provide a shortcode, if not, one will be generated for you.
- Redirect: You can use the shortened URL to redirect to the original URL by sending a GET request to the `/<shortcode>` endpoint.
- Stats: You can get the stats of a shortcode by sending a GET request to the `/<shortcode>/stats` endpoint. It will return the creation time, last redirect time, and the redirect count.

## Setup

1. Clone the repository.
2. Install the dependencies using pip: `pip install -r requirements.txt`
3. Run the application: `python app.py`

## API

### Shorten URL

**Endpoint:** `/shorten`

**Method:** `POST`

**Data Params:** 

```json
{
    "url": "[valid url]",
    "shortcode": "[optional shortcode]"
}
```

**Success Response:**

- **Code:** 201
- **Content:** `{ "shortcode" : "your_shortcode" }`

### Redirect

**Endpoint:** `/<shortcode>`

**Method:** `GET`

**Success Response:**

- **Code:** 302
- **Content:** Redirects to the original URL.

### Get Stats

**Endpoint:** `/<shortcode>/stats`

**Method:** `GET`

**Success Response:**

- **Code:** 200
- **Content:** 

```json
{
    "created": "creation_time",
    "lastRedirect": "last_redirect_time",
    "redirectCount": "redirect_count"
}
```

## Dependencies

- Flask
- Flask-SQLAlchemy
- Python's built-in datetime, string, random, and os modules.