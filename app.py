import streamlit as st
import pandas as pd
st.title("Proyecto Final Diploma BI")

st.sidebar.title("Parámetros")

st.image("Python_logo.png",width = 500)
st.sidebar.image("DMC.png",width = 100)

st.write("Elaborado por: Miguel Herrera")

archivo = st.file_uploader("Cargue el archivo excel o csv")

if archivo is not None :
  if archivo.name.endwith(".csv"):
    data = pd.read_csv(archivo)
  elif archivo.name.endswith(".xlsx"):
    data = pd.read_excel(archivo)
  else:
    st.write("Formato no válido")
  
else :
  st.write("Por favor cargue su archivo")
