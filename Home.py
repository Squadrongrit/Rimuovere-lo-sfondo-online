import base64
import streamlit as st
from rembg import remove
from PIL import Image
from PIL import ImageEnhance
from PIL import GifImagePlugin
from PIL import ImageSequence
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
    height: 400px;
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

.css-fis6aj {
    left: 0px;
    right: 0px;
    line-height: 1.25;
    padding-top: 0.75rem;
    padding-left: 1rem;
    padding-right: 1rem;
    display: none;
}

</style>
"""
st.markdown(style, unsafe_allow_html=True) #Title rendering

st.title("Rimuovi gli sfondi automaticamente al 100% in 5 secondi con un clic")
colb1, colb2 = st.columns(2)
images = colb2.file_uploader("", accept_multiple_files =True, type=['png', 'jpg','Jpeg', 'gif'])

colb1.image("background-removal-banner-1.jpg")


if images:
    for image in images:
        #ottengo il tipo del file
        file_details = image.type
        #se il file è 'png', 'jpg','Jpeg'
        if file_details == 'image/png' or file_details == 'image/jpg' or file_details == 'image/Jpeg':
            with st.spinner("Rimozione del background in corso..."):
                with st.expander("Immagine numero {}".format(images.index(image)+1)):
                    col1, col2 = st.columns(2)
                    col1.header("Originale")
                    col2.header("Senza Sfondo")
                    with Image.open(image) as img:
                        col1.image(img, caption="Dimensioni originali: {}x{}".format(img.size[0], img.size[1]))

                        output = remove(img)
                        col2.image(output, caption="Dimensioni senza sfondo: {}x{}".format(img.size[0], img.size[1]))

                        st.header("Migliorate dalla nostra IA")
                        curr_bri = ImageEnhance.Brightness(output)
                        new_bri = 1.1
                        img_brightened = curr_bri.enhance(new_bri)
                        curr_col = ImageEnhance.Color(img_brightened)
                        new_col = 1.1
                        img_colored = curr_col.enhance(new_col)
                        curr_con = ImageEnhance.Contrast(img_colored)
                        new_con = 1.05
                        img_contrasted = curr_con.enhance(new_con)

                        curr_bri2 = ImageEnhance.Brightness(output)
                        new_bri2 = 1.1
                        img_brightened2 = curr_bri2.enhance(new_bri2)
                        curr_col2 = ImageEnhance.Color(img_brightened2)
                        new_col2 = 1.2
                        img_colored2 = curr_col2.enhance(new_col2)
                        curr_con2 = ImageEnhance.Contrast(img_colored2)
                        new_con2 = 1.2
                        img_contrasted2 = curr_con2.enhance(new_con2)

                        col3, col4 = st.columns(2)
                        output2 = remove(img_contrasted2)
                        output3 = remove(img_contrasted)
                        col3.image(output3, caption="Immagine Migliorata poco dalla nostra IA")
                        col4.image(output2, caption="Immagine Migliorata molto dalla nostra IA")

                        st.info("Per scaricare le immagini usa il tasto destro del mouse")
        #se è gif
        elif file_details == 'image/gif':
            with st.spinner("Rimozione del background dalla GIF in corso... Può richiedere più tempo rispetto ad una semplice immagine"):
                with st.expander("GIF numero numero {}".format(images.index(image)+1)):
                    col1, col2 = st.columns(2)
                    col1.header("Originali")
                    col2.header("Senza Sfondo")
                    with Image.open(image) as img:
                        #salvo il gif originale

                        #if image dimension is too large, resize it of 50%
                        if img.size[0] > 500 or img.size[1] > 500:
                            img = img.resize((int(img.size[0]/2), int(img.size[1]/2)))
                        
                        img.save("gif{}.gif".format(images.index(image)+1))
                        file = open("gif{}.gif".format(images.index(image)+1), 'rb')
                        contents = file.read()
                        data_url = base64.b64encode(contents).decode('utf-8-sig')
                        file.close()
                        col1.markdown(f'<img src="data:image/gif;base64,{data_url}">',unsafe_allow_html = True)
                        frames = []
                        for frame in ImageSequence.Iterator(img):
                            output = remove(frame)
                            frames.append(output)
                        #save the new gif
                        frames[0].save("gif_no_bg{}.gif".format(images.index(image)+1), save_all=True, append_images=frames[1:], loop=0)
                        file2 = open("gif_no_bg{}.gif".format(images.index(image)+1), 'rb')
                        contents2 = file2.read()
                        data_url2 = base64.b64encode(contents2).decode('utf-8-sig')
                        file2.close()
                        col2.markdown(f'<img src="data:image/gif;base64,{data_url2}">',unsafe_allow_html = True)
                        st.info("Per scaricare le immagini usa il tasto destro del mouse")