# 1. Import necessary libraries
import streamlit as st
import numpy as np
import joblib

# 2. Load the trained Random Forest model
model = joblib.load('random_forest_monkeypox_model.pkl')

# 3. Define the application
def main():

    # 5. Title of the app
    st.title("Monkeypox Prediction App")

    # 6. Add an informative video
    st.video("https://www.youtube.com/watch?v=s8PAcUYRJdE&ab_channel=TheWallStreetJournal")  # Replace with a valid video URL

    # 7. Explain the two approaches
    st.write("""
    We offer two methods to check if you might have Monkeypox based on symptoms:
    
    - **Survey-style**: A guided approach with Yes/No questions.
    - **Selection Box**: Quickly select from a list of symptoms.

    Please choose your preferred method:
    """)

    # 8. User choice between Survey or Selection Box
    choice = st.radio('Which method would you prefer?', ('Selection Box', 'Survey'))


    # 10. Proceed based on the user's choice
    if choice == 'Survey':
        st.subheader("Survey-style Method")
        st.write("Please answer the following questions.")
        
        symptoms_questions = [
            'Rash', 'Skin lesions', 'Fever', 'Headache', 'Swollen lymph nodes', 'Fatigue', 
            'Loss of appetite', 'Muscle aches', 'Genital ulcers', 'Back pain', 'Cough', 
            'Sore throat', 'Nausea', 'Vomiting', 'Diarrhea', 'Chest pain', 'Abdominal pain', 
            'Shortness of breath', 'Joint pain', 'Conjunctivitis', 'Ear pain', 'Nasal congestion',
            'Bleeding gums', 'Night sweats', 'Dizziness', 'Chills', 'Runny nose', 'Difficulty swallowing',
            'Swelling in arms/legs', 'Blisters', 'Peeling skin', 'Red eyes', 'Dark urine', 'Light stools', 
            'Itchy skin', 'Difficulty breathing', 'Bruising', 'Hearing loss', 'Severe itching', 'Scabs', 
            'Vision loss', 'Dehydration', 'Fever with chills', 'Burning sensation', 'Eye discharge', 
            'Ulcers in mouth'
        ]

        columns = st.columns(3)
        symptom_answers = []
        for i, symptom in enumerate(symptoms_questions):
            col = columns[i % 3]
            answer = col.radio(f"Do you have {symptom.lower()}?", ('No', 'Yes'), index=0)
            symptom_answers.append(answer)
        
        symptoms = np.array(symptom_answers)
        symptoms = np.where(symptoms == 'Yes', 1, 0).reshape(1, -1)  # Convert 'Yes' to 1 and 'No' to 0
    
    elif choice == 'Selection Box':
        st.subheader("Selection Box Method")
        st.write("Please select your symptoms from the list.")

        symptoms_list = [
            'Rash', 'Skin lesions', 'Fever', 'Headache', 'Swollen lymph nodes', 'Fatigue', 
            'Loss of appetite', 'Muscle aches', 'Genital ulcers', 'Back pain', 'Cough', 
            'Sore throat', 'Nausea', 'Vomiting', 'Diarrhea', 'Chest pain', 'Abdominal pain', 
            'Shortness of breath', 'Joint pain', 'Conjunctivitis', 'Ear pain', 'Nasal congestion',
            'Bleeding gums', 'Night sweats', 'Dizziness', 'Chills', 'Runny nose', 'Difficulty swallowing',
            'Swelling in arms/legs', 'Blisters', 'Peeling skin', 'Red eyes', 'Dark urine', 'Light stools', 
            'Itchy skin', 'Difficulty breathing', 'Bruising', 'Hearing loss', 'Severe itching', 'Scabs', 
            'Vision loss', 'Dehydration', 'Fever with chills', 'Burning sensation', 'Eye discharge', 
            'Ulcers in mouth'
        ]
        
        selected_symptoms = st.multiselect('Select your symptoms:', symptoms_list)
        symptoms_input = [1 if symptom in selected_symptoms else 0 for symptom in symptoms_list]
        symptoms = np.array(symptoms_input).reshape(1, -1)  # Convert to numpy array

     # 9. Add an informative image
    st.image("https://th.bing.com/th/id/OIP.j1FMdiLn4LM3Hlvy-kgwdgAAAA?rs=1&pid=ImgDetMain", caption="Symptoms of Monkeypox", use_column_width=True)  # Replace with a valid image URL
    
    # 11. Make prediction if symptoms are provided
    if st.button('Predict'):
        with st.spinner('Predicting...'):
            prediction = model.predict(symptoms)
            prediction_prob = model.predict_proba(symptoms)
            
            if prediction == 1:
                st.error(f"Based on the symptoms, you might have Monkeypox!")
                st.write(f"There's a **{round(prediction_prob[0][1] * 100, 2)}%** chance that you're affected.")
            else:
                st.success(f"You are likely not infected with Monkeypox.")
                st.write(f"There's a **{round(prediction_prob[0][0] * 100, 2)}%** chance that you're not affected.")

# 12. Run the app
if __name__ == '__main__':
    main()
