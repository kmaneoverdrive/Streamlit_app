# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st

st.write("""
         # My first app
         Hello *World!*
         """)

user_input = st.text_input("Please enter your username", nameless)

st.write("Hello " + user_input + "!")
