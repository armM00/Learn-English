# basic
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Learn English",
                   page_icon="🍏")

df = px.data.iris()

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://pixelify.nyc3.cdn.digitaloceanspaces.com/wp-content/uploads/2020/06/20112726/runnerdesign_2020-3.jpg");
background-size: 130%;
}}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("Learn English")

with st.expander("How to use?"):
    st.info("Usage: \n1. Enter a word you want to explore \n2. Click on the platform  \n3. Click on 'Check' ")

    st.write("""<b><span style='color:yellow;'>Keep in mind:</span> This app doesn't auto-close previously 
    opened tabs.""", unsafe_allow_html=True)

    st.write('<b><span style="color:yellow;">Tip:</span>  You can press <span style="color:green;">Ctrl+W </span>to '
             'close the currently open page.</b><br><b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Also, '
             'you can <span style="color:green;"> Middle click </span> on any tab to close it.<b>',
             unsafe_allow_html=True)

    st.write("""<b><span style="color:red;">Note:</span> If the link doesn't update try to refresh the website<b>""",
             unsafe_allow_html=True)


def new_word():
    the_word = st.session_state["new word"]
    unicode_word = the_word.replace(" ", "%20")
    return unicode_word


st.text_input(label="Enter a word you want to check:",
              placeholder="Swim, read, drink coffee, etc",
              on_change=new_word,
              key="new word")

word = new_word()

st.write('<style>div.row-widget.stButton > button:first-child '
         '{ width: 100%; background-color: #074986; color: #FFFFFF; border-color: #0072C6; } '
         'div.row-widget.stButton > button:first-child:hover { background-color: #005EA2; border-color: #005EA2; } '
         'div.row-widget.stButton > button:first-child:active { background-color: #003B6F; border-color: #003B6F; '
         '}</style>',
         unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.button("Google Translate", key="Google")

    if st.session_state["Google"]:
        if len(new_word()) != 0:
            st.write(f"[Check](https://translate.google.com/?sl=en&tl=vi&text={word})")
        else:
            st.write("Please enter a word")

    st.button("Forvo", key="Forvo")

    if st.session_state["Forvo"]:
        if len(new_word()) != 0:
            st.write(f"[Check](https://forvo.com/word/{word}/#en)")
        else:
            st.write("Please enter a word")

    st.button("Myefe", key="Myefe")
    if st.session_state["Myefe"]:
        if len(new_word()) != 0:
            st.write(f"[Check](https://myefe.com/transcription-pronunciation/{word})")
        else:
            st.write("Please enter a word")

with col2:
    st.button("Cambridge Dictionary", key="Cambridge")
    if st.session_state["Cambridge"]:
        if len(new_word()) != 0:
            st.write(f"[Check](https://dictionary.cambridge.org/dictionary/english/{word})")
        else:
            st.write("Please enter a word")

    st.button("Collins Dictionary", key="Collins")
    if st.session_state["Collins"]:
        if len(new_word()) != 0:
            st.write(f"[Check](https://www.collinsdictionary.com/dictionary/english/{word})")
        else:
            st.write("Please enter a word")

    st.button("Reverso Context", key="Reverso")
    if st.session_state["Reverso"]:
        if len(new_word()) != 0:
            st.write(f"[Check](https://context.reverso.net/translation/english-korean/{word})")
        else:
            st.write("Please enter a word")

with st.expander("Radio"):
    url = "https://www.youtube.com/watch?v=jfKfPfyJRdk&ab_channel=LofiGirl"

    # st.audio("http://de-hz-fal-stream07.rautemusik.fm/study")
    st.video(url)
with st.expander("Legal Info"):  # Element 5
    st.write("<br><a href='https://linktr.ee/arm_andreasian_' style='color:green;'>Armen-Jean Andreasian</a> <br>Free Apps for All © 2023", unsafe_allow_html=True)
footer_container = st.container()
footer_container.markdown(
    """
    <style>
    .disclaimer {
        padding: 10px;
        background-color: yellow;
        color: black;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
with footer_container:
    st.markdown('<div class="disclaimer">'
                "This website is intended for educational purposes only and is designed to help kids learn English. "
                "<br>It is a free resource and does not contain any advertisements. "
                "<br>Usage of this website by teachers or educational institutions for commercial purposes is  prohibited."
                "<br>Feel free to inform the developers: freeappsforall.softworks@protonmail.com"


                '</div>',
                unsafe_allow_html=True)
