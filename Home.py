import streamlit as st
from streamlit.components.v1 import html
from strict_output import strict_output, advanced_output
from PIL import Image
from markdown import markdown

st.set_page_config(
    page_title="AIGen Courses - Generate Courses with the help of AI",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title(":computer: AI Course Generator")

tab1, tab2 = st.tabs(["General", "Advanced"])

with tab1:
    # INPLEMENT USING PaLM2
    course_name = st.text_input(label="Title", placeholder="Enter title of the course")

    if course_name:
        res = strict_output(course_name)
        if res:
            st.write("""## :laughing: Hurray
                        
                        Your course is Generated Successfully !!!""")
            md_to_html = markdown(res.result)
            st.download_button("Download as html", data=md_to_html, file_name=f"{course_name}.html")
            st.write(res.result)
    else:
        st.warning('Fill up all the fields', icon="⚠️")

with tab2:
    # INPLEMENT USING PaLM2
    course_name = st.text_input(label="Title", placeholder="Enter title of the course", key="adv")
    st.write("#### Units")

    units = st.text_input("Enter custom units/chapters separated by comma", placeholder="format: unit1, unit2, unit3, etc")

    unit_list = units.split(',')

    if course_name and units and unit_list:
        res = advanced_output(course_name, unit_list)
        if res:
            st.write('## Course')
            md_to_html = markdown(res.result)
            st.download_button("Download as html", data=md_to_html, file_name=f"{course_name}.html")
            st.write(res.result)
    else:
        st.warning('Fill up all the fields', icon="⚠️")


# with st.columns(3)[1]:
st.markdown("## AiGen Courses")
b_col1, b_col2 = st.columns(2)
with b_col1:
    st.write('AIGen.Courses is an AI service through which anyone can generate Free Courses with the help of AI and start learning on their oen, using free resources.')
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