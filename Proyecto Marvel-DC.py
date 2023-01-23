from curses.ascii import alt
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objs as go

st.set_page_config(page_title="Comparación Peliculas Marvel-DC",
                page_icon= "alien:",
                layout="wide")
st.header(":alien:¿Cuál será la mejor compañía?")
st.header("Date un gusto escuchando esto")
st.audio("Avengers Infinity war.mp3")
st.image("marvel-dc.jpeg")

st.header("Comparación Peliculas Marvel-DC (Opción de Filtrar en la esquina superior izquierda)")



#Carga de datos
df_db = pd.read_excel(r'db.xls')

# ---- SIDEBAR ----
st.sidebar.header("Filtra aquí:")
company = st.sidebar.multiselect(
    "Selecciona la Compañía:",
    options=df_db["Company"].unique(),
    default=df_db["Company"].unique()
)

valoracion = st.sidebar.multiselect(
    "Selecciona la Valoración:",
    options=df_db["Rate"].unique(),
    default=df_db["Rate"].unique(),
)

lanzamiento = st.sidebar.multiselect(
    "Selecciona el año de lanzamiento:",
    options=df_db["Release"].unique(),
    default=df_db["Release"].unique()
)
Oscars = st.sidebar.multiselect(
    "Nº de Oscars:",
    options=df_db["Oscar"].unique(),
    default=df_db["Oscar"].unique()
)
df_selection = df_db.query(
    "Company == @company & Rate ==@valoracion & Release == @lanzamiento & Oscar == @Oscars")

col5,col6 = st.columns(2)

with col5:
    st.dataframe(df_selection)
with col6:
    st.markdown("![Alt Text](https://i.imgur.com/bTb5UHQ.gif)")


st.markdown('---')
st.image("dcvs.jpeg")


data = [go.Box(x=df_db["Company"],y=df_db["Rate"])] #pointpos=0 para ubicación de los puntos en el centro / boxpoints ="all" si se quieren visualizar todos los puntos

#Definición de objeto "layout": diseño del gráfico como título, nombres de ejes,...
layout = go.Layout(title="",height=500)

#Creación de objeto "Figure" de Plotly a partir de los objetos data y layout creados previamente
fig2 = go.Figure(data=data, layout=layout)


fig1 = px.histogram(df_db, x="Minutes", color="Company")



col3,col4 = st.columns(2)
#TOP PELÍCULAS
st.markdown('---')
st.markdown('---')
with col3:
    st.header("Top Películas Marvel-DC")
    st.metric(label="Número 1",value="The Dark Knight (DC)",delta ="90/100")
    st.image("descarga.jpeg",width=200)
    st.metric(label="Número 2",value="Joker (DC)",delta ="87/100")
    st.image("descarga (3).jpeg",width=200)
    st.metric(label="Número 3",value="Avengers: Infinity War (MARVEL)",delta ="85/100")
    st.image("descarga (2).jpeg",width=200)
    st.metric(label="Número 4",value="Avengers: Endgame (MARVEL)",delta ="85/100")
    st.image("descarga (1).jpeg",width=200)
    st.metric(label="Número 5",value="Spiderman: into the Spider-Verse (Marvel)",delta ="84/100")
    st.image("images.jpeg",width=200)

with col4:
    st.header("¿Qué nota le darías tú a las 15 Mejores  Películas?")
    TheDarkKnight = st.slider('The Dark Knight (90/100 IMDb):', 0, 100)
    Joker = st.slider('Joker (87/100 IMDb):', 0, 100)
    AvengersInfinityWar = st.slider('Avengers: Infinity War (85/100 IMDb):',0, 100)
    AvengersEndgame = st.slider('Avengers: Endgame(85/100 IMDb):', 0, 100)
    SpidermanintotheSpiderVerse = st.slider('Spiderman: into the Spider-Verse (84/100 IMDb):',0, 100)
    TheDarkKnightRises = st.slider('The Dark Knight Rises (84/100 IMDb):', 0, 100)
    SpiderManNoWayHome = st.slider('Spider-Man: No Way Home (82/100 IMDb):', 0, 100)
    BatmanBegins = st.slider('Batman Begins (82/100 IMDb):', 0, 100)
    TheAvengers = st.slider('The Avengers (80/100 IMDb):', 0, 100)
    GuardiansoftheGalaxy = st.slider('Guardians of the Galaxy (80/100 IMDb):', 0, 100)
    ZackSnydersJusticeLeague = st.slider('Zack Snyders Justice League (80/100 IMDb):', 0, 100)
    IronMan = st.slider('Iron Man (79/100 IMDb):', 0, 100)
    ThorRagnarok = st.slider('Thor:Ragnarok (79/100 IMDb):', 0, 100)
    BigHero6 = st.slider('Big Hero 6 (78/100 IMDb):', 0, 100)
    CaptainAmericaCivilWar = st.slider('Captain America: Civil War (78/100 IMDb):', 0, 100)
    st.header("Vídeo Parodia Marvel V.S DC ")
    st.video("Marvel VS DC (Parody Battle!).mp4")
    
st.image("marvelvs.jpeg")

col1,col2 = st.columns([6,4])

# Plot! 
with col1:
    st.header("Duración de sus películas")
    st.plotly_chart(fig1, use_container_width=False)
    
    rate_por_película = (df_db.groupby(by=['Original Title']).sum()[['Metascore']].sort_values(by='Metascore'))

    #Guardar el gráfico de barras en la siguiente variable

    fig_rate_pelicula = px.bar(
    rate_por_película,
    x = 'Metascore',
    y=rate_por_película.index, #se pone el index porque esta como index esa columna dentro del df nuevo que creamos que esta agrupado
    orientation= "h", #horizontal bar chart
    color_discrete_sequence = ["#f5b932"] * len(rate_por_película),
    template='plotly_white',)

    fig_rate_pelicula.update_layout(
    plot_bgcolor = "rgba(0,0,0,0)",
    xaxis=(dict(showgrid = False)))

    ventas_por_vendedor = (
    df_db.groupby(by=['Original Title']).sum()[['Gross Worldwide']].sort_values(by='Gross Worldwide'))

    
    #Crear la gráfica de barras para los vendedores
    fig_ventas_por_vendedor = px.bar(
    ventas_por_vendedor,
    x=ventas_por_vendedor.index,
    y='Gross Worldwide',
    color_discrete_sequence = ["#F5B932"]*len(ventas_por_vendedor),
    template = 'plotly_white',)

    fig_ventas_por_vendedor.update_layout(
    xaxis=dict(tickmode='linear'), # se asegura que todos los ejes de X se muestren
    plot_bgcolor='rgba(0,0,0,0)',
    yaxis=(dict(showgrid=False)),)    
    st.header("Recaudación por Película")
    st.plotly_chart(fig_ventas_por_vendedor, use_container_width = True) #esta va al lado izquierdo
    st.markdown("![Alt Text](https://media.tenor.com/tiZXjdtJUIkAAAAC/robert-downey-jr-tony-stark.gif)")
    


    

with col2:
    st.header("Valoración en IMDb según la Compañía")
    st.plotly_chart(fig2, use_container_width=False)
    st.header("Metapuntuación por Película")
    st.plotly_chart(fig_rate_pelicula, use_container_width = True)
    st.markdown("![Alt Text](https://media2.giphy.com/media/Indq8l4l6Tq13lNtxF/giphy360p.mp4?cid=ecf05e47q0te0ohz7ld2qpsp2h0jp7ax3msrpdma6zsc70ah&rid=giphy360p.mp4&ct=v&cc=en)")
st.markdown('---')

average_rating = round(df_db["Rate"].mean(), 1)
star_rating = ":star:" * int(7)

colu3,colu4,colu5=st.columns(3)

average_rating1 = round(df_db["Metascore"].mean(), 1)
star_rating2 = ":star:" * int(6)

star_rating3 = ":star:" * int(9)

with colu3:
    st.subheader("Valoración media de ambas Compañías:")
    st.subheader(f"{average_rating} {star_rating}")
with colu4:
    st.subheader("MetaPuntuación media de ambas Compañías:")
    st.subheader(f"{average_rating1} {star_rating2}")
with colu5:
    st.subheader("Mi puntuación de ambas Compañías:")
    st.subheader(f"{90.5} {star_rating3}")

st.markdown('---')


col7,col8 = st.columns(2)
with col7:
    st.header("Top Presupuesto Películas Marvel-DC")
    st.metric(label="Número 1",value="Avengers: Endgame (MARVEL)",delta ="356.000.000 $")
    st.image("descarga (1).jpeg",width=200)
    st.metric(label="Número 2",value="Justice League (DC)",delta ="300.000.000 $")
    st.image("images (1).jpeg",width=200)
    st.metric(label="Número 3",value="Superman Returns (DC)",delta ="270.000.000 $")
    st.image("Superman.jpeg",width=200)
    st.metric(label="Número 4",value="Avengers: Age of Ultron (MARVEL)",delta ="250.000.000 $")
    st.image("descarga (4).jpeg",width=200)
    st.metric(label="Número 5",value="Captain America: Civil War (Marvel)",delta ="250.000.000 $")
    st.image("descarga (5).jpeg",width=200)
with col8:
    st.header("Top Recaudación Películas Marvel-DC") 
    st.metric(label="Número 1",value="Avengers: Endgame (MARVEL)",delta ="2.797.800.564 $")
    st.image("descarga (1).jpeg",width=200)
    st.metric(label="Número 2",value="Avengers: Infinity War (MARVEL)",delta ="2.048.359.754 $")
    st.image("descarga (2).jpeg",width=200)
    st.metric(label="Número 3",value="Spider-Man: No way Home (Marvel)",delta ="1.921.847.111 $")
    st.image("descarga (7).jpeg",width=200)
    st.metric(label="Número 4",value="The Avengers (MARVEL)",delta ="1.518.812.988 $")
    st.image("descarga (6).jpeg",width=200)
    st.metric(label="Número 5",value="Avengers: Age of Ultron (MARVEL)",delta ="1.402.805.868 $")
    st.image("descarga (4).jpeg",width=200)
st.markdown('---')

col9,colu1,colu2 = st.columns(3)

st.markdown('---')

with col9:
    st.markdown("![Alt Text](https://media.tenor.com/ltb7ljnfN6IAAAAM/spider-man.gif)")
with colu1:
    st.markdown("![Alt Text](https://media.tenor.com/Xi8AFdU2VXIAAAAM/spiderman-superhero.gif)")
with colu2:
    st.subheader("¿Qué nota debería tener este trabajo")
    radio = st.radio("Elige Sabiamente",options = ["9,5",
                                                 "9,9",
                                                 "10"])
    if radio == "9,5":
        st.markdown("MUY BIEN")
    elif radio == "9,9":
        st.markdown("MEJOR AÚN")
    elif radio == "10":
        st.markdown("OLE OLE")
    else:
        pass


st.header("Gracias por visitar la Web!!")
st.audio("Marvel.mp3")