
import streamlit as st
import pandas as pd
import joblib

# =========================================================
# LOAD MODEL
# =========================================================

model = joblib.load(
    r"C:\Users\velis\OneDrive\Desktop\MLProject\mlruns\9\models\m-a0af478a75104a4880ff5307488d8ff4\artifacts\model.pkl"
)

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Phone Addiction Prediction",
    page_icon="📱",
    layout="centered"
)

# =========================================================
# TITLE
# =========================================================

st.title("📱 Phone Addiction Prediction System")

st.write(
    "Fill all details to predict addiction level"
)

# =========================================================
# USER INPUTS
# =========================================================

Name = st.text_input(
    "Name",
    "Roopa"
)

Age = st.number_input(
    "Age",
    min_value=1,
    max_value=100,
    value=22
)

Gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

Location = st.text_input(
    "Location",
    "Hyderabad"
)

Phone_Usage_Purpose = st.selectbox(
    "Phone Usage Purpose",
    [
        "Browsing",
        "Education",
        "Entertainment",
        "Gaming",
        "Social Media",
        "Work"
    ]
)

Daily_Usage_Hours = st.number_input(
    "Daily Usage Hours",
    min_value=0.0,
    max_value=24.0,
    value=6.0
)

Sleep_Hours = st.number_input(
    "Sleep Hours",
    min_value=0.0,
    max_value=24.0,
    value=7.0
)

Screen_Time_Before_Bed = st.number_input(
    "Screen Time Before Bed",
    min_value=0.0,
    max_value=10.0,
    value=2.0
)

Phone_Checks_Per_Day = st.number_input(
    "Phone Checks Per Day",
    min_value=0,
    max_value=500,
    value=60
)

Apps_Used_Daily = st.number_input(
    "Apps Used Daily",
    min_value=0,
    max_value=100,
    value=15
)

Time_on_Social_Media = st.number_input(
    "Time on Social Media",
    min_value=0.0,
    max_value=24.0,
    value=3.0
)

Time_on_Gaming = st.number_input(
    "Time on Gaming",
    min_value=0.0,
    max_value=24.0,
    value=1.0
)

Time_on_Education = st.number_input(
    "Time on Education",
    min_value=0.0,
    max_value=24.0,
    value=4.0
)

Exercise_Hours = st.number_input(
    "Exercise Hours",
    min_value=0.0,
    max_value=24.0,
    value=1.0
)

Weekend_Usage_Hours = st.number_input(
    "Weekend Usage Hours",
    min_value=0.0,
    max_value=24.0,
    value=8.0
)

Social_Interactions = st.slider(
    "Social Interactions",
    0,
    10,
    5
)



Anxiety_Level = st.slider(
    "Anxiety Level",
    0,
    10,
    5
)

Depression_Level = st.slider(
    "Depression Level",
    0,
    10,
    5
)

Self_Esteem = st.slider(
    "Self Esteem",
    0,
    10,
    5
)

# =========================================================
# IMPORTANT MODIFICATION
# =========================================================
# Changed to 0-100 because dataset contains %
# =========================================================

Interllectual_Performance = st.slider(
    "Intellectual Performance (%)",
    0,
    100,
    75
)

Family_Communication = st.slider(
    "Family Communication",
    0,
    10,
    5
)


# =========================================================
# PREDICT
# =========================================================

if st.button("Predict Addiction Level"):

    input_data = pd.DataFrame({

        "Name": [Name],

        "Age": [Age],

        "Gender": [Gender],

        "Location": [Location],

        "Daily_Usage_Hours": [Daily_Usage_Hours],

        "Sleep_Hours": [Sleep_Hours],

        "Interllectual_Performance": [Interllectual_Performance],

        "Social_Interactions": [Social_Interactions],

        "Exercise_Hours": [Exercise_Hours],

        "Anxiety_Level": [Anxiety_Level],

        "Depression_Level": [Depression_Level],

        "Self_Esteem": [Self_Esteem],

        "Screen_Time_Before_Bed": [Screen_Time_Before_Bed],

        "Phone_Checks_Per_Day": [Phone_Checks_Per_Day],

        "Apps_Used_Daily": [Apps_Used_Daily],

        "Time_on_Social_Media": [Time_on_Social_Media],

        "Time_on_Gaming": [Time_on_Gaming],

        "Time_on_Education": [Time_on_Education],

        "Phone_Usage_Purpose": [Phone_Usage_Purpose],

        "Family_Communication": [Family_Communication],

        "Weekend_Usage_Hours": [Weekend_Usage_Hours]

    })

    prediction = model.predict(input_data)[0]

    st.success(
        f"Predicted Addiction Level: {prediction:.2f}"
    )

    # =====================================================
    # ADDICTION CATEGORY
    # =====================================================

    if prediction < 3:

        st.info("Low Phone Addiction")

    elif prediction < 6:

        st.warning("Moderate Phone Addiction")

    else:

        st.error("High Phone Addiction")

