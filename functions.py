from dotenv import load_dotenv
from urllib.parse import quote
import os
import requests

load_dotenv()

def search(movie_name):
    api_key = os.getenv("TMDB_API_KEY")
    if not api_key:
        raise Exception("Error: The TMDB_API_KEY environment variable is not set.")
    
    movie_name_encoded = quote(movie_name)
    base_url = "https://api.themoviedb.org/3/search/movie"
    full_url = f"{base_url}?api_key={api_key}&query={movie_name_encoded}"
    
    # Send GET request to TMDB and store the response in a variable
    response = requests.get(full_url)

    # Parse the response as JSON
    data = response.json()

    results = data.get("results", [])
    if not results:
        print("No results found")

    for movie in results:
        title = movie.get("title", "No title")
        release_date = movie.get("release_date", "N/A")
        print(f"{title} ({release_date})")