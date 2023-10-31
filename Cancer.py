import pickle
import streamlit as st

model = pickle.load(open('Cancer.sav', 'rb'))

st.title('Estimasi Cancer')

index = st.number_input('Masukan Input 1')
Age = st.number_input('Masukan Input 2')
Gender = st.number_input('Masukan Input 3')
AirPollution = st.number_input('Masukan Input 4')
Alcoholuse = st.number_input('Masukan Input 5')
DustAllergy = st.number_input('Masukan Input 6')
OccuPationalHazards = st.number_input('Masukan Input 7')
GeneticRisk = st.number_input('Masukan Input 8')
chronicLungDisease = st.number_input(
    'Masukan 9')


predict = ''

if st.button(' Estimasi Cancer'):
    predict = model.predict(
        [[index, Age ,Gender, AirPollution, Alcoholuse, DustAllergy, OccuPationalHazards, GeneticRisk, chronicLungDisease]]
    )
    st.write('Estimasi Cancer : ', predict)
    st.write('Estimasi Cancer Keseluruhan: ', predict*3000)
