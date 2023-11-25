import streamlit as st
import google.generativeai as palm

st.title("Home Page")

palm_api_key = ""

# st.text_input(label="OpenAI Api", placeholder="Enter your OpenAI API Key")
# INPLEMENT USING PaLM2
course_name = st.text_input(label="Title", placeholder="Enter title")

if course_name:
    palm.configure(api_key=palm_api_key)
    res = palm.chat(messages=[course_name])

    st.write(res.last)
