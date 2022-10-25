import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('Canifornia Housing Data(1990) By Yongchen Zhao')
df = pd.read_csv('housing.csv')


pop_slider = st.slider('Median Housing Price', 0.0, 500001.0, 200000.0)
capital_filter = st.sidebar.multiselect(
     'Choose the location type',
     ['NEAR BAY', '<1H OCEAN', 'INLAND', 'NEAR OCEAN', 'ISLAND'], 
     ['NEAR BAY', '<1H OCEAN', 'INLAND', 'NEAR OCEAN', 'ISLAND'])

genre = st.sidebar.radio(
     'Choose income level',
     ('Low', 'Medium', 'High')
)
if genre == 'Low':
     df = df[df.median_income <= 2.5]
if genre == 'Medium':
     df = df[df.median_income < 4.5]
if genre == 'High':
     df= df[df.median_income > 4.5]

df = df[df.median_house_value >= pop_slider]
df = df[df.ocean_proximity.isin(capital_filter)]


st.subheader('See more filterrs in the sidebar:')
st.map(df)
st.subheader('Histogram of the Median House Value')
fig, ax = plt.subplots(figsize=(8, 6))
df.median_house_value.hist(bins=30)
st.pyplot(fig)
