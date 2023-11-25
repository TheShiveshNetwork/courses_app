import streamlit as st
from streamlit.components.v1 import html
import google.generativeai as palm
from config import PALM_API_KEY

st.title("AI Course Generator")

palm_api_key = PALM_API_KEY

# st.text_input(label="OpenAI Api", placeholder="Enter your OpenAI API Key")
# INPLEMENT USING PaLM2
course_name = st.text_input(label="Title", placeholder="Enter title")

defaults = {
    'model': 'models/text-bison-001',
    'temperature': 0.7,
    'candidate_count': 1,
    'top_k': 40,
    'top_p': 0.95,
    'max_output_tokens': 1024,
    'stop_sequences': [],
    'safety_settings': [{"category":"HARM_CATEGORY_DEROGATORY","threshold":1},{"category":"HARM_CATEGORY_TOXICITY","threshold":1},{"category":"HARM_CATEGORY_VIOLENCE","threshold":2},{"category":"HARM_CATEGORY_SEXUAL","threshold":2},{"category":"HARM_CATEGORY_MEDICAL","threshold":2},{"category":"HARM_CATEGORY_DANGEROUS","threshold":2}],
}

if course_name:
    palm.configure(api_key=palm_api_key)
    res = palm.generate_text(
        **defaults,
        prompt=course_name
    )

    st.write(res.result)


button = """
<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="mrdevknown404" data-color="#FFDD00" data-emoji=""  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#ffffff" ></script>
"""

html(button, height=70, width=220)

st.markdown(
    """
    <style>
        iframe[width="220"] {
            position: fixed;
            bottom: 60px;
            right: 40px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)