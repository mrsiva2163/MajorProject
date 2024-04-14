import streamlit as st
import joblib

st.title("Tri View Dashboard: Insights Across Dimensions")
tab1, tab2, tab3 = st.tabs(["Crop Recommendation", "Fertiliser Prediction", "Yield Prediction"])

model = joblib.load("model1.pkl")
model2=joblib.load("model2.pkl")
# model3=joblib.load("model3.pkl")
soil_type_dict = {'Black': 0, 'Clayey': 1, 'Loamy': 2, 'Red': 3, 'Sandy': 4}
yield_prediction_dict={
    'Tamil Nadu':'./'
}
# Dictionary mapping crop types to indices
crop_type_dict = {'Barley': 0, 'Cotton': 1, 'Groundnut': 2, 'Maize': 3, 'Millets': 4, 'Oil seeds': 5, 'Paddy': 6,
                  'Pulses': 7, 'Sugarcane': 8, 'Tobacco': 9, 'Wheat': 10}
with tab1:
    st.header("Crop Recommendation System")
    N = st.number_input('N (Nitrogen)', min_value=0.0, value=0.0, step=1.0, key='crop_N')
    P = st.number_input('P (Phosphorus)', min_value=0.0, value=0.0, step=1.0, key='crop_P')
    K = st.number_input('K (Potassium)', min_value=0.0, value=0.0, step=1.0, key='crop_K')
    temperature = st.number_input('Temperature (°C)', value=0.0, key='crop_temp')
    humidity = st.number_input('Humidity (%)', value=0.0, key='crop_humidity')
    ph = st.number_input('pH Level', value=0.0, max_value=14.0, step=0.1, key='crop_ph')
    rainfall = st.number_input('Rainfall (mm)', value=0.0, key='crop_rainfall')
    all_fields_filled = not(N == 0.0 and P == 0.0 and K == 0.0 and temperature == 0.0 and humidity == 0.0 and rainfall < 100.0)
    button = st.button("Predict Crop")

    if button:
        if all_fields_filled:
            prediction = model.predict([[N, P, K, temperature, humidity, ph, rainfall]])
            st.write(f"The recommended crop is {prediction[0]}")
        else:
            st.write("Please fill all the values to get the recommendation")

with tab2:
    st.header("Fertiliser Prediction System")
    temperature2 = st.number_input('Temperature (°C)', value=0.0, key='fertilizer_temp')
    humidity2 = st.number_input('Humidity (%)', value=0.0, key='fertilizer_humidity')
    soil_type2 = st.selectbox('Soil Type', ('Black', 'Clayey', 'Loamy', 'Red', 'Sandy'), key='fertilizer_soil')
    crop_type2 = st.selectbox('Crop Type', ('Barley', 'Cotton', 'Groundnut', 'Maize', 'Millets', 'Oil seeds', 'Paddy', 'Pulses', 'Sugarcane','Tobacco', 'Wheat'), key='fertilizer_crop')
    N2 = st.number_input('N (Nitrogen)', min_value=0.0, value=0.0, step=1.0, key='fertilizer_N')
    P2 = st.number_input('P (Phosphorus)', min_value=0.0, value=0.0, step=1.0, key='fertilizer_P')
    K2 = st.number_input('K (Potassium)', min_value=0.0, value=0.0, step=1.0, key='fertilizer_K')
    all_fields_filled2 = not(N2 == 0.0 and P2 == 0.0 and K2 == 0.0 and humidity2 == 0.0 and temperature2 == 0.0)
    if st.button("Predict Fertiliser"):
        if all_fields_filled2:
            prediction=model2.predict([[temperature2, humidity2,75, soil_type_dict[soil_type2], crop_type_dict[crop_type2], N2, P2, K2]])
            st.write("Fertilizer Type: ", prediction[0])
        else:
            st.write("Please fill all the values for fertilizer prediction.")

with tab3:
    st.header("Yield Prediction System")
    
    state = st.selectbox('State', ('Tamil Nadu', 'Karnataka', 'Kerala', 'Andhra Pradesh', 'Telangana'), key='yield_state')
    district = st.selectbox('District', ('Chennai', 'Coimbatore', 'Madurai', 'Salem', 'Trichy'), key='yield_district')
    crop = st.selectbox('Crop', ('Barley', 'Cotton', 'Groundnut', 'Maize', 'Millets', 'Oil seeds', 'Paddy', 'Pulses', 'Sugarcane','Tobacco', 'Wheat'), key='yield_crop')
    crop_season=st.selectbox('Crop Season', ('Kharif', 'Rabi', 'Summer', 'Winter'), key='yield_season')
    area=st.number_input('Area', min_value=0.0, value=0.0, step=1.0, key='yield_area')
    all_fields_filled3 = not(state == '' and district == '' and crop == '' and crop_season == '')
    if st.button("Predict Yield"):
        if all_fields_filled3:
            # prediction=model3.predict([[district,crop_season,crop,area]])
            st.write("Yield:" )
        else:
            st.write("Please fill all the values for yield prediction.")
    
