import streamlit as st
from PIL import Image

st.title('Le réseau de neurones convolutif')

# Sous-partie expliquant l'utilité d'un CNN
st.header('Objectif')
st.markdown("Analyser des données complexes (en particulier des images) qui pourraient difficilement être traitées par des réseaux de neurones traditionnels : étant donné le nombre de pixels dans une image haute définition, il faudrait un nombre pharaonique de multiplications si chaque neurone d'une couche était connecté à la couche suivante.")

image = Image.open('images/traditional_network.png')
st.image(image, caption="Les multiples connexions d'un réseau de neurones artificiels")

# Sous-partie expliquant le processus
st.header('Fonctionnement')
st.markdown("Un CNN considère une image comme un ensemble de caractéristiques plus simples à évaluer : par exemple, un lapin pourra être reconnu grâce à ses grandes oreilles, ses yeux arrondis, son pelage, ses pattes...")

image = Image.open('images/hare-4639512.jpg')
st.image(image, caption="Parmi les attributs possibles pour un lapin...")

st.markdown("Pour pouvoir déterminer chacune de ces caractéristiques, le CNN va appliquer un filtre approprié sur l'image. Cette opération mathématique s'appelle une convolution (d'où le nom) et aboutit à un nombre de pixels moindre.")

# Sous-partie expliquant les avantages
st.header('Forces')
st.markdown("Outre la diminution de la complexité, cette technique permet de prévenir l'écueil habituel quand une machine cherche à apprendre à partir de données : elle aura tendance à coller aux exemples fournis au point d'être incapable de généraliser quand on lui présente de nouveaux cas.\nC'est typiquement ce qui arrive dans le cas de réseaux où chaque neurone est connecté à la couche suivante. Ici, il n'est pas nécessaire de simplifier en stoppant le processus ou en diminuant le nombre de neurones.\n\nLe filtrage par convolution est aussi conçu pour s'adapter à une image différente. Par exemple, il pourra détecter plusieurs types d'ovales permettant la reconnaissance de chiffres:")

image = Image.open('images/ovales.jpg')
st.image(image, caption="Les multiples connexions d'un réseau de neurones artificiels")

st.markdown("Autre avantage : les données peuvent être ingérées sans réclamer beaucoup de préparation. Il suffit juste d'ajuster la taille des images et la valeur des pixels (entre 0 et 1 au lieu de 0 à 255).\n\nMalgré (ou grâce à) toutes ces simplifications, le CNN obtient des performances inégalées dans la reconnaissance d'images et dans de nombreux autres domaines, comme nous le verrons ultérieuremnt.")

# Sous-partie expliquant les faiblesses d'un CNN
st.header('Faiblesses')
st.subheader('La fameuse "boîte noire"')
st.markdown("On reproche à tous les réseaux de neurones, CNN inclus, de proposer des prédictions sans pouvoir justifier les résultats obtenus. Comme un tour de magie à l'intérieur d'une boîte obscure. Dans le cas de systèmes critiques, tels les véhicules autonomes, il est souhaitable d'avoir des explications interprétables par l'homme. Heureusement, les progrès de la recherche en saillence visuelle (ce qui nous saute aux yeux) permettent progressivement de mieux comprendre comment la vision fonctionne, et viennent consolider l'architecture des CNN.")
st.subheader('Le CNN est dépendant de la fiabilité des données')
st.markdown("Si des humains ont failli dans la labellisation des textes, sons ou images servant à l'entraînement, le modèle ne pourra que refléter les biais, erreurs ou ambiguités qui lui ont été transmis.")
st.subheader('Le CNN ne sait pas extrapoler une orientation différente')
st.markdown("Votre modèle est entraîné uniquement avec des lapins de profil ? Eh bien, il ne pourra pas reconnaître un lapin de face.\nD'où l'importance d'une étape appelée Data Augmentation : il faut veiller à varier au maximum le type d'images que le modèle reçoit en entrée.")
st.subheader('Les probabilités sont à prendre avec des pincettes')
st.markdown("Un CNN obtient souvent des scores remarquables pour la classification, mais quand il s'agit d'indiquer plus précisément la probabilité que tel objet appartienne à telle ou telle classe, les chercheurs ont constaté des résultats illogiques pour un être humain : une modification à peine perceptible à l'oeil nu peut entraîner une grande variation de probabilité. La machine semble exagérément sensible à l'illumination d'une image ou à la taille de l'objet à détecter.")
st.subheader('Le CNN réclame des ressources importantes')
st.markdown("Il faut des millions d'images pour qu'un réseau parvienne à dériver des informations pertinentes à partir des couleurs, textures, formes... C'est pourquoi la mise à disposition en open source des modèles pré-entraînés est cruciale pour notre neutralité carbone. Il convient aussi de s'assurer que le CNN représente la solution la mieux adaptée en fonction des bénéfices attendus.")

# Sous-partie expliquant les cas d'usage
st.header("Cas d'usage")
st.markdown("Parmi les multiples applications, on peut citer des examples dans des domaines très variés, de la santé à l'environnement, en passant par le commerce de détail et l'impression 3D :")
image = Image.open('images/300px-Tumor_Mesothelioma2_legend.jpg')
st.image(image, caption="Classification des cancers")
image = Image.open('images/1024px-Starr_071024-9740_Caladium_bicolor.jpg')
st.image(image, caption="Reconnaissance des plantes poisonneuses")
image = Image.open('images/Amazon_Go_in_Seattle,_December_2016.jpg')
st.image(image, caption="Magasin sans caisse Amazon Go")
image = Image.open('images/3D_failure.jpg')
st.image(image, caption="Impression 3 D : différents types d'échecs")
