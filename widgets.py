import streamlit as st
import pandas as pd

# Text Input
name = st.text_input("Your Name Is:")
if name: 
    st.write(f'Hello,{name}')

# Slider
age = st.slider("Select Your Age:",0,100,25)
if age:
    st.write(f'Your Age Is:{age}')

# Select Box 
choices = ["Python","Java","Javascript"]

lang = st.selectbox('Favorite Programming language',choices)

if lang:
    st.write(f'Favorite Programming Language is {lang}')


# File Uploader
file = st.file_uploader('Choose a CSV file','csv')

if file:
    data = pd.read_csv(file)
    st.write(data)