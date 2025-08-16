from dotenv import load_dotenv
from urllib.parse import quote
import os
import requests

load_dotenv()

def fetch_data_and_print(base_url, url_extension=""):
    api_key = os.getenv("TMDB_API_KEY")
    if not api_key:
        raise Exception("Error: The TMDB_API_KEY environment variable is not set.")
    
    full_url = f"{base_url}?api_key={api_key}" + url_extension

    response = requests.get(full_url)
    if response.status_code != 200:
        print("Error fetching movies: ", response.status_code)
        return

    data = response.json()
    results = data.get("results", [])
    if not results:
        print("No results found")
        return
    
    for movie in results:
        title = movie.get("title", "No title")
        release_date = movie.get("release_date", "N/A")
        print(f"{title} ({release_date})")

def search(movie_name):
    movie_name_encoded = quote(movie_name)
    base_url = "https://api.themoviedb.org/3/search/movie"
    url_extension = f"&query={movie_name_encoded}"
    fetch_data_and_print(base_url, url_extension)
    


def now_playing():    
    base_url = "https://api.themoviedb.org/3/movie/now_playing"
    fetch_data_and_print(base_url)


def popular_movies():
    base_url = "https://api.themoviedb.org/3/movie/popular"
    fetch_data_and_print(base_url)


def top_rated_movies():
    base_url = "https://api.themoviedb.org/3/movie/top_rated"
    fetch_data_and_print(base_url)

def upcoming_movies():
    base_url = "https://api.themoviedb.org/3/movie/upcoming"
    fetch_data_and_print(base_url)