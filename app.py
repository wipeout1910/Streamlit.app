# Import daftar pustaka
import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# Mengambil data dari file .joblib
model = joblib.load('Dimas.joblib')

# Load trans data(import file csv)
trans_data = pd.read_csv("trans_data.csv")
st.title("Hello geiss,welcome")

# Buat label encoder
label_encoders = {}
for column in trans_data.columns:
    le = LabelEncoder()
    trans_data[column] = le.fit_transform(trans_data[column])
    label_encoders[column] = le

color_op = ['Cool', 'Neutral', 'Warm']
music_genre_op = ['Rock', 'Hip hop', 'Folk/Traditional', 'Jazz/Blues', 'Pop', 'Electronic','R&B and soul']
beverage_op = ['Vodka', 'Wine', 'Whiskey',"Doesn't drink",'Beer', 'Other']
soft_drink_op = ['7UP/Sprite', 'Coca Cola/Pepsi','Fanta','Other']

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
# Membuat tampilan dan konfigurasi combo box pada app yang kita buat
favorite_color = st.selectbox('Favorite Color', ['Select']+color_op)
favorite_music_genre = st.selectbox('Favorite Music Genre', ['Select']+music_genre_op)
favorite_beverage = st.selectbox('Favorite Beverage', ['Select']+beverage_op)
favorite_soft_drink = st.selectbox('Favorite Soft Drink', ['Select']+soft_drink_op)

# Tambahkan tombol untuk memicu prediksi

if st.button('Predict'):
    if favorite_color != 'Select' and favorite_music_genre != 'Select' and favorite_beverage != 'Select' and favorite_soft_drink != 'Select':
        favorite_color_numeric = color_map[favorite_color]
        favorite_music_genre_numeric = music_genre_map[favorite_music_genre]
        favorite_beverage_numeric = beverage_map[favorite_beverage]
        favorite_soft_drink_numeric = soft_drink_map[favorite_soft_drink]

        # Prediksi gender berdasarkan nilai numerik
        prediction = model.predict([[favorite_color_numeric, favorite_music_genre_numeric, favorite_beverage_numeric, favorite_soft_drink_numeric]])[0]
        

        # Menampilkan hasil prediksi
        st.write(f"Predicted Gender: {prediction}")
    else:
        st.write("Please select values for all features.")
