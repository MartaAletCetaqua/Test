import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

st.write(f"<h1 style='text-align: center; color: #ffffff; background-color:#7d9ac9;'>Results</h1>", unsafe_allow_html=True)
dataframe = pd.DataFrame(
    np.random.randn(10, 10),
    columns=('col %d' % i for i in range(10)))
st.table(dataframe)

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)

df = px.data.iris()
fig = px.scatter(
    df,
    x="sepal_width",
    y="sepal_length",
    color="sepal_length",
    color_continuous_scale="reds",
)
st.plotly_chart(fig, theme="streamlit", use_container_width=True)