from src.config import TMDB_API_KEY,BASE_URL,IMAGE_URL
import requests

def get_title(title: str)->dict:
    url=f"{BASE_URL}/search/movie"
    params={
        "api_key":TMDB_API_KEY,
        "query":title}
    response=requests.get(url,params=params)
    response.raise_for_status()
    
    return response.json() #converts json to python dict


def select_movie(title: str)->dict: #dropdown for users to choose
    results=get_title(title)["results"]

    if not results:
        print("No movie found")
        return None
    
    for i,movie in enumerate(results):
        year=movie.get("release_date",'Unknown')[:4]
        print(f"{i}:{movie["title"]}({year})")
    choice=int(input("select movie no.: "))

    if choice < 0 or choice >= len(results):
        raise ValueError("Invalid movie selection")
    
    return results[choice]


def movie_details(movie_id: int)->dict:
    url=f"{BASE_URL}/movie/{movie_id}"

    params={
        "api_key":TMDB_API_KEY
    }

    response=requests.get(url, params=params)
    response.raise_for_status()

    return response.json()


def get_poster(movie_id: int)->str|None:
    movie=movie_details(movie_id)

    poster_path=movie.get("poster_path")

    if poster_path is None:
        return None

    return f"{IMAGE_URL}{poster_path}"