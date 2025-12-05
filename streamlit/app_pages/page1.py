import streamlit as st
import pandas as pd
import numpy as np

#print(st.__version__)

def page1_body():
    """
    This function displays the content of Page one.
    """
    

    df = pd.read_csv('../data/penguins_cleaned.csv')
    if st.button('View Data'):
        st.dataframe(df.head())


# st.header("This is a header")
# st.subheader("This is a subheader")
# st.text("This is fixed-width text.")
# st.markdown("**This text is bold using Markdown!**")