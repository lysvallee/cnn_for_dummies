import base64
from pathlib import Path
import streamlit as st


st.set_page_config(layout="wide")

# Fonctions permettant d'indiquer l'emplacement local d'une image dans st.markdown.


def img_to_bytes(img_path):
    '''Conversion de l'image en bytes'''
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded


def img_to_html(img_path):
    '''Ecriture du code HTML à partir de l'image convertie'''
    img_html = "<img id='image' src='data:image/png;base64,{}' class='img-fluid'>".format(
        img_to_bytes(img_path)
    )
    return img_html


# Lien vers le fichier CSS.
with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Code HTML permettant d'afficher la page d'accueil avec du style CSS.
st.markdown('<main><div id="landing"> <div id="landing-text"> <h1>L\'IA voit vos images à votre place</h1> <h2>Aussi fidèle qu\'un chien...</h2>' +
            img_to_html('images/dog-g42c306bca_1280.jpg') + '</div> </main>', unsafe_allow_html=True)

# END
