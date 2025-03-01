# -*- coding: utf-8 -*-
"""
Created on Sat Mar  1 01:16:49 2025

@author: LDIN
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('D:/Misbah/PICT STUDY/ML_DP/trained_model.sav', 'rb'))

#creating a function for prediciton

def diabetes_pred(input_data):
    
    input_data_as_numpy_array = np.asarray(input_data)
    
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    
    print(prediction)

    if prediction[0] == 0:
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'


def main():
    
    #giving title 
    st.title('Diabetes Prediction WebApp')
    
    #getting ip data from the user to pass on later
    
    # Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome
    
    Pregnancies=st.text_input('Number of Pregnancies')
    Glucose=st.text_input('Glucose level')
    BloodPressure=st.text_input('Blood Pressure value')
    SkinThickness=st.text_input(' Skin Thickness value')
    Insulin=st.text_input('Insulin level')
    BMI=st.text_input('Body Mass Index value ')
    DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function')
    Age=st.text_input('Patient Age')
    
    
    

    
    #code for prediciton 
    diagnosis='' #null string
    
    #creating button for prediciton
    
    if st.button('Diabetes Test Result'):
        diagnosis=diabetes_pred([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
    st.success(diagnosis)
    
if __name__=='__main__':
    main()
        
    
    
    
    
    
    
    
    
    