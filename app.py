import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

header_text = "Genera histogramas y gráficas de dispersión"
st.title(header_text)

subheader_text = "Botones mágicos"
st.markdown(f"**{subheader_text}**")

hist_button = st.button('Construir histograma') # crear un botón

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

hist_button = st.button('Construir gráfico de dispersión') # crear un botón

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")  # Línea separadora
subsubheader_text = "Casillas de verificación"
st.markdown(f"**{subsubheader_text}**")

# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')

        # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# crear una casilla de verificación
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter: # si la casilla de verificación está seleccionada
    st.write('Construir un gráfico de dispersión para la columna odómetro')

        # crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)