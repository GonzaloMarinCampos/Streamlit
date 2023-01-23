import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# st.set_page_config(page_title="EJEMPLO CONTROLES",page_icon="❄️",layout="wide")

st.markdown('---')
st.header("st.checkbox")
estado_del_checkbox = st.checkbox("mi chewckbox", value = True)
if estado_del_checkbox:
    st.write("Check True")

def cambia():
    print("Ha cambiado")
estado_del_checkbox2 = st.checkbox("mi chewckbox2", value = True,on_change=cambia)

def cambia2():
    print(st.session_state.chequeador)
estado_del_checkbox3 = st.checkbox("mi chewckbox3", value = True,on_change=cambia2,key="chequeador")



st.markdown('---')
st.header("st.radio")
salida_radio_button = st.radio("Donde vives?",options=["GERMANY","FRANCE","SPAIN"])
st.write("VIVO EN:",salida_radio_button)


st.markdown('---')
st.header("st.button")
salida_button = st.button("Pulsa AQUI si te atreves",key="mi_primer_boton",help="si se pulsa una vez ya se queda True")
st.write("PULSAR:",salida_button)
st.write(st.session_state.mi_primer_boton)


st.markdown('---')
st.header("st.selectbox")
option = st.selectbox(
     'How would you like to be contacted?',
     ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

st.markdown('---')
st.header("st.multiselect")
options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)


st.markdown('---')
st.header("st.slider")
from datetime import time
appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)


st.markdown('---')
st.header("st.select_slider")
start_color, end_color = st.select_slider(
     'Select a range of color wavelength',
     options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
     value=('red', 'blue'))
st.write('You selected wavelengths between', start_color, 'and', end_color)




picture = st.camera_input("Take a picture")

if picture:
     st.image(picture)