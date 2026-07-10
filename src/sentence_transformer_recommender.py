from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from src.config import movies_csv,embeddings_file
import numpy as np
import pandas as pd
import re

st_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

st_matrix = np.load(embeddings_file)
df=pd.read_csv(movies_csv)


def recommend_new_movie(searched_movie):
    overview=searched_movie.get("overview","") #text preprocessing
    overview=re.sub(r'[^a-zA-Z\s]',"",overview.lower())

              
    query_embedding=st_model.encode([overview])
    
    scores=cosine_similarity(query_embedding,st_matrix)#st_matrix is the embeddings from the cleaned tmdb dataset 
    
    scores=scores.flatten() #frm 2d array to 1d array
    sim_scores=list(enumerate(scores))
    ranked=sorted(sim_scores,key=lambda x:x[1],reverse=True)

    movie_indices=[x[0] for x in ranked]
    similarity_scores = [x[1] for x in ranked]

    #get recommendations 
    recs=df.iloc[movie_indices][["id","title","weighted_rating","original_language","overview"]].copy()

    recs["similarity_score"]=similarity_scores

    top_5_recs=recs[(recs["original_language"]!='en') & (recs["weighted_rating"]>=7.0)].head(5)
    
    return top_5_recs