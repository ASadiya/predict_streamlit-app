import streamlit as st 
import joblib 

from pipeline import recode_region 

model = joblib.load("model_pipeline.joblib")

st.title("Modèle de prédiction des primes d'assurances")

sex_map = {
    'Homme': 'male',
    'Femme': 'female'
}

smoker_map = {
    'Oui': 'yes',
    'Non': 'no'
}

region_map = {
    'Nord-Est': 'northeast',
    'Sud-Est': 'southeast',
    'Nord-Ouest': 'northwest',
    'Sud-Ouest': 'southwest'
}


with st.form(key='prediction.form'):
    
    age = st.number_input("Entrez votre âge", min_value=0.0, step=1, format="%.d")
    bmi = st.number_input("Entrez votre indice de masse corporelle", min_value=0.0, format="%.2f")
    children = st.number_input("Entrez le nombre d'enfants couverts par l'assurance maladie ou le nombre de personnes à charge (Entre 0 et 5)", min_value=0.0, step=1, format="%.d")

    sex = st.selectbox("Êtes-vous une femme ou un homme ?", list(sex_map.keys()))
    smoker = st.selectbox("Fumez-vous ?", list(smoker_map.keys()))
    region = st.selectbox("Dans quelle région vivez-vous ?", list(region_map.keys()))

    st.form_submit_button(label="Obtenir votre prédiction")


if submit_button:
    try:

        if age < 0 or age > 200:
            st.error("Entrez un âge valide.")
        if bmi <= 0:
            st.error("\nVotre indice de masse corporelle ne peut pas etre négatif. \nEntrez un indice de masse corporelle valide.")
        if children < 0 or children > 5:
            st.error("Nombre d'enfants ou de personnes à charges compris entre 0 et 5 !")

        else:
            sex = sex_map[sex_display]
            smoker = smoker_map[smoker_display]
            region = region_map[region_display]

            input_data = [[age, sex, bmi, children, smoker, region]]

            prediction = model.predict(input_data)
            st.success(f" Prédiction\nPrime d'assurance maladie: {prediction[0]}")

    except Exception as e:
        st.error(f"Une erreur est survenue: {e}")