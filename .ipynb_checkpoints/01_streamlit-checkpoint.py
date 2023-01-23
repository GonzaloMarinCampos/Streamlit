import streamlit as st
import pandas as pd

st.title("st.title")
st.subheader("st.subheader")
st.header("st.header")
st.text("st.text")


st.markdown('---')
st.header("st.caption")
st.caption("para incluir un subtítulo se usa st.caption")
st.markdown('---')

st.markdown('---')
st.header("st.markdown")
st.markdown("se usa st.markdown para poder escribir **negrita** *cursiva* ")
st.markdown("# esto es como H1 en html")
st.markdown("## esto es como H2 en html")
st.markdown("### esto es como H3 en html")
st.markdown("#### esto es como H4 en html")
st.markdown("##### esto es como H5 en html")
st.markdown("###### esto es como H6 en html")
st.markdown('[chuleta markdown] (https://www.markdownguide.org/cheat-sheet/)')

st.markdown('---')

st.markdown('---')
st.header("st.latex")
st.latex(r"\frac{1}{\sqrt{x}}")  # recorda usar raw text
st.markdown('[referencia latex] (https://katex.org/docs/supported.html)')
st.latex(r"\chi")
st.markdown('---')

st.markdown('---')
st.header("st.json")
json = {"clave a":"valor de a","b":[1,2,3]}
st.json(json)
st.markdown('---')


st.markdown('---')
st.header("st.code")
codigo = """
#include <stdio.h>

int main() {
  int i;
  for (i = 0; i < 5; i++) {
    printf("%d\n", i);
  }
  return 0;}
"""
st.code(codigo,language="c")
st.markdown('---')

st.markdown('---')
st.header("st.write")
st.subheader("This is the Swiss Army knife of Streamlit commands: it does different things depending on what you throw at it")

st.write("## H2")
st.write('[st.write documentacion] (https://docs.streamlit.io/library/api-reference/write-magic/st.write)')
