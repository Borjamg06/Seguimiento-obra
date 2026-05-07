import streamlit as st
import pandas as pd
from datetime import datetime

# Configuración de la página
st.set_page_config(page_title="App Electricista", page_icon="⚡")

st.title("⚡ Registro de Tareas de Electricista")

# Formulario de entrada
nombre = st.text_input("Nombre del Electricista:")
tarea = st.selectbox("Selecciona la tarea realizada:", [
    "Instalación de luminarias",
    "Mantenimiento de tableros",
    "Cableado estructurado",
    "Reparación de cortocircuito",
    "Instalación de toma corrientes"
])

if st.button("Guardar Registro"):
    if nombre:
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        nuevo_registro = f"{fecha} - {nombre} - {tarea}\n"
        
        # Guardar en un archivo de texto
        with open("tareas.txt", "a", encoding="utf-8") as f:
            f.write(nuevo_registro)
            
        st.success(f"¡Hecho! Tarea '{tarea}' registrada con éxito.")
    else:
        st.error("Por favor, escribe tu nombre.")

# Mostrar historial básico
if st.checkbox("Ver historial de tareas"):
    try:
        with open("tareas.txt", "r", encoding="utf-8") as f:
            st.text(f.read())
    except FileNotFoundError:
        st.write("Aún no hay registros.")
