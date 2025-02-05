import streamlit as st
from prediction_helper import predict
# Streamlit UI
st.set_page_config(page_title="CodeX Beverage: Price Prediction", layout="wide")

st.markdown("<h1 style='text-align: center;'>CodeX Beverage: Price Prediction</h1>", unsafe_allow_html=True)

# Create three-column layout
col1, col2, col3, col4 = st.columns(4)

with col1:
    age = st.number_input("Age", min_value=18, max_value=100, value=30, step=1)
    income_level = st.selectbox("Income Level (In L)", ['<10L', '10L - 15L', '16L - 25L', '26L - 35L', '> 35L','Not Reported'])
    awareness = st.selectbox("Awareness of other brands", ["0 to 1", "2 to 4", "More than 4"])
    packaging = st.selectbox("Packaging Preference", ['Simple', 'Premium', 'Eco-Friendly'])

with col2:
    gender = st.selectbox("Gender", ["M", "F"])
    consume_freq = st.selectbox("Consume Frequency (weekly)", ['3-4 times', '5-7 times', '0-2 times'])
    brand_choice = st.selectbox("Reasons for choosing brands", ['Price', 'Quality', 'Availability', 'Brand Reputation'])
    health_concerns = st.selectbox("Health Concerns", ['Medium (Moderately health-conscious)', 'Low (Not very concerned)',
       'High (Very health-conscious)'])

with col3:
    zone = st.selectbox("Zone", ['Urban', 'Metro', 'Rural', 'Semi-Urban'])
    current_brand = st.selectbox("Current Brand", ['Newcomer', 'Established'])
    flavor_pref = st.selectbox("Flavor Preference", ['Traditional', 'Exotic'])
    consume_situations = st.selectbox("Typical Consumption Situations", ['Active (eg. Sports, gym)', 'Social (eg. Parties)',
       'Casual (eg. At home)'])

with col4:
    occupation = st.selectbox("Occupation", ['Working Professional', 'Student', 'Entrepreneur', 'Retired'])
    preferable_consumption_size = st.selectbox("Preferable Consumption Size", ['Medium (500 ml)', 'Large (1 L)', 'Small (250 ml)'])
    purchase_channel = st.selectbox("Purchase Channel", ['Online', 'Retail Store'])



# Button
if st.button("Calculate Price Range"):
    price_range = predict(age,income_level,awareness,packaging,gender,consume_freq,brand_choice,
                          health_concerns,zone,current_brand,flavor_pref,consume_situations,
                          occupation,preferable_consumption_size,purchase_channel)
    st.success("Price Range => " + price_range)

