import pandas as pd
import numpy as np
import base64
from sklearn.neighbors import NearestNeighbors
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from pathlib import Path
import streamlit as st
from PIL import Image

# Load dataset
data = pd.read_csv("assets/data/sw_dataset_new.csv")

# Features for similarity matching
X = data[['harga', 'merk', 'layar', 'tahan_air', 'jenis_layar', 'ketahanan_baterai', 'gps', 'nfc', 'hrm', 'bt_call', 'wifi', 'simcard']]

# Model for nearest neighbors (unsupervised)
knn = NearestNeighbors(n_neighbors=3, metric='euclidean')
knn.fit(X)

# Load the image
image_path = "assets/logo/logo.jpg"  # Replace with the path to your image
image = Image.open(image_path)

# Convert the image to base64
with open(image_path, "rb") as img_file:
    img_str = base64.b64encode(img_file.read()).decode("utf-8")

# Display the image within a styled div in Streamlit
st.markdown(
    f"""
    <div style="display: flex; justify-content: center; align-items: center; background-color: #021529;">
        <img src="data:image/jpeg;base64,{img_str}" alt="My Image" style="width: 100%; max-width: 300px;"/>
    </div>
    """,
    unsafe_allow_html=True
)

# Function to encode images to base64
def encode_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Path to images
image_folder = Path("assets/images")
image_files = list(image_folder.glob("*.jpg"))  # Adjust to match your image formats, e.g., "*.png"

# Encode images
encoded_images = [encode_image(str(image)) for image in image_files]

#images slider
img_sldr = """
    <style>
        .slider-container {
            max-width: 700px;
            position: relative;
            margin: auto;
        }
        .slide {
            display: none;
        }
        .slide img {
            width: 100%;
            border-radius: 8px;
        }
        .footer {
            text-align: center;
            padding: 20px;
            font-size: 14px;
            color: #555;
            background-color: #ddd;
        }
    </style>
    <div class="slider-container">
    """
for encoded_image in encoded_images:
    img_sldr += f"""
    <div class="slide">
        <img src="data:image/jpeg;base64,{encoded_image}">
    </div>
    """

img_sldr += """
    </div>
    <script>
        let slideIndex = 0;
        function showSlides() {
            let slides = document.getElementsByClassName("slide");
            for (let i = 0; i < slides.length; i++) {
                slides[i].style.display = "none";  
            }
            slideIndex++;
            if (slideIndex > slides.length) {slideIndex = 1}    
            slides[slideIndex-1].style.display = "block";  
            setTimeout(showSlides, 3000); // Change image every 3 seconds
        }
        showSlides();
    </script>
    """

st.components.v1.html(img_sldr, height=350)

#header website
st.markdown('<H2 align="center">Masukkan Kriteria Smartwatch Impianmu</H2>', unsafe_allow_html=True)
optionMerk = {"Terkenal": 1,"Tidak Terkenal": 0}
merk = st.selectbox("Merk", optionMerk)
optionBtr = {'Tidak Tahan Lama':0, 'Sedang':1, 'Tahan Lama':2}
ketahanan_baterai = st.selectbox("Ketahanan Baterai", optionBtr)
optionLyr = {'Kecil':0, 'Sedang':1, 'Besar':2}
layar = st.selectbox("Ukuran Layar", optionLyr)
optionWp = {'Tidak':0, 'Tahan Cipratan':1, 'Tahan Air':2}
waterproof = st.selectbox("Ketahanan Air", optionWp)
optionJlyr = {'Biasa':0, 'Bagus':1, 'Sangat Bagus':2}
jenis_layar = st.selectbox("Tipe Layar", optionJlyr)
harga = st.number_input("Harga", min_value=0, placeholder="Tulis anggaran keuangan anda")
# Feature checkboxes

# Create three columns to arrange the checkboxes
col1, col2, col3, col4, col5, col6 = st.columns(6)

# Place the checkboxes inside the columns
with col1:
    gps = st.checkbox("GPS", value="True")

with col2:
    nfc = st.checkbox("NFC", value="True")

with col3:
    hrm = st.checkbox("Detak Jantung", value="True")

with col4:
    bt_call = st.checkbox("Bluetooth Call", value="True")

with col5:
    wifi = st.checkbox("Wifi", value="True")

with col6:
    sim_card = st.checkbox("SIM Card", value="True")

# Button to find recommendations
if st.button("Cari Rekomendasi"):
    # Encode user inputs for features
    input_data = np.array([
        harga,
        optionMerk[merk],
        optionLyr[layar],
        optionWp[waterproof],
        optionJlyr[jenis_layar],
        optionBtr[ketahanan_baterai],
        int(gps),
        int(nfc),
        int(hrm),
        int(bt_call),
        int(wifi),
        int(sim_card)
    ]).reshape(1, -1)

    # Find the nearest neighbors (closest matches)
    distances, indices = knn.kneighbors(input_data)

    # Get recommendations based on the closest matches
    recommendations = data.iloc[indices[0]]

    # Select only the columns you want to display
    columns_to_display = [
        'Brand', 'OS', 'Model', 'Connectivity', 'harga', 'display_type',
        'display_size_inch', 'water_resistance', 'hrm', 'gps', 'nfc', 'Connectivity', 'bt_call'
    ]
    recommendations = recommendations[columns_to_display]

    # Display recommendations as cards
    st.subheader("Rekomendasi Smartwatch Terbaik untuk Anda:")
    cols = st.columns(3)
    for i, (index,row) in enumerate(recommendations.iterrows()):
        with cols[i]:
            st.markdown(f"""
        <div style="background-color: #f1f1f1; border-radius: 10px; padding: 20px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">
            <img src="https://media.istockphoto.com/id/509464671/id/foto/jam-tangan-pintar.jpg?s=2048x2048&w=is&k=20&c=D7VGT_h4lvxvq5QtRtgmqMqmTVIaZ0XyRBovWVEb61Y=">
            <h4 style="text-align: center; font-size: 18px; font-weight: bold;">{row['Brand']} - {row['Model']}</h4>
            <strong>OS:</strong> {row['OS']}</br>
            <strong>Harga:</strong> Rp {row['harga']:,}</br>
            <strong>Tipe Layar:</strong> {row['display_type']}</br>
            <strong>Ukuran Layar:</strong> {row['display_size_inch']} inchi</br>
            <strong>Ketahanan Air:</strong> {row['water_resistance']} %</br>
            <strong>Detak Jantung:</strong> {'Ya' if row['hrm'] else 'Tidak'}</br>
            <strong>GPS:</strong> {'Ya' if row['gps'] else 'Tidak'}</br>
            <strong>NFC:</strong> {'Ya' if row['nfc'] else 'Tidak'}</br>
            <strong>Pantau Detak Jantung:</strong> {'Ya' if row['hrm'] else 'Tidak'}</br>
            <strong>Konektivitas:</strong> {row['Connectivity']}</br>
            <strong>Bluetooth Call:</strong> {'Ya' if row['bt_call'] else 'Tidak'}</br>
            <p><button href="https://shopee.co.id" style="padding: 5px 10px; background-color: light-blue; border-radius: 5px">Beli</button></p>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown('<div style="text-align: center; background-color: #021529; color: white; padding: 10px 5px;">Tugas Mata Kuliah Kecerdasan Buatan © 2024 by Gino Erman Agusta | 24051640005</div>', unsafe_allow_html=True)
