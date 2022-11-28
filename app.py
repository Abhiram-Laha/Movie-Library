import pandas as pd
import pickle
import streamlit as st
import requests
import time

movie_data = pickle.load(open("movie_data.pkl", 'rb'))

m_list = movie_data['Title'].values







st.set_page_config(
    page_title="Movie Library",
    page_icon="🧊"
)






def fetch_details(movie_name):
    response = requests.get("http://www.omdbapi.com/?t={}&apikey=58ded75c".format(movie_name))

    data = response.json()

    title = data['Title']
    year = data['Year']
    rated = data['Rated']
    runtime = data['Runtime']
    genre = data['Genre']
    director = data['Director']
    writer = data['Writer']
    actors = data['Actors']
    plot = data['Plot']
    poster = data['Poster']

    return title, year, rated,runtime, genre, director, writer, actors, plot, poster


st.header("Movie Library")
selected_movie = st.selectbox('Search Movie Details : ', m_list)

if st.button('Search'):
    title, year, rated, runtime, genre, director, writer, actors, plot, poster = fetch_details(selected_movie)

    with st.spinner('Wait for it...'):
        time.sleep(0.5)
    st.success('Done!')


    st.header("")


    st.subheader(title)
    st.write(year,"☉",rated,"☉",runtime)
    st.write("")
    st.write("")

    st.image(poster)
    st.write(genre)
    st.write("")
    st.write(plot)

    st.write("")
    st.write("𝐃𝐢𝐫𝐞𝐜𝐭𝐨𝐫 : ",director)
    st.write("𝐖𝐫𝐢𝐭𝐞𝐫 : ", writer)
    st.write("𝐒𝐭𝐚𝐫𝐬 : ", actors)

    st.header("")

    #st.subheader("Trailer :")

    #st.video("https://www.youtube.com/watch?v=alQlJDRnQkE&t=5s&ab_channel=RottenTomatoesTrailers", format='video/mp4', start_time=0)



hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)








































