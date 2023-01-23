import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.markdown('---')
st.header("st.write")
st.subheader("This is the Swiss Army knife of Streamlit commands: it does different things depending on what you throw at it")


st.write('[st.write documentacion] (https://docs.streamlit.io/library/api-reference/write-magic/st.write)')

st.write("Esto es un texto normal")

st.write("""
# esto es un header
y est es _markdown_   **negrita**

""")

df = pd.DataFrame({"col1":[1,2,4],"col2":[33,44,55]})
st.write(df)

y = np.random.normal(2,3,size=1000)
fig, ax = plt.subplots()
ax.hist(y,bins=20)

st.write(fig)


st.markdown('---')
st.header("magic command!!!!")


"Esto es un texto normal mágico"

"""
# esto es un header
y est es _markdown_   **negrita**
pero mágico

"""

df = pd.DataFrame({"col1 magic":[10,20,40],"col2 magic":[33,44,55]})
df

y = np.random.normal(0,6,size=1000)
fig, ax = plt.subplots()
ax.hist(y,bins=20)
ax.set_title("Magic plot")

fig



st.markdown('---')
st.header("st.metric")
st.metric(label="IBEX 35",value="8.416,60",delta ="28.5%")
st.metric(label="Acciona",value="9324",delta ="-0.13%")
st.metric(label="SABADELL",value="4581",delta ="5.5%")

st.markdown('---')
st.header("st.dataframe")


df = pd.DataFrame({"col1":[10,20,40,50],"col2":[33,33,44,55],"col3":[330,440,550,342],"col4":[1033,442,5522,4]})


st.dataframe(df)
st.markdown('---')
st.header("st.table")

st.table(df)


