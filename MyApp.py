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
         
df = pd.read_excel("Data/ahrefs_klint.xlsx")


