import streamlit as st
import pycountry
from gtts import gTTS
import tempfile

from main import translate

st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍",
    layout="centered"
)

# ---------------- CSS ----------------
st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

.title{
    text-align:center;
    font-size:42px;
    font-weight:700;
    color:#2E86DE;
}

.subtitle{
    text-align:center;
    color:gray;
    margin-bottom:25px;
}

.stButton>button{
    width:100%;
    height:50px;
    border-radius:12px;
    font-size:18px;
    font-weight:bold;
}

.output-box{
    background:white;
    padding:18px;
    border-radius:15px;
    border:1px solid #ddd;
    box-shadow:0px 2px 10px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

# ---------------- Header ----------------
st.markdown(
    '<div class="title">🌍 AI Language Translator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Translate text into any language and listen to the pronunciation.</div>',
    unsafe_allow_html=True
)

# ---------------- Languages ----------------
languages = sorted(
    list(
        set(
            language.name
            for language in pycountry.languages
            if hasattr(language, "name")
        )
    )
)

# ---------------- Session State ----------------
if "translated_text" not in st.session_state:
    st.session_state.translated_text = ""

# ---------------- Input ----------------
user_text = st.text_area(
    "📝 Enter Text",
    height=170,
    placeholder="Type something here..."
)

selected_language = st.selectbox(
    "🌐 Select Target Language",
    languages
)

# ---------------- Translate ----------------
if st.button("🔄 Translate"):

    if not user_text.strip():
        st.warning("Please enter some text.")

    else:
        with st.spinner("Translating..."):
            st.session_state.translated_text = translate(
                user_text,
                selected_language
            )

# ---------------- Output ----------------
if st.session_state.translated_text:

    st.markdown("### ✅ Translation")

    st.markdown(
        f"""
        <div class="output-box">
        {st.session_state.translated_text}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        st.code(st.session_state.translated_text)

    with col2:

        if st.button("🔊 Speak"):

            try:
                tts = gTTS(text=st.session_state.translated_text)

                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
                    tts.save(fp.name)

                    audio_file = open(fp.name, "rb")
                    audio_bytes = audio_file.read()

                st.audio(audio_bytes, format="audio/mp3")

            except Exception as e:
                st.error(f"Speech Error: {e}")

st.markdown("---")
st.caption("Built with ❤️ using LangGraph + Mistral AI + Streamlit")