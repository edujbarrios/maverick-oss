from __future__ import annotations

import os

import streamlit as st
from dotenv import load_dotenv
from PIL import Image

from maverick_oss.config import build_agent_config
from maverick_oss.pipeline import MaverickPipeline


load_dotenv()


st.set_page_config(page_title="MAVERICK-OSS", page_icon="M", layout="wide")
st.title("MAVERICK-OSS")
st.caption("Reference-free multi-agent image description with Vision-Language Models.")

with st.sidebar:
    st.header("API Configuration")
    api_key = st.text_input("API key", value=os.getenv("OPENAI_API_KEY", ""), type="password")
    base_url = st.text_input("Base URL", value=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1"))
    model = st.text_input("Model", value=os.getenv("MAVERICK_MODEL", "gpt-4o-mini"))
    st.info("The same OpenAI-compatible configuration is applied to all agents in this demo.")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg", "webp"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Input image", use_container_width=True)

    if st.button("Run reference-free pipeline", type="primary"):
        if not api_key:
            st.error("An API key is required before running the pipeline.")
        else:
            config = build_agent_config(api_key=api_key, base_url=base_url, model=model)
            pipeline = MaverickPipeline(config)

            with st.spinner("Running MAVERICK-OSS agents..."):
                result = pipeline.run(image)

            st.subheader("Agent Outputs")
            tabs = st.tabs(["A1 Identifier", "A2 Descriptor", "A3 Critic", "A4 Refiner"])
            for tab, key in zip(tabs, ["A1", "A2", "A3", "A4"]):
                with tab:
                    st.markdown(result[key])
else:
    st.info("Upload an image to run the reference-free pipeline.")
