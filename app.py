import streamlit as st
import joblib
import time

# init
color_selected = None
music_genre_selected = None
beverage_selected = None
soft_drink_selected = None
predicted_rest = None
predicted_value=None

#map
color_op = ('Cool', 'Neutral', 'Warm')
music_genre_op = ('Rock', 'Hip hop', 'Folk/Traditional', 'Jazz/Blues', 'Pop', 'Electronic','R&B and soul')
beverage_op = ('Vodka', 'Wine', 'Whiskey',"Doesn't drink",'Beer', 'Other')
soft_drink_op = ('7UP/Sprite', 'Coca Cola/Pepsi','Fanta','Other')

color_map = {'Cool': 1, 'Neutral': 2, 'Warm': 3}
music_genre_map = {
    'Rock': 1, 
    'Hip hop': 2, 
    'Folk/Traditional': 3, 
    'Jazz/Blues': 4,
    'Pop': 5,
    'Electronic': 6,
    'R&B and soul': 7,
}
beverage_map = {
    'Vodka' : 1, 
    'Wine' : 2, 
    'Whiskey' : 3,
    "Doesn't drink" : 4,
    'Beer': 5, 
    'Other' : 6
}
soft_drink_map = {
    '7UP/Sprite': 1, 
    'Coca Cola/Pepsi': 2,
    'Fanta': 3,
    'Other' : 4
}

# Muat model
model = joblib.load('Gender_Prediction_Logistic_Regression_Model.pkl')

# Tampilkan judul aplikasi
st.title('Gender Prediction App')

# Tambahkan input untuk fitur-fitur yang diperlukan
col1, col2 = st.columns(2)
with col1:
    fav_color = st.selectbox(
    "Favorite Color",
    color_op,
    index=None,
    placeholder="Select Favorite Color...",
    )
    fav_music_genre = st.selectbox(
    "Favorite Music Genre",
    music_genre_op,
    index=None,
    placeholder="Select Favorite Music Genre...",
    )
with col2:
    fav_beverage = st.selectbox(
    "Favorite Beverage",
    beverage_op,
    index=None,
    placeholder="Select Favorite Beverage...",
    )
    fav_soft_drink = st.selectbox(
    "Favorite Soft Drink",
    soft_drink_op,
    index=None,
    placeholder="Select Favorite Soft Drink...",
    )

bt1, bt2, bt3 = st.columns(3)
with bt2:
    if st.button("Predict", type="primary"):
         # Tampilkan animasi loading
        with st.spinner('Sedang memproses...'):
            # Proses yang panjang atau tugas yang memakan waktu
            time.sleep(2)  # Contoh proses yang memakan waktu selama 5 detik

        # Mengubah nilai berdasarkan pilihan yang dipilih
        if fav_color in color_map:
            color_selected = color_map[fav_color]
        if fav_music_genre in music_genre_map:
            music_genre_selected = music_genre_map[fav_music_genre]
        if fav_beverage in beverage_map:
            beverage_selected = beverage_map[fav_beverage]
        if fav_soft_drink in soft_drink_map:
            soft_drink_selected = soft_drink_map[fav_soft_drink]

        predicted_rest = model.predict([[color_selected, music_genre_selected, beverage_selected, soft_drink_selected]])

        if predicted_rest[0] == 1:
            predicted_value = "Female"
            st.title(f':red[{predicted_value}]')
        else:
            predicted_value = "Man"
            st.title(f':blue[{predicted_value}]')
