from src.config import TMDB_API_KEY
import requests

def get_title(title: str)->dict:
    url="https://api.themoviedb.org/3/search/movie"
    params={
        "api_key":TMDB_API_KEY,
        "query":title}
    response=requests.get(url,params=params)
    response.raise_for_status()
    
    return response.json() #converts json to python dict


def select_movie(title: str):
    results=get_title(title)["results"]
    for i,movie in enumerate(results):
        year=movie.get("release_date",'Unknown')[:4]
        print(f"{i}:{movie["title"]}({year})")
    choice=int(input("select movie no.: "))
    return results[choice]

import requests

def movie_details(movie_id: int):
    url=f"https://api.themoviedb.org/3/movie/{movie_id}"

    params={
        "api_key":TMDB_API_KEY
    }

    response=requests.get(url, params=params)
    response.raise_for_status()

    return response.json()


def get_poster(movie_id: int):
    movie=movie_details(movie_id)

    poster_path=movie.get("poster_path")

    if poster_path is None:
        return None

    return f"https://image.tmdb.org/t/p/w500{poster_path}"