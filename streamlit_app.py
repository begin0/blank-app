import streamlit as st
from PIL import Image

# Set up the title and header
st.title("Rekomendasi Smartwatch Kece")

# Image Slider (Carousel)
st.subheader("Smartwatch Gallery")
carousel_images = ["assets/images/1.jpg", "assets/images/2.jpg", "assets/images/3.jpg", "assets/images/4.jpg", "assets/images/5.jpg"]

# Display images in a carousel-like manner
for i in range(0, len(carousel_images), 1):
    image = Image.open(carousel_images[i])
    st.image(image, caption=f"Smartwatch {i+1}", use_column_width=True)

# Selection Form
st.subheader("Pilih Kriteria Smartwatch Impianmu")

# Create a form using Streamlit widgets
with st.form(key='smartwatch_form'):
    merk = st.selectbox("Merk", ['Terkenal', 'Tidak Terkenal'])
    battery_life = st.selectbox("Ketahanan Baterai", ['Tidak Tahan Lama', 'Sedang', 'Tahan Lama'])
    screen_size = st.selectbox("Ukuran Layar", ['Kecil', 'Sedang', 'Besar'])
    water_resistance = st.selectbox("Ketahanan Air", ['Tidak', 'Tahan Cipratan', 'Tahan Air'])
    screen_type = st.selectbox("Tipe Layar", ['Biasa', 'Bagus', 'Sangat Bagus'])
    budget = st.number_input("Harga", min_value=0, label="Tulis anggaran keuangan anda")
    
    # Checkbox for additional features
    gps = st.checkbox("GPS", value=True)
    nfc = st.checkbox("NFC", value=True)
    heart_rate_monitor = st.checkbox("Detak Jantung", value=True)
    bluetooth_call = st.checkbox("Bluetooth Call", value=True)
    wifi = st.checkbox("Wifi", value=True)
    sim_card = st.checkbox("SIM Card", value=True)
    
    submit_button = st.form_submit_button(label="Cari")
    
    if submit_button:
        st.write("Form Submitted! Implement your recommendation logic here.")

# Recommendations Section (you would typically get this from your logic or API)
if submit_button:
    # Example recommendations data (replace with actual dynamic data from your backend or logic)
    recommendations = [
        {
            "Brand": "Brand A",
            "Model": "Model 1",
            "OS": "WearOS",
            "Display": "AMOLED",
            "Connectivity": "WiFi, Bluetooth",
            "Heart Rate Monitor": "Yes",
            "GPS": "Yes",
            "Price": "Rp. 2,000,000"
        },
        {
            "Brand": "Brand B",
            "Model": "Model 2",
            "OS": "Tizen",
            "Display": "LCD",
            "Connectivity": "Bluetooth",
            "Heart Rate Monitor": "No",
            "GPS": "No",
            "Price": "Rp. 1,500,000"
        }
    ]

    st.subheader("Rekomendasi Smartwatch Impianmu")
    for rec in recommendations:
        st.write(f"**{rec['Brand']} - {rec['Model']}**")
        st.write(f"**Operating System:** {rec['OS']}")
        st.write(f"**Screen Type:** {rec['Display']}")
        st.write(f"**Connectivity:** {rec['Connectivity']}")
        st.write(f"**Heart Rate Monitor:** {rec['Heart Rate Monitor']}")
        st.write(f"**GPS:** {rec['GPS']}")
        st.write(f"**Price:** {rec['Price']}")
        
        st.button("Beli")

# Footer
st.markdown("---")
st.markdown("Tugas Mata Kuliah Kecerdasan Buatan © 2024 by Gino Erman Agusta | 24051640005")
