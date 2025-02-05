import joblib
import numpy as np
import pandas as pd
import streamlit

MODEL_PATH = 'model2.joblib'
model_data = joblib.load(MODEL_PATH)


def process(age,income_level,awareness,packaging,gender,consume_freq,brand_choice,
                          health_concerns,zone,current_brand,flavor_pref,consume_situations,
                          occupation,preferable_consumption_size,purchase_channel):
    expected_cols = ['cf_ab_score', 'zac_score', 'bsi', 'age_group_encoded',
           'income_levels_encoded', 'health_concerns_encoded',
           'consume_frequency(weekly)_encoded',
           'preferable_consumption_size_encoded', 'gender_M', 'zone_Rural',
           'zone_Semi-Urban', 'zone_Urban', 'occupation_Retired',
           'occupation_Student', 'occupation_Working Professional',
           'current_brand_Newcomer', 'awareness_of_other_brands_2 to 4',
           'awareness_of_other_brands_above 4',
           'reasons_for_choosing_brands_Brand Reputation',
           'reasons_for_choosing_brands_Price',
           'reasons_for_choosing_brands_Quality', 'flavor_preference_Traditional',
           'purchase_channel_Retail Store', 'packaging_preference_Premium',
           'packaging_preference_Simple',
           'typical_consumption_situations_Casual (eg. At home)',
           'typical_consumption_situations_Social (eg. Parties)']

    # Feature Engineering as per model requirements
    cf_ab_score = 1 if consume_freq == "3-4 times" else (2 if consume_freq == "consume_freq" else 3)
    zac_score = (1 if zone == "Rural" else 2 if zone == "Semi-Urban" else 3 if zone == "Urban" else 4) * (
        1 if income_level == "<10L" else 2 if income_level == "10L - 15L" else 3 if income_level == "16L - 25L" else
        4 if income_level == "26L - 35L" else 5)

    bsi = 1 if current_brand != "Established" and brand_choice in ['Price', 'Quality'] else 0

    # Encoding categorical variables
    age_group_encoded = (1 if 26 <= age <= 35 else 2 if 36 <= age <= 45 else
    3 if 46 <= age <= 55 else 4 if 56 <= age <= 70 else 0)

    income_levels_encoded = {"10L - 15L": 0, "16L - 25L": 1, "26L - 35L": 2, "<10L": 3, "> 35L": 4}.get(income_level, 5)
    health_concerns_encoded = {"Low (Not very concerned)": 1, "Medium (Moderately health-conscious)": 2}.get(
        health_concerns, 0)
    consume_frequency_encoded = {"3-4 times": 1, "5-7 times": 2}.get(consume_freq, 0)
    preferable_consumption_size_encoded = {"Medium (500 ml)": 1, "Small (250 ml)": 2}.get(preferable_consumption_size,
                                                                                          0)

    gender_M = 1 if gender == "M" else 0

    zone_Rural, zone_Semi_Urban, zone_Urban = (1, 0, 0) if zone == "Rural" else (0, 1, 0) if zone == "Semi-Urban" else (
    0, 0, 1)
    occupation_Retired, occupation_Student, occupation_Working_Professional = (
        (1, 0, 0) if occupation == "Retired" else
        (0, 1, 0) if occupation == "Student" else
        (0, 0, 1)
    )

    current_brand_Newcomer = 1 if current_brand == "Newcomer" else 0

    awareness_of_other_brands_2_to_4 = 1 if awareness == "2 to 4" else 0
    awareness_of_other_brands_above_4 = 1 if awareness == "More than 4" else 0

    reasons_for_choosing_brands_Brand_Reputation = 1 if brand_choice == "Reputation" else 0
    reasons_for_choosing_brands_Price = 1 if brand_choice == "Price" else 0
    reasons_for_choosing_brands_Quality = 1 if brand_choice == "Quality" else 0

    flavor_preference_Traditional = 1 if flavor_pref == "Traditional" else 0
    purchase_channel_Retail_Store = 1 if purchase_channel == "Retail Store" else 0

    packaging_preference_Premium = 1 if packaging == "Premium" else 0
    packaging_preference_Simple = 1 if packaging == "Simple" else 0

    typical_consumption_situations_Casual = 1 if consume_situations == "Casual (eg. At home)" else 0
    typical_consumption_situations_Social = 1 if consume_situations == "Social (eg. Parties)" else 0


    input_data = pd.DataFrame([[
            cf_ab_score, zac_score, bsi, age_group_encoded, income_levels_encoded, health_concerns_encoded,
            consume_frequency_encoded, preferable_consumption_size_encoded, gender_M, zone_Rural, zone_Semi_Urban,
            zone_Urban, occupation_Retired, occupation_Student, occupation_Working_Professional, current_brand_Newcomer,
            awareness_of_other_brands_2_to_4, awareness_of_other_brands_above_4,
            reasons_for_choosing_brands_Brand_Reputation,
            reasons_for_choosing_brands_Price, reasons_for_choosing_brands_Quality, flavor_preference_Traditional,
            purchase_channel_Retail_Store, packaging_preference_Premium, packaging_preference_Simple,
            typical_consumption_situations_Casual, typical_consumption_situations_Social
        ]], columns=expected_cols)
    print(cf_ab_score, zac_score, bsi, age_group_encoded, income_levels_encoded, health_concerns_encoded,
               consume_frequency_encoded,preferable_consumption_size_encoded, gender_M)

    return input_data


def predict_result(input_data):
    #streamlit.dataframe(input_data)
    output = model_data["model"].predict(input_data)
    if output == 0:
        return "50 to 100"
    elif output == 1:
        return '100-150'
    elif output == 2:
        return '150-200'
    elif output == 3:
        return '200-250'




def predict(age,income_level,awareness,packaging,gender,consume_freq,brand_choice,
                          health_concerns,zone,current_brand,flavor_pref,consume_situations,
                          occupation,preferable_consumption_size,purchase_channel):
    input_df = process(age, income_level, awareness, packaging, gender, consume_freq, brand_choice,
            health_concerns, zone, current_brand, flavor_pref, consume_situations,
            occupation, preferable_consumption_size, purchase_channel)
    predicted_price = predict_result(input_df)
    return predicted_price
