work in progress....
click for app: https://foreign-film-recs.streamlit.app/

So most film recommendation systems don’t explicitly provide foreign film recommendations which makes it harder for people to discover and appreciate international cinema. As someone who loves international films, I hoped that by building a recommendation system solely giving foreign film recommendations it allows cinema goers who are interested in this niche or just the curious to discover similar storytelling elements  explored in a different culture and setting. Hence this project aims to recommend foreign films that share similar themes, genres, or storytelling elements with well-known English-language movies.

This project allows 

before we start these are my own top foreign film recs <3 
* Anatomy of a Fall (2023)
* Potrait of a Lady on Fire (2019)
* Jab We Met (2007)
* Yi Yi (2000)
* Chungking Express (1994)


## Table of Contents
- Overview of Project
- Dataset Used
- Installation
- How to Use
- Overview of Project
- Areas for Improvement
- Tech Stack

## Overview of Project

'''mermaid
flowchart TD
      A([ User enters movie title])
      B([Search TMDB API])
      C([Retrieve title + overview])
      D([Sentence Transformer encodes overview])
      E([Compare embedding with your precomputed movie embeddings])
      F([Cosine Similarity])
      G([Return the top 5 most similar movies + overview +])

A-->B
B-->C
C-->D
D-->E
E-->F
F-->G
'''

My aim was to build a content based recommendation system. In the experimentation phase to determine which nlp model to use, I started out testing the TF-IDF model to capture the meaning of the movie overview. After which I used cosine similarity on the embeddings to derive the similarity score. Movies witht he top 5 highest similarity scores were returned as the top recommendations . 
However after a few test cases, I noticed that the recommendations just happened to have the same overlapping words in the overview and did not capture semantic similarity  of the overview.

Hence my options were to use a neural network like word2vec or a transformer transfer learning model like Sentence Transformers. However word2vec doesnt capture the semantic context of the entire overview but for the individual words in the overview unlike sentence transformers. Hence I went ahead with sentence transformers and likewise used cosine similairyt to generate the similarity scores and give me the top 5 recommendations. From the test cases the movie recommendations usign sentence transformers aligned more with the themes and storyline of the searched movie.

I then saved the dataframe with the sentence transformer embedding. Afterwhich I created the logic for allowing users to search for any movie using the tmdb api and then using the transformer model to embed its overview and use cosine similarity to compare with the embeddings in the database. The recommendations are then filtered to only show films that are not in english and have a weighted rating>7.0
Again I use the TMDB api to return the posters for the recommended films and the oveviews are returned from the databse. 





