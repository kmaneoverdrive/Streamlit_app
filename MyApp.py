# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Imports
import streamlit as st

# Hello world attempt
st.write("""
         # My first app
         Hello *World!*
         """)

# Getting the user name
user_input = st.text_input("Please enter your username", nameless)

# Saying hello to the user
st.write("Hello " + user_input + "!")
