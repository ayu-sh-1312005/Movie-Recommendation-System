import streamlit as st
import pickle
import pandas
import requests



movies=pickle.load(open(r'movies.pkl','rb'))
similarity=pickle.load(open(r'similarity.pkl','rb'))
movies_list=movies['title']
st.title('Movie Recommendation System')
selected_movie_name=st.selectbox('Search',movies_list)

def fetch_poster(movie_id):
    response=requests.get("https://api.themoviedb.org/3/movie/"+str(movie_id)+"?api_key=da363f844e74b2ba6a7c8defe7e86dff")
    poster_path=response.json()["poster_path"]
    url='https://image.tmdb.org/t/p/original'+poster_path
    return url
    

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distance=similarity[movie_index]
    movies_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0],1])
        recommended_movies_posters.append(fetch_poster(movies.iloc[i[0],0]))
    return recommended_movies,recommended_movies_posters



if st.button('Recommend'):
    movie_name,movie_poster=recommend(selected_movie_name)
    col1,col2,col3,col4,col5= st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])