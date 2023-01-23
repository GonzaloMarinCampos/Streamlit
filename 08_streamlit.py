import streamlit as st
import numpy as np
import pandas as pd

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [ 37.38283,-5.97317],
    columns=['lat', 'lon'])

st.map(map_data)