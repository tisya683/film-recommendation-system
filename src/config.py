from dotenv import load_dotenv
import streamlit as st
import os 
from pathlib import Path

load_dotenv()
#api key
TMDB_API_KEY=st.secrets.get("API_KEY",os.getenv("API_KEY")) #streamlit when deployed os when local (quite cooool heheheh)

# file paths

base_directory=Path(__file__).resolve().parent.parent

data_directory=base_directory/"data"
model_directory=base_directory/"models"
image_directory=base_directory/"images"


movies_csv=data_directory/"tmdb_movies_cleaned.csv"
embeddings_file=model_directory/"embeddings.npy"
image=image_directory/"dead_poets_society.jpg"

#url links
BASE_URL = "https://api.themoviedb.org/3"
IMAGE_URL = "https://image.tmdb.org/t/p/w500"