# pro
import streamlit as st
import plotly.express as px
import streamlit.components.v1 as components
import random


st.set_page_config(page_title="Learn English",
                   page_icon="🍏")
df = px.data.iris()
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://i.ibb.co/w6mTRgX/cover.jpg");
background-size: 130%;
}}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("Learn English")


with st.expander("How to use?"):    # Element 1
    st.markdown('<div class="disclaimer">'
                "To be able to use Better English Pro you need to allow pop-ups for this website"
                "from your browser's settings."
                "<br>However, you can still use the basic version of Better English without giving any access"
                "on <b> <span style='color:green;'>better.streamlit.com:</span>  </b>"
                '</div>',
                unsafe_allow_html=True)
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


st.text_input(label="Enter a word you want to check:",    # Element 2
              placeholder="Swim, read, drink coffee, etc",
              on_change=new_word,
              key="new word")


st.write('<style>div.row-widget.stButton > button:first-child '
         '{ width: 100%; background-color: #074986; color: #FFFFFF; border-color: #0072C6; } '
         'div.row-widget.stButton > button:first-child:hover { background-color: #005EA2; border-color: #005EA2; } '
         'div.row-widget.stButton > button:first-child:active { background-color: #003B6F; border-color: #003B6F; '
         '}</style>',
         unsafe_allow_html=True)


def open_tab(local_url):
    script_local = f"window.open('{local_url}', '_blank', 'noopener');"
    return script_local


def show_poster():
    urls = [
        "https://i.ibb.co/nzLqkqq/1.jpg",
        "https://i.ibb.co/LPMbJ1p/2.jpg",
        "https://i.ibb.co/55wGQPX/3.jpg",
        "https://i.ibb.co/zJ7Nx1z/4.jpg",
        "https://i.ibb.co/s9025Tk/5.jpg",
        "https://i.ibb.co/m6598PM/6.jpg",

    ]
    image = random.choice(urls)
    poster = st.image(image)
    return poster


def warning():
    message = st.write("<span style='color:red'>Please enter a word</span>", unsafe_allow_html=True)
    return message


Left_column, Right_column = st.columns(2)  # Element 3

with Left_column:
    Google_Translator = st.button("Google Translate")
    Forvo_com = st.button("Forvo")
    Myefe_com = st.button("Myefe")

with Right_column:
    Cambridge_Dictionary = st.button("Cambridge Dictionary")
    Collins_Dictionary = st.button("Collins Dictionary")
    Reverso_Context = st.button("Reverso Context")

word = new_word()

if Google_Translator:
    if len(new_word()) != 0:
        script = open_tab(f"https://translate.google.com/?sl=en&tl=vi&text={word}")
        st.components.v1.html(f"<script>{script}</script>")

    else:
        warning()

if Forvo_com:
    if len(new_word()) != 0:
        script = open_tab(f"https://forvo.com/word/{word}/#en")
        st.components.v1.html(f"<script>{script}</script>")
        show_poster()
    else:
        warning()

if Myefe_com:
    if len(new_word()) != 0:
        script = open_tab(f"https://myefe.com/transcription-pronunciation/{word}")
        st.components.v1.html(f"<script>{script}</script>")
        show_poster()
    else:
        warning()


if Cambridge_Dictionary:
    if len(new_word()) != 0:
        script = open_tab(f"https://dictionary.cambridge.org/dictionary/english/{word}")
        st.components.v1.html(f"<script>{script}</script>")
        show_poster()
    else:
        warning()

if Collins_Dictionary:
    if len(new_word()) != 0:
        script = open_tab(f"https://www.collinsdictionary.com/dictionary/english/{word}")
        st.components.v1.html(f"<script>{script}</script>")
        show_poster()
    else:
        warning()

if Reverso_Context:
    if len(new_word()) != 0:
        script = open_tab(f"https://context.reverso.net/translation/english-korean/{word}")
        st.components.v1.html(f"<script>{script}</script>")
        show_poster()
    else:
        warning()


with st.expander("Radio"):   # Element 4
    radio_url = "https://www.youtube.com/watch?v=jfKfPfyJRdk&ab_channel=LofiGirl"
    # st.audio("http://de-hz-fal-stream07.rautemusik.fm/study")
    st.video(radio_url)

with st.expander("Live chat with Learn English AI"):  # Element 5
    st.info("COMING SOON")

with st.expander("Legal Info"):  # Element 5
    st.write("<br>Armen-Jean Andreasian <br>Free Apps for All © 2023", unsafe_allow_html=True)


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
with footer_container:  # Element 6
    st.markdown('<div class="disclaimer">'
                "This website is intended for educational purposes only and is designed to help kids learn English. "
                "<br>It is a free resource and does not contain any advertisements. "
                "<br>Usage of this website by teachers or educational institutions for commercial purposes is  prohibited."
                "<br>Feel free to inform the developers: freeappsforall.softworks@protonmail.com"


                '</div>',
                unsafe_allow_html=True)
