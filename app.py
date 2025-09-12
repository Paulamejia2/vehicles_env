import streamlit as st
import pandas as pd
import plotly.express as px


car_data = pd.read_csv('vehicles_us.csv')


st.title("Análisis de vehículos 🚗")


st.write("Vista previa de los datos:")
st.dataframe(car_data.head())

hist_button = st.button('Construir histograma') # crear un botón
     
if hist_button: # al hacer clic en el botón
       
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
        
    fig = px.histogram(car_data, x="odometer")
     
       
    st.plotly_chart(fig, use_container_width=True)



if st.checkbox("Mostrar dispersión precio vs odómetro"):
    fig2 = px.scatter(car_data, x="odometer", y="price", title="Precio vs Odómetro")
    st.plotly_chart(fig2)
    
if st.checkbox("Mostrar histograma de odómetro"):
    fig = px.histogram(car_data, x="odometer", nbins=30, title="Distribución del odómetro")
    st.plotly_chart(fig, use_container_width=True)
