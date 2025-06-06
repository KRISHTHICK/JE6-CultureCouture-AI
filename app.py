import streamlit as st
from PIL import Image
import os
from transformers import pipeline
from langchain.llms import Ollama

# === SETUP ===
st.set_page_config(page_title="🧠 CultureCouture AI", layout="wide")
st.title("🧵 CultureCouture AI - Tradition Meets Trend")

# === IMAGE UPLOAD ===
uploaded_image = st.file_uploader("📸 Upload a traditional outfit image", type=["jpg", "jpeg", "png"])
if uploaded_image:
    img = Image.open(uploaded_image)
    st.image(img, caption="Uploaded Outfit", use_column_width=True)

    # Simulate analysis
    st.subheader("🧬 Cultural Fashion Analysis")
    st.markdown("""
    - Style: Saree (Traditional)
    - Origin: South Asia
    - Fabric: Silk Blend
    - Occasion: Festive/Ceremonial
    """)

    st.subheader("✨ TrendFusion Suggestions")
    st.markdown("""
    - Transform into a modern **crop top and long skirt** fusion.
    - Pair with **blazer and boots** for urban festive wear.
    - Use **digital print** of traditional motifs on casual tees.
    """)

    st.subheader("✍️ Insta Caption Generator")
    caption_prompt = "Write a stylish Instagram caption combining tradition and modern fashion."
    llm = Ollama(model="llama3")
    caption = llm.invoke(caption_prompt)
    st.text_area("Generated Caption", caption.strip(), height=100)

    st.subheader("🏷️ Hashtag Suggestions")
    hashtags = "#TraditionMeetsTrend #FusionWear #CulturalChic #SareeNotSari #AIStylist"
    st.text_area("Generated Hashtags", hashtags, height=80)

    st.subheader("💬 Ask AI Style Agent")
    user_question = st.chat_input("Ask: How can I modernize this outfit?")
    if user_question:
        answer = llm.invoke(f"Suggest a trendy fusion style idea for: {user_question}")
        st.markdown(f"💡 **AI Suggestion:** {answer}")
