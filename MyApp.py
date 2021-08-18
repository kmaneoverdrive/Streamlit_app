# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Imports
import pandas as pd
import streamlit as st
import os
import numpy as np
cwd = os.getcwd()
cwd

# Hello world attempt
st.write("""
         # My first app
         Hello *World!*
         """)

# Getting the user name
user_input = st.text_input("Please enter your username", "nameless")

# Saying hello to the user
st.write("Hello " + user_input + "!")

# File download experiment
def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}">Download csv file</a>'
         
df = pd.read_excel("Data/ahrefs_klint.xlsx")

get_table_download_link(df)
