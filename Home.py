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
    background-color: #f5f5f5;
    border-radius: 0.5rem;
    color: rgb(49, 51, 63);
    height: 300px;
    width: 90%;
    box-shadow: 10px 10px 5px #dedede;
}
</style>
"""
st.markdown(style, unsafe_allow_html=True) #Title rendering

st.title("Rimuovi gli sfondi automaticamente al 100% in 5 secondi con un clic")
colb1, colb2 = st.columns(2)
images = colb2.file_uploader("Trascina una o più immagini", accept_multiple_files =True, type=['png', 'jpg','Jpeg'])
colb1 = st.markdown("![Alt Text](remove-gif.242b60d.gif)")

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
