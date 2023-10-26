import base64
import streamlit as st
from rembg import remove
from PIL import Image
from PIL import ImageEnhance
from PIL import GifImagePlugin
from PIL import ImageSequence
import numpy as np
images=st.image("background-removal-banner-1.jpg")
st.file_uploader("", accept_multiple_files =True, type=['png', 'jpg','Jpeg', 'gif'])
style = """
<style>
#root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0.5rem;}
.css-po3vlj {
    display: flex;
    -webkit-box-align: center;
    align-items: center;
    padding: 1rem;
    background-color: #076ad9;
    border-radius: 0.5rem;
    color: rgb(49, 51, 63);
    height: 350px;
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
    color: darkblue;
    font-size: smaller;
    line-height: 1.25;
}

.css-fis6aj {
    padding-top: 0.75rem;
    display: block;
    width: 80%;
}

.css-12xsiil {
    display: flex;
    -webkit-box-align: center;
    align-items: center;
    margin-bottom: 0.05rem;
    font-size: small;
}

.css-vskyf7 {
    vertical-align: middle;
    overflow: hidden;
    color: blue;
    fill: currentcolor;
    display: inline-flex;
    -webkit-box-align: center;
    align-items: center;
    font-size: 0.8rem;
    width: 0.8rem;
    height: 0.8rem;
}

.css-fblp2m {
    vertical-align: middle;
    overflow: hidden;
    color: inherit;
    fill: currentcolor;
    display: inline-flex;
    -webkit-box-align: center;
    align-items: center;
    font-size: 1.25rem;
    width: 1.25rem;
    height: 1.25rem;
    padding-left: 5px;
}
.css-18ni7ap {
    /* position: fixed; */
    top: 0px;
    left: 0px;
    right: 0px;
    height: 2.875rem;
    background: rgb(255, 255, 255);
    outline: none;
    z-index: 999990;
    display: none;
}
</style>


"""
st.markdown(style, unsafe_allow_html=True) #Title rendering



if images:
    for image in images:
        #ottengo estensione del file
        ext = image.name.split(".")[-1]
        # se ext è 'png', 'jpg','Jpeg'
        if ext in ['png', 'jpg','Jpeg', 'jpeg', 'JPG']:
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
                        #save image
                        #output2.save("output2{}.png".format(images.index(image)+1))
                        #output3.save("output3{}.png".format(images.index(image)+1))

                        
 
                        #sr = cv2.dnn_superres.DnnSuperResImpl_create()
                        #path = "ESPCN_x4.pb"
                        #sr.readModel(path) 
                        #sr.setModel("espcn", 4) # set the model by passing the value and the upsampling ratio
                        #result = sr.upsample(output2)
                        #result2 = sr.upsample(output3)
                        #col5, col6 = st.columns(2)
                        #col5.image(result, caption="Immagine Migliorata molto dalla nostra IA + Super Resolution")
                        #col6.image(result2, caption="Immagine Migliorata poco dalla nostra IA + Super Resolution")
                        st.info("Per scaricare le immagini usa il tasto destro del mouse")
        #se è gif
        elif ext == 'gif':
            st.info("Stiamo lavorando per migliorare la rimozione del background per i file gif")
            # rimuovi gif da images
            images.remove(image)
