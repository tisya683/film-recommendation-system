import streamlit as st
from src.sentence_transformer_recommender import recommend_new_movie
from src.api import get_title,get_poster


st.title(":pink[Foreign Film Recs ヾ(⁍̴̆◡⁍̴̆。)ノ✧･ﾟ:]")

st.write(
    '''instructions: Search for any film in the text box and get 5 similar foreign recommendations '''
)

st.markdown('''by exposing yourself to a film in a different language you are immersing yourself with the culture and gain a 
                whole new perspective on how life is actually lived on the other side of the world''')


movie_name=st.text_input("movie title")



def select_movie(title: str)->dict: #dropdown for users to choose
    results=get_title(title)["results"]

    if not results:
        st.warning("No movies found")
        return None
    
    options=[]

    for movie in results:
        year=movie.get("release_date",'Unknown')[:4]
        options.append(f"{movie["title"]}({year})")


    selected=st.selectbox("select the correct movie",options)
    
    return results[options.index(selected)] # reuturns entire movie dict of selected movie 

if movie_name:
    selected_movie=select_movie(movie_name)

    if selected_movie:
        recs=recommend_new_movie(selected_movie)

        cols=st.columns(len(recs)) #list of columns

        for col,(_,movie)in zip(cols,recs.iterrows()):
        
            with col: # everything inside must be displayed in each streamlit col
                poster=get_poster(movie["id"])
                if poster:
                    st.image(poster,width=200)
                
                st.write(movie["title"])
                st.write(f"{movie["weighted_rating"]:.1f}")