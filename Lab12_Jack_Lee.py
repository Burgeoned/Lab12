import streamlit as st
import pandas as pd

##setting up defaults to set to 
df = pd.read_csv('car_data.csv')
transmission_options = ['Manual', 'Automatic']
min_year = 2000 
max_year = 2024  
min_price = 0.0
max_price = 20.0


st.sidebar.header('Filters')

car_name_input = st.sidebar.text_input('Enter Car Name (Optional): ')

transmissions = st.sidebar.multiselect('Select Transmission Type: ', transmission_options, default=transmission_options)

year_range = st.sidebar.slider('Select Year Range: ', min_value=min_year, max_value=max_year, value=(min_year, max_year))

price_range = st.sidebar.slider('Select Selling Price Range: ', min_value=min_price, max_value=max_price, value=(min_price, max_price))



if st.sidebar.button('Apply Filters'): ##if button is clicked
    filtered_data = df.copy()
    ## if to test if user gave inputs
    if car_name_input: 
        filtered_data = filtered_data[filtered_data['Car_Name'].str.contains(car_name_input, case=False)]
    if transmissions:
        filtered_data = filtered_data[filtered_data['Transmission'].isin(transmissions)]
    if year_range: 
        filtered_data = filtered_data[(filtered_data['Year'] >= year_range[0]) & (filtered_data['Year'] <= year_range[1])] ##filtering from paramters set above
    if price_range:
        filtered_data = filtered_data[(filtered_data['Selling_Price'] >= price_range[0]) & (filtered_data['Selling_Price'] <= price_range[1])]

    st.write(filtered_data)
else:
    ##print original data if no filters applied
    st.write(df)