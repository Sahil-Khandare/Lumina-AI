import streamlit as st
import base64
import os

from dotenv import load_dotenv

from api import analyze_image
from prompts import PROMPT_MAP

load_dotenv()
API_KEY = os.getenv("NVIDIA_API_KEY")

st.set_page_config(
    page_title="Lumina AI",
    page_icon="📷",
    layout="wide"
)

def get_base64_image(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode()
    
bg_image = get_base64_image("assets/moon.png")
with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.markdown(
    f"""
    <style>
    .stApp {{
        background:
            linear-gradient(
                rgba(0,0,0,0.65),
                rgba(0,0,0,0.65)
            ),
            url("data:image/png;base64,{bg_image}");

        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
<h1>Lumina AI</h1>

<p class="small-header">
SEE BEYOND THE PIXELS · NVIDIA POWERED
</p>

<hr>
""", unsafe_allow_html=True)

st.markdown("## Choose Analysis Mode")

MODES = list(PROMPT_MAP.keys())
task = st.radio(
    "",
    MODES,
    horizontal=True
)
max_tokens= MAX_TOKENS[task]


uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg","png","jpeg"]
)

if "description" not in st.session_state:
    st.session_state["description"] = None

if uploaded_file is not None:
     
    col1, col2 = st.columns([1.2,1], gap="large")

    with col1:

        st.subheader("Uploaded Image")

        st.image(
                    uploaded_file,
                    use_container_width=True,
                    caption="Uploaded Image"
        )

    with col2:

        st.subheader("AI Analysis")

        if st.button("Generate Analysis"):

            with st.spinner("Analyzing image..."):

                image_base64 = base64.b64encode(
                    uploaded_file.read()
                ).decode()

                prompt = PROMPT_MAP[task]

                try:

                    description = analyze_image(
                        image_base64,
                        prompt,
                        API_KEY
                    )

                    st.session_state["description"] = description

                except Exception as e:
                    st.error(f"❌ Unexpected Error: {e}")


        if st.session_state["description"]:

            st.markdown(
                f"""
                <div class="description-box">
                {st.session_state["description"]}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.success("✅ Analysis Complete")

            st.download_button(
                label="📄 Download Report",
                data=st.session_state["description"],
                file_name="lumina_report.txt",
                mime="text/plain",
                key="download_report"
            )

# =========================
# Footer
# =========================

st.markdown("---")

st.caption(
    "Lumina AI • Transforming Images into Insights • Powered by NVIDIA NIM"
)  
