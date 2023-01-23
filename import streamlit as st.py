import streamlit as st
import pandas as pd  # pip install pandas openpyxl
import plotly.express as px 

df = pd.read_excel(
    io="db.xlsx",
    engine="openpyxl",
    sheet_name="db (2)",
    skiprows=0,
    usecols="A:K",
    nrows=40)

print(df)