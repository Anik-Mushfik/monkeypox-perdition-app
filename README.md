
# 🐵 Monkeypox Prediction App

This is a **machine learning-based web application** developed using **Streamlit**. It predicts the likelihood of a person being infected with Monkeypox based on their symptoms. The app leverages a **Random Forest Classifier** trained on 46 symptoms to make predictions.

## 🚀 Features

- **Two Input Methods**:
  1. **Survey-style**: Users answer Yes/No questions about specific symptoms, ensuring thorough symptom entry.
  2. **Selection Box**: Users select their symptoms from a multi-selection box for faster interaction.
  
- **Real-time Prediction**: The app provides an instant prediction, including:
  - Whether the user is likely infected with Monkeypox.
  - The probability (percentage) of infection.

- **Trained Machine Learning Model**: The app uses a pre-trained **Random Forest** model saved as `random_forest_monkeypox_model.pkl` for predictions.

## 🛠️ Installation & Setup

Follow these steps to get the app up and running on your local machine:

### 1. Clone the repository

```bash
git clone https://github.com/your-username/monkeypox-prediction-app.git
cd monkeypox-prediction-app
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

Launch the app using Streamlit:

```bash
streamlit run app.py
```

### 4. Access the app

Once the app is running, it will open in your browser or can be accessed at `http://localhost:8501`.

## 🧭 How to Use the App

### Step 1: Choose Your Input Method
- **Survey-style**: You'll be asked a series of Yes/No questions for each symptom.
- **Selection Box**: You'll select from a list of symptoms that you are currently experiencing.

### Step 2: Enter Symptoms
- Based on your selected input method, fill in your symptoms either by answering questions or selecting symptoms from the list.

### Step 3: Get Prediction
- Press the **Predict** button, and the app will:
  - Indicate whether you are likely infected with Monkeypox.
  - Display the **percentage chance** of infection.

## 📊 Dataset

The model was trained on a dataset containing 46 key symptoms associated with Monkeypox, including:
- Rash
- Skin lesions
- Fever
- Headache
- Swollen lymph nodes
- Muscle aches
- **... and more (46 symptoms in total).**

The full list of symptoms is displayed in the app, allowing for comprehensive input.

## 🔍 Model

The prediction model is a **Random Forest Classifier**. This supervised learning algorithm is well-suited for classification tasks like this, where it determines whether or not a user is infected based on their symptoms.

The trained model (`random_forest_monkeypox_model.pkl`) is loaded in the app and used for real-time predictions.

## 📂 Repository Structure

```
monkeypox-prediction-app/
├── app.py                  # Main Streamlit app
├── random_forest_monkeypox_model.pkl  # Trained model
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation (this file)
```

## ⚡ Requirements

- Python 3.x
- Streamlit
- Scikit-learn
- Numpy
- Joblib

All dependencies can be installed using the `requirements.txt` file.

## 🚀 Future Improvements

- Enhance the UI with animations and better aesthetics.
- Incorporate additional machine learning models for comparison.
- Collect and add more data to improve prediction accuracy.

## 📝 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for any improvements or bug fixes.

## 📧 Contact

For any questions or inquiries, feel free to reach out at `anikmushfik@gmail.com`.

---
