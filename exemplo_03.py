"""
App mini analisador de linguagem natural com spaCy.
"""

import streamlit as st
from streamlit.components import v1 as components

from spacy import load, displacy


nlp = load("pt_core_news_lg")

bar = st.sidebar

escolha = bar.selectbox("Escolha uma categoria", ["Entidades", "Gramática"])

textao = st.text_area("Bote um textão aqui!")

if textao:
    doc = nlp(textao)

    if escolha == "Entidades":
        data = displacy.render(doc, style="ent")

        with st.expander("Dados do spaCy"):
            components.html(data, scrolling=True, height=300)

        for e in doc.ents:
            a, b = st.columns(2)
            a.info(e)
            b.warning(e.label_)

    elif escolha == "Gramática":
        filtros = bar.multiselect(
            "Filtro", 
            ["VERB", "PROPN", "ADV", "AUX"], 
            default=["VERB", "PROPN"]
        )

        with st.expander("Dados do spaCy"):
            st.json(doc.to_json())

        container = st.container()
        a, b, c = st.columns(3)

        a.subheader("Token")
        b.subheader("TAG")
        c.subheader("MORPH")

        for t in doc:
            if t.tag_ in filtros:
                container = st.container()
                a, b, c = st.columns(3)
                a.info(t)
                b.warning(t.tag_)
                c.error(t.morph)
            