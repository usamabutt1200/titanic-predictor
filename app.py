import streamlit as st
import joblib
import pandas as pd

# Model load karein
model = joblib.load('decision_tree_titanic.pkl')

st.title("🚢 Titanic Survival Predictor")
st.write("Passenger ki details enter karein taake prediction ki ja sakay:")

# User inputs
pclass = st.selectbox("Ticket Class (Pclass)",)
sex = st.selectbox("Sex", ["Male", "Female"])
age = st.slider("Age", 0, 100, 28)
sibsp = st.number_input("Siblings/Spouses Aboard (SibSp)", 0, 10, 0)
parch = st.number_input("Parents/Children Aboard (Parch)", 0, 10, 0)
fare = st.number_input("Ticket Fare", 0.0, 500.0, 32.0)
embarked = st.selectbox("Port of Embarkation", ["S", "C", "Q"])

# Format inputs for model
sex_male = 1 if sex == "Male" else 0
embarked_Q = 1 if embarked == "Q" else 0
embarked_S = 1 if embarked == "S" else 0

input_data = pd.DataFrame([{
    'Pclass': pclass, 'Age': age, 'SibSp': sibsp, 'Parch': parch, 'Fare': fare,
    'Sex_male': sex_male, 'Embarked_Q': embarked_Q, 'Embarked_S': embarked_S
}])

if st.button("Predict Survival"):
    prediction = model.predict(input_data)
    if prediction == 1:
        st.success("🎉 Passenger bach jayega! (Survived)")
    else:
        st.error("💀 Passenger nahi bach sakay ga. (Not Survived)")
