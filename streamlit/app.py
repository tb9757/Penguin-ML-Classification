import streamlit as st
import pandas as pd
import numpy as np

#print(st.__version__)

st.title("Palmers Penguins ML Classification Example")
# st.header("This is a header")
# st.subheader("This is a subheader")
# st.text("This is fixed-width text.")
# st.markdown("**This text is bold using Markdown!**")

df = pd.read_csv('../data/penguins_cleaned.csv')

st.dataframe(df)