import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# Load the trained model
model = joblib.load('Dimas.joblib')

# Load mapped data
mapped_data = pd.read_csv("trans_data.csv")
st.title("Hello geiss,welcome")

# Buat label encoder
label_encoders = {}
for column in transformData.columns:
    le = LabelEncoder()
    transformData[column] = le.fit_transform(transformData[column])
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
# Create selectbox for each feature
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
        
# Streamlit UI
def main():
    # Page title
    st.title('Gender Prediction App')

    # Input fields
    age = st.slider('Age', min_value=18, max_value=100, value=30, step=1)
    income = st.number_input('Income', value=50000)
    family_size = st.number_input('Family Size', value=2)
    education = st.selectbox('Education', ['High School', 'Bachelor', 'Master', 'PhD'])

    # Predict button
    if st.button('Predict Gender'):
        # Make prediction
        prediction = predict_gender(age, income, family_size, education)
        st.write(f'The predicted gender is: {prediction}')

# Run the app
if __name__ == '__main__':
    main()
