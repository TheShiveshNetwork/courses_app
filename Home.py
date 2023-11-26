import streamlit as st
from streamlit.components.v1 import html
from strict_output import strict_output
from PIL import Image

st.title(":computer: AI Course Generator")

tab1, tab2 = st.tabs(["General", "Advanced"])

with tab1:
    # INPLEMENT USING PaLM2
    course_name = st.text_input(label="Title", placeholder="Enter title of the course")

    if course_name:
        res = strict_output(course_name)
        st.write(res.result)

with tab2:
    # INPLEMENT USING PaLM2
    course_name = st.text_input(label="Title", placeholder="Enter title of the course", key="adv")

    st.write("This feature is yet to come!")

# with st.columns(3)[1]:
# st.markdown("## AiGen Courses")
st.markdown("### Made with :heart: by")
profile = Image.open('./public/assets/profile.jpeg')
st.image(profile, caption="Shivesh T", width=100)
st.markdown("[![Github](https://img.icons8.com/material-outlined/48/000000/github.png)](https://github.com/TheShiveshNetwork)")

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

        @media(max-width: 533px) {
            iframe[width="220"] {
                position: relative;
                left: 50%;
                bottom: 0;
                transform: translateX(-50%);
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)