
import streamlit as st
import joblib
import pandas as pd

model = joblib.load('model.joblib')

st.title("Titanic Survival Prediction")
st.write("Enter Passenger Details")

pclass = st.selectbox("Passenger Class", [1, 2, 3])
sex = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=1, max_value=100, value=25)
fare = st.number_input("Fare", min_value=0.0, value=50.0)

if st.button("Predict Survival"):

    sex_value = 1 if sex == "Male" else 0

        data = pd.DataFrame(
                [[pclass, sex_value, age, fare]],
                        columns=['pclass', 'sex', 'age', 'fare']
                            )

                                prediction = model.predict(data)

                                    if prediction[0] == 1:
                                            st.success("Passenger Survived!")
                                                else:
                                                        st.error("Passenger Did Not Survive")
