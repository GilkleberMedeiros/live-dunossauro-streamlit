"""
App visualizador de arquivos (.jpg, .jpeg, .png, .py, .js, .wav, .csv, .json). 
"""

import streamlit as st
from  pandas import read_csv

from json import loads


DISPLAY = {
    "jpg": lambda f: st.image(f), 
    "png": lambda f: st.image(f), 
    "jpeg": lambda f: st.image(f), 
    "x-python": lambda f: st.code(f.read().decode(), wrap_lines=True), 
    "javascript": lambda f: st.code(f.read().decode(), "javascript", wrap_lines=True), 
    "wav": lambda f: st.audio(f.read()), 
    "csv": lambda f: st.dataframe(read_csv(f)),
    "json": lambda f: st.json(loads(f.read()))
}

st.markdown("""
    # Visualizador de arquivos
            
    Suba seu arquivo para tentar visualizá-lo 😄
""")

arquivo = st.file_uploader(
    "Envie seu arquivo aqui 👇", 
    ["jpg", "png", "py", "js", "wav", "csv", "json"], 
)

if arquivo:
    type1, type2 = arquivo.type.split("/")

    display_func = DISPLAY.get(type2) 
    if not display_func:
        st.status(f"Não pôde mostrar o arquivo do tipo {type2}!!")

    display_func(arquivo)