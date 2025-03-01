# # -*- coding: utf-8 -*-
# """
# Created on Sat Mar  1 02:21:41 2025

# @author: LDIN
# """

# import numpy as np
# import pickle
# import streamlit as st
# import time

# # Load trained model
# loaded_model = pickle.load(open('D:/Misbah/PICT STUDY/ML_DP/trained_model.sav', 'rb'))

# def diabetes_pred(input_data):
#     input_data_as_numpy_array = np.asarray(input_data, dtype=np.float64)  # Convert input to float
#     input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    
#     prediction = loaded_model.predict(input_data_reshaped)
    
#     if prediction[0] == 0:
#         return 'The person is not diabetic'
#     else:
#         return 'The person is diabetic'


# def main():
#     st.title('Diabetes Prediction WebApp')
    
#     # User Input using sliders
#     Pregnancies = st.slider('Number of Pregnancies', 0, 15, 1)
#     Glucose = st.slider('Glucose level', 50, 200, 100)
#     BloodPressure = st.slider('Blood Pressure value', 30, 140, 80)
#     SkinThickness = st.slider('Skin Thickness value', 0, 99, 20)
#     Insulin = st.slider('Insulin level', 0, 900, 30)
#     BMI = st.slider('Body Mass Index (BMI)', 10.0, 50.0, 25.0)
#     DiabetesPedigreeFunction = st.slider('Diabetes Pedigree Function', 0.0, 2.5, 0.5)
#     Age = st.slider('Patient Age', 10, 100, 30)
    
#     diagnosis = ''
    
#     if st.button('Diabetes Test Result'):
#         with st.spinner('Analyzing...'):
#             time.sleep(2)  # Simulate processing time
#             diagnosis = diabetes_pred([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
    
#     st.success(diagnosis)

# if __name__ == '__main__':
#     main()


#---------------------------------------

import numpy as np
import pickle
import streamlit as st
import matplotlib.pyplot as plt
import time

# Load trained model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

def diabetes_pred(input_data):
    input_data_as_numpy_array = np.asarray(input_data, dtype=np.float64)  # Convert input to float
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    return 'The person is **diabetic**' if prediction[0] == 1 else 'The person is **not diabetic**'

# def set_bg_style():
#     st.markdown(
#         """
#         <style>
#         .stApp {
#             background-color: #f0f2f6;
#         }
#         .stTextInput, .stButton, .stNumberInput {
#             border-radius: 10px;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )
    
def set_dark_theme():
    dark_theme_css = """
    <style>
        /* Background and text colors */
        body, .stApp {
            background-color: #121212 !important;
            color: #ffffff !important;
        }
        /* Sidebar */
        .st-emotion-cache-1gulkj5 {  
            background-color: #1E1E1E !important;
        }
        /* Input boxes */
        .stTextInput, .stNumberInput, .stSelectbox, .stSlider {
            background-color: #333 !important;
            color: #ffffff !important;
        }
        /* Headers */
        h1, h2, h3, h4, h5, h6, label, span, p {
            color: #ffffff !important;
        }
        /* Button */
        .stButton>button {
            background-color: #6200EE !important;
            color: white !important;
            border-radius: 10px;
            border: none;
        }
        /* Graph background */
        .stPlotlyChart, .stAltairChart, .stImage, .stMarkdown {
            background-color: #222 !important;
        }
    </style>
    """
    # st.markdown(dark_theme_css, unsafe_allow_html=True)
#     st.markdown(
#     "<h1 style='color: #ffffff; font-size: 32px;'>🩺 Diabetes Prediction WebApp</h1>", 
#     unsafe_allow_html=True
# )


# Call this function at the top of your main function



def main():
    # set_bg_style()
    # st.image("diabetes_banner.jpg", use_container_width=True)
    st.image("diab1.jpeg", use_container_width=True)
    
    set_dark_theme()
    st.title('🩺 Diabetes Prediction WebApp')
    
    # Sidebar
    st.sidebar.title("🔧 Settings")
    st.sidebar.info("Adjust your inputs and run the test.")
    
    col1, col2 = st.columns(2)
    with col1:
        Pregnancies = st.number_input('Pregnancies', min_value=0, max_value=15, step=1)
        Glucose = st.number_input('Glucose level', min_value=50, max_value=200)
        BloodPressure = st.number_input('Blood Pressure', min_value=30, max_value=180)
    
    with col2:
        SkinThickness = st.number_input('Skin Thickness', min_value=0, max_value=99)
        Insulin = st.number_input('Insulin Level', min_value=0, max_value=900)
        BMI = st.number_input('BMI', min_value=10.0, max_value=50.0, format="%.2f")
    
    DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=2.5, format="%.3f")
    Age = st.number_input('Age', min_value=10, max_value=100, step=1)
    
    diagnosis = ''
    if st.button('🧪 Run Diabetes Test', help="Click to Predict"):
        with st.spinner('Analyzing...'):
            time.sleep(2)  # Simulate processing time
            diagnosis = diabetes_pred([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
    
    st.success(diagnosis)
    
    # Data Visualization
    # plt.style.use("dark_background")
    # fig, ax = plt.subplots()
    # ax.bar(["Glucose", "Blood Pressure", "BMI"], [Glucose, BloodPressure, BMI], color=['blue', 'red', 'green'])
    # ax.set_ylabel("Values")
    # st.pyplot(fig)
    
    
    import matplotlib.pyplot as plt

    # 🔹 Apply dark mode to plots
    plt.style.use("dark_background")  
    
    # Create figure and axes
    fig, ax = plt.subplots()
    
    # Bar chart with custom colors
    ax.bar(["Glucose", "Blood Pressure", "BMI"], [Glucose, BloodPressure, BMI], color=['blue', 'red', 'green'])
    
    # 🔹 Change background color of the figure and axes
    fig.patch.set_facecolor("#121212")  # Dark background for the figure
    ax.set_facecolor("#1E1E1E")         # Dark background for the plot area
    
    # Set labels and colors
    ax.set_ylabel("Values", color="white")  # Make labels visible on dark bg
    ax.tick_params(colors="white")          # Change tick colors to white
    ax.spines['bottom'].set_color("white")  # Change border color
    ax.spines['left'].set_color("white")
    
    # Display in Streamlit
    st.pyplot(fig)

    
if __name__ == '__main__':
    main()
