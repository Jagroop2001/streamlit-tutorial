import streamlit as st
import pandas as pd
import numpy as np

## Writing title in streamlit
st.title("Hello World")

## Display simple text
st.write("Displaying a simple text")

##  Display Dataframe
df = pd.DataFrame({
    "first column":[1,2,3,4],
    "second column": [5,6,7,8]
})

st.write("Displaying a Dataframe")
st.write(df)

## Display Linechart
chart_data = pd.DataFrame(
    np.random.randn(20,4),columns=['a','b','c','d']
)
st.line_chart(chart_data)

