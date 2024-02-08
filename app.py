import streamlit as st
import pickle
import requests
import pandas as pd
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=1374f55a311b282b5218c6e2ccdd50d4&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path
def recommend(movie):
  movie_index=movies[movies['title']==movie].index[0]
  distances=similarity[movie_index]
  movies_list=sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6] #key to tell to sort on values or itll do on index , start from 1 not 0 as it will be itself
  recommended_movies=[]
  posters=[]
  for i in movies_list:
    #print(i[0])
    movie_id=movies.iloc[i[0]].id
    recommended_movies.append(movies.iloc[i[0]].title)
    posters.append(fetch_poster(movie_id))
  return recommended_movies,posters
st.title("Movie Recommender System")
movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl', 'rb'))
option=st.selectbox(
'One search away from finding your next favorite movie!',movies['title'].values)
if st.button('Discover now:) '):
    recommended_movie_names,recommended_movie_posters = recommend(option)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])