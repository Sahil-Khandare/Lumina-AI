import streamlit as st
import requests
import base64
import os
from dotenv import load_dotenv

# =========================
# Load Environment Variables
# =========================

load_dotenv()
API_KEY = os.getenv("NVIDIA_API_KEY")

# =========================
# Page Config
# =========================

st.set_page_config(
    page_title="VisionLens",
    page_icon="📷",
    layout="wide"
)

# =========================
# Custom CSS
# =========================

st.markdown("""
<style>

.main {
    background-color: #F5F1EA;
}

.block-container {
    padding-top: 2rem;
    padding-left: 5rem;
    padding-right: 5rem;
}

h1 {
    font-size: 72px !important;
    font-family: Georgia, serif;
    font-weight: 300;
    color: #111111;
}

body {
    color: #111111;
}

.small-header {
    letter-spacing: 3px;
    font-size: 12px;
    color: #666666;
}

.description-box {
    background-color: #1E1E1E;
    color: #FFFFFF;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #444444;

    min-height: 350px;
    max-height: 650px;

    overflow-y: auto;
    line-height: 1.8;
}

hr {
    border: none;
    border-top: 1px solid #BBBBBB;
    margin-top: 10px;
    margin-bottom: 25px;
}

.selected-mode {
    background: linear-gradient(90deg,#16a34a,#22c55e);
    color: white;
    border-radius: 8px;
    text-align: center;
    padding: 10px;
    margin-top: 6px;
    font-weight: bold;
    border: 2px solid #4ade80;
    box-shadow: 0 0 15px rgba(34,197,94,0.6);
}

div[role="radiogroup"] label {
    font-size: 20px !important;
    padding: 20px !important;
    min-width: 250px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# Header
# =========================

st.markdown("""
<h1>VisionLens</h1>

<p class="small-header">
INDEPENDENT · VISUAL INTELLIGENCE · NVIDIA POWERED
</p>

<hr>
""", unsafe_allow_html=True)

# Default mode

st.markdown("## Choose Analysis Mode")

task = st.radio(
    "",
    [
        "Describe Image",
        "Summarize Image",
        "Detect Objects",
        "Explain Scene"
    ],
    horizontal=True
)

# =========================
# Prompt Selection
# =========================

prompt_map = {
    "Describe Image": "Describe this image in detail.",
    "Summarize Image": "Give a concise summary of this image.",
    "Detect Objects": "List all visible objects in this image.",
    "Explain Scene": "Explain what is happening in this image."
}

prompt = prompt_map[task]

# =========================
# Upload Section
# =========================

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

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

                image_bytes = uploaded_file.read()

                image_base64 = base64.b64encode(
                    image_bytes
                ).decode()

                headers = {
                    "Authorization": f"Bearer {API_KEY}",
                    "Accept": "application/json"
                }

                payload = {
                    "model": "meta/llama-3.2-11b-vision-instruct",
                    "messages": [
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "text",
                                    "text": prompt
                                },
                                {
                                    "type": "image_url",
                                    "image_url": {
                                        "url": f"data:image/jpeg;base64,{image_base64}"
                                    }
                                }
                            ]
                        }
                    ],
                    "max_tokens": 150
                }

                try:

                    response = requests.post(
                        "https://integrate.api.nvidia.com/v1/chat/completions",
                        headers=headers,
                        json=payload,
                        timeout=60
                    )

                    result = response.json()

                    if "choices" in result:

                        description = result["choices"][0]["message"]["content"]

                        st.markdown(
                            f"""
                            <div class="description-box">
                            <h4>AI Analysis Result</h4>
                            {description}
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                        st.success("✅ Analysis Complete")

                        st.download_button(
                            label="📄 Download Report",
                            data=description,
                            file_name="visionlens_report.txt",
                            mime="text/plain",
                            key="download_report"
                        )

                    else:

                        st.error("⚠️ API Error")
                        st.write(result)

                except requests.exceptions.Timeout:

                    st.warning("⏳ Request timed out.")

                    st.info(
                        "The NVIDIA endpoint may be busy. Try again."
                    )

                except Exception as e:

                    st.error(f"❌ Unexpected Error: {e}")

# =========================
# Footer
# =========================

st.markdown("---")

st.caption(
    "VisionLens • AI-Powered Visual Intelligence using NVIDIA NIM"
)               

