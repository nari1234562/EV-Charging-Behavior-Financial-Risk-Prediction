import streamlit as st
import pickle
import numpy as  np
import pandas as pd

with open("model.pkl","rb") as file:
    model=pickle.load(file)
    
    
    
st.title("EV Charging Behavior & Financial Risk Prediction")  


# Numerical


City_Tier=st.number_input("City_Tier",min_value=0,max_value=100)
EV_Type=st.number_input("EV_Type",min_value=0,max_value=100),
Battery_Capacity_kWh=st.number_input("Battery_Capacity_kWh",min_value=0,max_value=100),
Charging_Sessions_Per_Month=st.number_input("Charging_Sessions_Per_Month",min_value=0,max_value=100),
Avg_Charge_Cost=st.number_input("Avg_Charge_Cost",min_value=0,max_value=100),
Distance_Travelled_Per_Month=st.number_input("Distance_Travelled_Per_Month",min_value=0,max_value=100),
Tenure_Months=st.number_input("Tenure_Months",min_value=0,max_value=100),
App_Usage_Score=st.number_input("App_Usage_Score",min_value=0,max_value=100),
Charging_Time_Minutes=st.number_input("Charging_Time_Minutes",min_value=0,max_value=100),
Charging_Efficiency_Index=st.number_input("Charging_Efficiency_Index",min_value=0,max_value=100)

# categoricall

Charging_Location_Type=st.selectbox("Charging_Location_Type",['Public', 'Highway', 'Private'])
Charger_Working_Status=st.selectbox("Charger_Working_Status",['Working', 'Not Working'])

input=pd.DataFrame({
    "City_Tier":[City_Tier],
    "EV_Type":[EV_Type],
    "Battery_Capacity_kWh":[Battery_Capacity_kWh],
    "Charging_Sessions_Per_Month":[Charging_Sessions_Per_Month],
    "Avg_Charge_Cost":[Avg_Charge_Cost],
    "Distance_Travelled_Per_Month":[Distance_Travelled_Per_Month],
    "Tenure_Months":[Tenure_Months],
    "App_Usage_Score":[App_Usage_Score],
    "Charging_Time_Minutes":[Charging_Time_Minutes],
    "Charging_Efficiency_Index":[Charging_Efficiency_Index],
    "Charging_Location_Type":[Charging_Location_Type],
    "Charger_Working_Status":[Charger_Working_Status]
    })


if st.button("Predict  Risk "):
    
    probability = model.predict(input)[0][1]

    
    if probability == 1:
        st.succes(" No Risk")
    else:
        st.error(" Risk")




