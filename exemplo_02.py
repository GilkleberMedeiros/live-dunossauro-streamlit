"""
Aplicativo de marca d'água em imagem. Fornecida uma imagem, um texto, uma cor de fonte e um tamanho de fonte 
coloca o texto, com a cor informada e com o tamanho informado no centro da imagem.
"""


import streamlit as st

from PIL import Image, ImageFont, ImageDraw

def text_on_image(image, text, font_size, color): 
    """Draws text on image"""
    img = Image.open(image)
    font = ImageFont.truetype("arial.ttf", font_size)
    draw = ImageDraw.Draw(img)

    iw, ih = img.size
    fxs, fys, fxe, fye = font.getbbox(text)
    fw, fh = (fxe), (fye)

    draw.text(
        ((iw - fw) / 2, (ih - fh) / 2),
        text=text, 
        fill=color, 
        font=font
    )

    img.save("image.png")

image = st.file_uploader("Imagem:", ["jpg", "png"]) 
text = st.text_input("Seu texto para marca d'água: ")
#color = st.selectbox("Cor da sua marca d'água: ", ["black", "white", "grey"])
color = st.color_picker("Cor da marca d'água: ") 
font_size = st.number_input("Tamanho da fonte da marca d'água: ", 50) 

if image: 
    img_name = image.name
    mime = image.type

    result = st.button(
        "Aplicar", 
        type="primary", 
        on_click=text_on_image, 
        args=(image, text, font_size, color), 
    )

    if result:
        st.image("image.png")
        with open("image.png", "rb") as file: 
            st.download_button(
                label="Baixar imagem", 
                data=file, 
                file_name=img_name, 
                mime=mime
            )

