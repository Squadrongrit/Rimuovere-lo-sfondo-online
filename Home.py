import base64
import streamlit as st
from rembg import remove
from PIL import Image
import numpy as np

style = """
<style>
.css-po3vlj {
    display: flex;
    -webkit-box-align: center;
    align-items: center;
    padding: 1rem;
    background-color: #076ad9;
    border-radius: 0.5rem;
    color: rgb(49, 51, 63);
    height: 300px;
    width: 90%;
    box-shadow: 10px 10px 5px #dedede;
    text-align: center;
}
.css-6kekos {
    -webkit-box-align: center;
    align-items: center;
    -webkit-box-pack: center;
    justify-content: center;
    font-weight: 400;
    padding: 0.25rem 0.75rem;
    border-radius: 0.25rem;
    margin: 0px;
    line-height: 1.6;
    color: inherit;
    width: auto;
    user-select: none;
    background-color: rgb(255, 255, 255);
    border: 1px solid rgba(49, 51, 63, 0.2);
    display: none;
}

.css-u8hs99 {
    margin-right: auto;
    -webkit-box-align: center;
    align-items: center;
    text-align: center;
    padding-left: 10%;
    display: block;
}

.css-noeb3a {
    vertical-align: middle;
    overflow: hidden;
    color: white;
    fill: currentcolor;
    display: inline-flex;
    -webkit-box-align: center;
    align-items: center;
    font-size: 2.3rem;
    width: 4.3rem;
    height: 4.3rem;
}

.css-1fttcpj {
    display: flex;
    flex-direction: column;
    color: white;
}

.css-1aehpvj {
    color: white;
    font-size: 14px;
    line-height: 1.25;
}

</style>
"""
st.markdown(style, unsafe_allow_html=True) #Title rendering

st.title("Rimuovi gli sfondi automaticamente al 100% in 5 secondi con un clic")
colb1, colb2 = st.columns(2)
images = colb2.file_uploader("Trascina una o più immagini", accept_multiple_files =True, type=['png', 'jpg','Jpeg'])

colb1.image("background-removal-banner-1.jpg")

if images:
    col1, col2 = st.columns(2)
    for image in images:
        with st.expander("Immagine numero {}".format(images.index(image)+1)):
            col1.header("Originali")
            col2.header("Senza Sfondo")
            with Image.open(image) as img:
                col1.image(img, caption="Dimensioni originali: {}x{}".format(img.size[0], img.size[1]))

                output = remove(img)
                col2.image(output, caption="Dimensioni senza sfondo: {}x{}".format(output.size[0], output.size[1]))
