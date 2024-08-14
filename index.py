import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt

st.title('Streamlit Built-in Charts')

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))


import streamlit as st
import numpy as np

dataf = np.random

dataframe = dataf.randn(10, 10)
st.dataframe(dataframe)

# Streamlit app
st.title('Streamlit Built-in Charts')

# Line chart
st.subheader('Line Chart')
st.line_chart(dataframe)

# Bar chart
st.subheader('Bar Chart')
st.bar_chart(dataframe)

# Area chart
st.subheader('Area Chart')
st.area_chart(dataframe)




# /////////////////////////////////

import streamlit as st
import numpy as np
import pandas as pd

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)



# //////////////////////////////////////


map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

# //////////////////////////////////////
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)




# //////////////////////////////////////
st.text_input("Your name", key="name")
# You can access the value at any point with:
st.session_state.name





import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'



if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])

st.header("Choose a datapoint color")
color = st.color_picker("Color", "#FF0000")
st.divider()
st.scatter_chart(st.session_state.df, x="x", y="y", color=color)