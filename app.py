import streamlit as st
from src.sentence_transformer_recommender import recommend_new_movie
from src.api import get_title,get_poster
from src.config import image


st.markdown('''
<h1 style="color:#FFD1DC;">Foreign Film Recsヾ(⁍̴̆◡⁍̴̆。)ノ✧･ﾟ:</h1>
''', unsafe_allow_html=True)

st.subheader(
    '''instructions: Search for any film in the text box and get 5 similar foreign recommendations '''
)

st.markdown('''
<p style="font-size:22px; color:#FFF5A0;">
by exposing yourself to a film in a different language you are immersing yourself with the culture and gaining a 
whole new perspective on how life is actually lived on the other side of the world
</p>
''', unsafe_allow_html=True)


st.image(image,use_container_width=True)

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
                    st.image(poster,width=400)
                
                st.write(movie["title"])
                st.write(f"{movie["weighted_rating"]:.1f}")
                with st.expander("info"):
                    st.write(movie["overview"])
