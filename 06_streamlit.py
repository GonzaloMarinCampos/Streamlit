import streamlit as st
import pandas as pd
import datetime
# Importing the StringIO module.
from io import StringIO

# st.set_page_config(page_title="EJEMPLO CONTROLES",page_icon="❄️",layout="wide")

st.markdown('---')
st.header("st.text_input")
title = st.text_input('Movie title', 'Life of Brian')
st.write('*The current movie title is:*', title)

st.markdown('---')
st.header("st.number_input")
number = st.number_input('Insert a number',step=4)
st.write('The current number is ', number)



def kingolnalizador(txt):
    r = list(txt)
    r.reverse()
    return "".join(r)

st.markdown('---')
st.header("st.text_area")
txt = st.text_area('Text to analyze', '''Yo, señora, soy el gigante Caraculiambro, señor de la ínsula Malindrania, a quien venció en singular batalla el jamás como se debe alabado caballero don Quijote de la Mancha, el cual me mandó que me presentase ante vuestra merced, para que la vuestra grandeza disponga de mí a su talante
     ''')
st.write('Sentiment:', kingolnalizador(txt))



st.markdown('---')
st.header("st.date_input")
d = st.date_input(
    "When's your birthday",
    datetime.date(2019, 7, 6),min_value=datetime.date(1970, 1, 1))
st.write('Your birthday is:', d)

st.markdown('---')
st.header("st.time_input")
t = st.time_input('Set an alarm for', datetime.time(8, 45))
st.write('Alarm is set for', t)


st.markdown('---')
st.header("st.file_uploader")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)


st.markdown('---')
st.header("st.color_picker")
color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)