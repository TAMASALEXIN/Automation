#Movie Recommendation System:

#Implement a program that uses the OMDB API (http://www.omdbapi.com/) to recommend movies
# based on a user's preferred genre. Prompt the user to input their favorite movie genre 
#and fetch a list of top-rated movies in that genre, displaying details such as title, year, and IMDb rating.

import requests
import json

# Fetch the top-rated movies in a user's preferred genre from the OMDB API
def fetch_movies(genre):
    url = "http://www.omdbapi.com/?s=" + genre + "&type=movie&apikey=4b2f35dc"
    response = requests.get(url)
    data = response.json()
    return data['Search']

# Allow the user to input their favorite movie genre
try:
    genre = input("Enter your favorite movie genre: ")
    if genre == "":
        raise Exception("No genre entered")
    movies = fetch_movies(genre)
    for movie in movies:
        print("Title:", movie['Title'])
        print("Year:", movie['Year'])
        print("IMDb ID:", movie['imdbID'])
        print("\n")
except Exception as error:
    print(error)

# Output:
# Enter your favorite movie genre: action
# Title: Action Jackson
# Year: 1988
# IMDb Rating: tt0094608
#
# Title: Action Point
# Year: 2018
# IMDb Rating: tt6495770
#  
# Title: Action Replayy
# Year: 2010
# IMDb Rating: tt1639426
    