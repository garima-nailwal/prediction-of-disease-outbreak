import os
import pickle # load pre-trained model loading
import streamlit as st    # web app
from streamlit_option_menu import option_menu

# Get the current working directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

st.set_page_config(page_title='Prediction of Disease Outbreaks',layout='wide',page_icon="🧑‍⚕️")
# diabetes_model= pickle.load(open(r"C:\Users\Administrator\Documents\disease_outbreak\saving_models\diabetes_model.sav",'rb'))
# heart_disease_model=pickle.load(open(r"C:\Users\Administrator\Documents\disease_outbreak\saving_models\heart_model.sav",'rb'))
# parkinsons_model= pickle.load(open(r"C:\Users\Administrator\Documents\disease_outbreak\saving_models\parkinsons_model.sav",'rb'))

# Use relative path instead of Windows absolute path
diabetes_model = pickle.load(open(os.path.join(BASE_DIR, "saving_models", "diabetes_model.sav"), "rb"))
heart_disease_model = pickle.load(open(os.path.join(BASE_DIR, "saving_models", "heart_disease_model.sav"), "rb"))
parkinsons_model = pickle.load(open(os.path.join(BASE_DIR, "saving_models", "parkinsons_model.sav"), "rb"))

with st.sidebar:
    selected= option_menu('Prediction of disease outbreak system',
                          ['Diabetes Prediction','Heart Disease Prediction','Parkinsons prediction'],
                          menu_icon='hospital-fill',icons=['activity','heart','person'],default_index=0)

if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies= st.text_input('Number of Pregnancies')
    with col2:
        Glucose= st.text_input('Glucose level')
    with col3:
        Bloodpressure= st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin= st.text_input('Insulin level')
    with col3:
        BMI = st.text_input('BMI  value')
    with col1:
        DiabetesPedigreeFunction= st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age= st.text_input('Age of the person')

    #code for prediction
    diab_diagnosis = ''

    #creating a button for prediction
    if st.button('Diabetes Test Result'):
        user_input=[Pregnancies, Glucose, Bloodpressure, SkinThickness, Insulin,
                        BMI, DiabetesPedigreeFunction, Age]
        user_input= [float(x) for x in user_input]
        diab_prediction= diabetes_model.predict([user_input])
        if diab_prediction[0]==1:
            diab_diagnosis= 'The person is diabetic'
        else:
            diab_diagnosis= 'The person is not diabetic'
    st.success(diab_diagnosis)
    

#for heart disease
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    col1,col2,col3 = st.columns(3)
    with col1:
        age= st.text_input('Age')
    with col2:
        sex= st.text_input('Sex')
    with col3:
        cp= st.text_input('Chest pain types')
    with col1:
        trestbps = st.text_input('Resting blood pressure')
    with col2:
        chol= st.text_input('serum cholestrol in mg/dl')
    with col3:
        fbs = st.text_input('fasting blood sugar > 120mg/dl')
    with col1:
        restecg= st.text_input('Resting electrocardiographic results')
    with col2:
        hr= st.text_input('Maximum heart rate achieved')
    with col3:
        exang= st.text_input('Exercise induced angina')
    with col1:
        oldpeak= st.text_input('ST depression induced by exercise')
    with col2:
        slope= st.text_input('Slope of the peak exercise ST segment')
    with col3:
        ca= st.text_input('Major vessels colored by flourosopy')
    with col1:
        thal= st.text_input('thal: 0 = normal,1= fixed defect,2= reversible defect')
    
    #code for prediction
    heart_diagnosis = ''

    #creating a button for prediction
    if st.button('Heart Disease Test Result'):
        user_input=[age,sex,cp,trestbps,chol,fbs,restecg,hr,exang,oldpeak,slope,ca,thal]
        user_input= [float(x) for x in user_input]
        heart_prediction= heart_disease_model.predict([user_input])
        if heart_prediction[0]==1:
            heart_diagnosis= 'The person is having heart disease'
        else:
            heart_diagnosis= 'The person is not having heart disease'
    st.success(heart_diagnosis)

#for parkinsons disease
if selected == 'Parkinsons prediction':
    st.title('Parkinsons Disease Prediction using ML')
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
       fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
       fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    with col4:
        jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col5:
        jitter_abs= st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')
    with col2:
        PPQ= st.text_input('MDVP:PPQ')
    with col3:
        DDP= st.text_input('Jitter:DDP')
    with col4:
        shimmer= st.text_input('MDVP:Shimmer')
    with col5:
        shimmer_db= st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3= st.text_input('Shimmer:APQ3')
    with col2:
        APQ5= st.text_input('Shimmer:APQ5')
    with col3:
        APQ= st.text_input('MDVP:APQ')
    with col4:
        DDA= st.text_input('Shimmer:DDA')
    with col5:
        NHR= st.text_input('NHR')

    with col1:
        HNR= st.text_input('HNR')
    with col2:
        RPDE= st.text_input('RPDE')
    with col3:
        DFA= st.text_input('DFA')
    with col4:
        spread1= st.text_input('spread1')
    with col5:
        spread2= st.text_input('spread2')

    with col1:
            D2= st.text_input('D2')
    with col2:
            PPE= st.text_input('PPE')
        
    #code for prediction
    parkinsons_diagnosis = ''

    #creating a button for prediction
    if st.button('Parkinsons Disease Test Result'):
        user_input=[fo, fhi,flo,jitter_percent, jitter_abs, 
                    RAP, PPQ, DDP, shimmer, shimmer_db, 
                    APQ3, APQ5, APQ, DDA, NHR,
                    HNR, RPDE, DFA, spread1, spread2,
                    D2, PPE]
        user_input= [float(x) for x in user_input]
        parkinsons_prediction= parkinsons_model.predict([user_input])
        if parkinsons_prediction[0]==1:
            parkinsons_diagnosis= 'The person has parkinsons disease'
        else:
            parkinsons_diagnosis= 'The person does not have parkinsons disease'
    st.success(parkinsons_diagnosis)
