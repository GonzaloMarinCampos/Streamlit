from curses.ascii import alt
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objs as go

st.set_page_config(page_title="Comparación Peliculas Marvel-DC",
                page_icon= "alien:",
                layout="wide")

def main():
    c6,c7,c8= st.columns(3)
    with c7:
        st.title("Marvel V.S. DC")

    menu = ["Historia de ambas Compañías", "Comparación Marvel-DC", "Gráficos"]
    choice = st.sidebar.selectbox("Seleccione una opción", menu)

    if choice == "Historia de ambas Compañías":
        st.title("Primeras Páginas de su Historia")
        c1,c2 = st.columns([5,5])
        st.markdown('---')
        with c1:
            st.image("marve.jpeg")
            st.title("Primer Cómic de Marvel 1939")
            st.markdown("Marvel Comics, es una editorial de historietas estadounidense creada en 1939, inicialmente con el nombre de Timely Publications. Entre sus personajes emblemáticos del género superheroico se encuentran Spider-Man, Wolverine, X-Men, Capitán América, Iron Man, Hulk, Thor, Los 4 Fantásticos, Daredevil, Punisher, Los Vengadores, entre otros. A partir de los años 1990, la compañía se posicionó como una de las principales editoriales de cómics del país. El 31 de agosto de 2009, The Walt Disney Company compró Marvel Entertainment por cerca de 4 000 millones de dólares. El primer cómic de Timely Comics, apareció con fecha de portada en octubre de 1938. Este primer número incluía las aventuras de los tres primeros superhéroes de la editorial, el androide conocido como la Antorcha Humana, el antihéroe Namor y el Ángel (sin relación con el personaje de los X-Men)")

        with c2:
            st.image("Action_Comics_1.jpeg")
            st.title("Primer Cómic de DC 1938")
            st.markdown("DC Comics es una editorial de cómics estadounidense. Forma parte de DC Entertainment,​ una de las empresas que conforman Warner Bros. Entertainment, la cual a su vez es propiedad de Warner Bros. Discovery. Fue fundada en 1934 bajo el nombre National Allied Publications, para luego tomar el nombre de DC Comics en 1937.Entre algunos de sus personajes más emblemáticos se encuentran Superman, Batman, Mujer Maravilla, Flash, Linterna Verde, Aquaman, Hombre Halcón, Chica Halcón, Flecha Verde, Shazam, Detective Marciano, Starfire, Nightwing, Raven, Cyborg, Canario Negro, Doctor Destino, Robin, Chico Bestia, Zatanna, Hombre Plástico, Catwoman, Supergirl, El Joker y Harley Quinn. Su sede principal estuvo situada históricamente en la ciudad de Nueva York, pero desde 2015 mudaron sus oficinas a la ciudad de Burbank (LA)")
        
        co1,co2,co3= st.columns(3)
        with co2:
            st.title("Fuera del Papel")

        c3,c4= st.columns([5,5])
        st.markdown('---')
        st.markdown('---')
        with c3:
            st.image("fase-4.jpeg")
            st.markdown("La relación de Marvel con la televisión comenzó en 1967, durante el apogeo de las teleseries de superhéroes tanto de imagen real como de animación.​ La productora Grant-Ray-Lawrence Company compró los derechos de los personajes para realizar una serie de animación, La hora Marvel, un espacio semanal de media hora que adaptaba de forma muy fiel aventuras del Capitán América, Hulk, Iron Man, Namor y Thor. El éxito de la serie permitió que se produjesen otras como, Spider-Man, Los 4 Fantásticos y años más tarde, Spider-Woman y The Avengers.​ A lo largo de los años 1970, Marvel también licenció algunos de sus personajes para series de imagen real, algunas de las cuales obtuvieron bastante éxito, como El increíble Hulk (1977), mientras que otras no lograron conectar con el público, como pasó con la serie Spider-Man. Los primeros intentos de Marvel por producir películas de sus personajes tuvieron, en el mejor de los casos, escaso éxito. Las películas para televisión de Doctor Strange y Capitán América lograron conectar con el público a mayor profundidad que Spider-Man.​ Aunque Stan Lee pasó buena parte de los años 1980 y 90 buscando productores interesados en hacer películas con personajes de Marvel, los resultados fueron igualmente pobres, como Howard el pato en 1986, El Castigador en 1989 o Capitán América en 1990. Una película centrada en Los 4 Fantásticos fue producida en 1994 pero nunca llegó a comercializarse, lo que da una idea de su calidad.No obstante, la suerte de las películas de Marvel cambiaría a partir de 1997 con el estreno de Blade y, sobre todo, X-Men en 2000, que recaudó 54 millones de dólares en su primer fin de semana.​ Seguirían otras películas, como la primera trilogía de Spider-Man iniciada en 2002, las secuelas de X-Men y las películas centradas en diferentes personajes del Universo Marvel. El éxito de estas películas llevó a un litigio entre la editorial y Stan Lee, la cara pública de Marvel, en 2002. Stan Lee demandó 10 millones de dólares en concepto de beneficios por las películas y las series televisivas, basándose en un contrato entre él y Marvel de 1998.​Aunque las películas de personajes Marvel fueron realizadas en un primer momento en colaboración con diversos estudios cinematográficos sin conexión directa con el mundo del cómic, Marvel Studios se ocupó a partir de 2008 de producir sus propias películas. Los resultados de la implicación directa de Marvel en la producción de sus películas han sido una Trilogía de Iron Man, una Trilogía de Thor, una Trilogía de Capitán América, una Tetralogía de Los Vengadores y películas de Guardianes de la Galaxia, Ant-Man, Doctor Strange, Spider-Man, Black Panther, Capitana Marvel, Black Widow, Shang-Chi y Eternals. Derivando así, en la creación del Universo cinematográfico de Marvel, actualmente la franquicia más exitosa de la historia del cine.")
        with c4:
            st.image("dchi.jpeg")
            st.markdown("En septiembre de 2009, Warner Bros. anunció que DC Comics se convertiría en DC Entertainment Inc., con Diane Nelson (presidente de Warner Premiere) como presidente de la nueva empresa. Paul Levitz (anterior presidente de DC Comics) fue designado editor, colaborador y asesor general. El 18 de febrero de 2010, DC Entertainment convocó a Jim Lee y a Dan DiDio como co-editores de DC Comics, Geoff Johns como ejecutivo creativo en jefe, John Rood como vicepresidente ejecutivo de Ventas, Marketing y Desarrollo de Negocio, y Caldon Patrick como vicepresidente ejecutivo de Finanzas y Administración. Actualmente, Jim Lee es presidente de DC Entertainment. DC Entertainment se encargará de llevar a la gran pantalla a los superhéroes y demás personajes de DC Comics. También, DC Entertainment se ocupará de los videojuegos, televisión, Internet, y del sector editorial, con la publicación de novelas gráficas y nuevos cómics. En 2016, se crea DC Films como division especial de las películas del Universo Extendido de DC, siendo Geoff Johns y Walter Hamada los encargados de la división.  .DC Entertainment se ocupó de las películas basadas en personajes e historias del catálogo de DC Comics, comenzando con Jonah Hex, Los Perdedores y la película Linterna Verde, dirigida por Martin Campbell que se estrenó el 17 de junio de 2011. Entre las más destacadas están; La Trilogía de The Dark Knight de Christopher Nolan. V for Vendetta y Watchmen, ambas del sello Vertigo. En 2013 se estrenó El hombre de acero, el anunciado reinicio de Superman, el cual fue dirigido por Zack Snyder, producido por Christopher Nolan y guionizado por David S. Goyer. Así mismo, Nolan participó como director y productor de The Dark Knight Rises. El guion de la película estuvo a cargo de Jonathan Nolan y estuvo basado en un argumento escrito por David S. Goyer y Christopher Nolan, la cual se estrenó en el verano de 2012, siendo la última entrega de la saga dirigida por Nolan. En julio de 2013 se anunció la película de Batman y Superman para 2015, aunque en un principio se especuló que la película saldría en 2015, la fecha de estreno fue postpuesta a mayo de 2016, para posteriormente adelantarse a marzo del mismo año, para no coincidir con el Mega-estreno de Marvel Studios Capitán América: Civil War. Esto con el fin de dar inicio a un Universo Cinematográfico de DC y con la película de Justice League estrenándose en 2 partes, una en 2017 y otra en 2019 con Zack Snyder como director de ambas. El universo extendido cuenta con títulos como Batman v Superman: Dawn of Justice, Escuadrón suicida (2016), Wonder Woman (2017), Aquaman (2018), Shazam! (2019), The Batman (2021), The Flash , Green Lantern Corps (2022). Así como la secuela de Wonder Woman, Wonder Woman 1984 , la versión de The Suicide Squad de James Gunn, The Flash, la película en solitario de Batgirl.")

        
        st.image("Stanlee.jpeg")


    elif choice == "Comparación Marvel-DC":
        import plotly.express as px
        st.header(":alien:¿Cuál será la mejor compañía?")
        st.header("Date un gusto escuchando esto")
        st.audio("Avengers Infinity war.mp3")
        st.image("marvel-dc.jpeg")

        st.header("Comparación Peliculas Marvel-DC (Opción de Filtrar en la esquina superior izquierda)")

        #st.write("")

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
        st.markdown('---')
        st.image("dcvs.jpeg")
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
        st.markdown('---')
        st.markdown('---')  
        cl6,cl7=st.columns([6,4])
        with cl6:
            st.markdown("![Alt Text](https://media2.giphy.com/media/Indq8l4l6Tq13lNtxF/giphy360p.mp4?cid=ecf05e47q0te0ohz7ld2qpsp2h0jp7ax3msrpdma6zsc70ah&rid=giphy360p.mp4&ct=v&cc=en)")
        with cl7:
            st.markdown("![Alt Text](https://media.tenor.com/tiZXjdtJUIkAAAAC/robert-downey-jr-tony-stark.gif)")
        st.markdown('---')
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
        
    elif choice == "Gráficos":
        import plotly.express as px
        df_db = pd.read_excel(r'db.xls')
        # Create a scatter plot
        fig = px.scatter(df_db, x="Release", y="Opening Weekend USA", facet_col="Company", color="Original Title")

        # Show the chart
        st.plotly_chart(fig)
        st.markdown('---')
        st.markdown('---')
        cl3,cl4=st.columns(2)
        with cl3:

            import altair as alt
            # Create a chart
            chart = alt.Chart(df_db).mark_bar().encode(
                x='Minutes',
                y='Company'
            )

            # Show the chart
            st.altair_chart(chart)
        with cl4:

            chart = alt.Chart(df_db).mark_bar().encode(
                x='Gross Worldwide',
                y='Company'
            )

            # Show the chart
            st.altair_chart(chart)

        data = [go.Box(x=df_db["Company"],y=df_db["Rate"])] #pointpos=0 para ubicación de los puntos en el centro / boxpoints ="all" si se quieren visualizar todos los puntos

        #Definición de objeto "layout": diseño del gráfico como título, nombres de ejes,...
        layout = go.Layout(title="",height=500)

        #Creación de objeto "Figure" de Plotly a partir de los objetos data y layout creados previamente
        fig2 = go.Figure(data=data, layout=layout)


        fig1 = px.histogram(df_db, x="Minutes", color="Company")

        st.markdown('---')
        st.markdown('---')
        col1,col2 = st.columns([5,5])
        
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
         
        st.markdown('---')
        st.markdown('---')   
        st.header("Recaudación por Película")
        st.plotly_chart(fig_ventas_por_vendedor, use_container_width = True) #esta va al lado izquierdo
        

            

        with col2:
            st.header("Valoración en IMDb según la Compañía")
            st.plotly_chart(fig2, use_container_width=False)
        st.markdown('---')
        st.markdown('---')
        import matplotlib.pyplot as plt

        st.header("Metapuntuación por Película")
        st.plotly_chart(fig_rate_pelicula, use_container_width = True)
        st.markdown('---')
        # Create some data
        st.title("Comparación de la recaudación de Superman")
        labels = ['Superman', 'Superman 2', 'Superman 3', 'Superman 4']
        sizes = [300000000, 108185706, 59950623, 15681020]
        st.set_option('deprecation.showPyplotGlobalUse', False)

        # Create a pie chart
        plt.pie(sizes, labels=labels)

        # Show the chart
        st.pyplot()
        st.markdown('---')
        st.markdown('---')

        

if __name__== "__main__":
    main()
