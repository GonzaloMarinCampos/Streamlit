import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.header("Remove Hamburger and Footer")

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

st.markdown('---')
st.header("st.image")
st.image("imagen_ejemplo.jpeg")
st.image("imagen_ejemplo.jpeg",caption="esto es una bonita maripora",width=200)

st.markdown('---')
st.header("st.audio")
st.audio("relax-music-7738.mp3")


st.markdown('---')
st.header("st.video")
st.video("Streamlit.mp4")