import streamlit as st
from rembg import remove
from PIL import Image
import numpy as np

st.title("rembg Demo")
images = st.file_uploader("Load Image", accept_multiple_files =True, type=['png', 'jpg','Jpeg'])

if images:
    col1, col2 = st.columns(2)
    for image in images:
        col1.header("Originali")
        col2.header("Senza Sfondo")
        with Image.open(image) as img:
            col1.image(img)

            output = remove(img)
            col2.image(output)
