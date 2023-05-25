# Import des librairies Python.
from joblib import load
import streamlit as st

# Texte de présentation.
st.title('Chat ou chien ?')
st.header('Notre IA vous donne la réponse.')

# Chargement de l'image.
uploaded_file = st.file_uploader(
    'Chargez votre image :', type=['png', 'jpg'], help='Faites glisser et déposez ou parcourez vos fichiers.')

if uploaded_file is not None:
    # Affichage de l'image fournie.
    st.image(uploaded_file)

    @st.cache_resource
    def load_model(joblib_file):
        ''' Chargement du modèle dans le cache.'''
        global model
        model = load(joblib_file)
        return model
    model = load_model('cnn_model.joblib')
    image_size = (180, 180)
    # Import retardé des modules Tensorflow et Keras pour permettre à la page de se charger rapidement.
    import tensorflow as tf
    from tensorflow import keras
    # Restitution des prédictions avec la probabilité de la classification.
    img = keras.preprocessing.image.load_img(
        uploaded_file, target_size=image_size)
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create batch axis
    predictions = model.predict(img_array)
    score = float(predictions[0])
    st.header('Probabilités')
    st.subheader(f'Chat : {100 * (1 - score):.2f} %')
    st.subheader(f'Chien : {100 * score:.2f} %')
    st.success('Bravo, vous savez utiliser une IA 🤖', icon="✅")
