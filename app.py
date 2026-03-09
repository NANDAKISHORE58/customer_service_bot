# app.py
import streamlit as st
import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from src.intent_classifier import IntentClassifier
from src.response_engine import ResponseEngine

st.set_page_config(page_title="Customer Service Bot", page_icon="🤖")

@st.cache_resource
def load_models():
    print("Loading models...")
    classifier = IntentClassifier()
    engine = ResponseEngine()
    return classifier, engine

classifier, engine = load_models()

st.sidebar.title("🤖 Customer Service Bot")
st.sidebar.info("This bot uses NLP to understand your intent and rules to answer.")

st.title("Customer Support Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Type your query here..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Debug output
    intent_tag, confidence = classifier.predict(prompt)
    st.sidebar.markdown(f"""
    **Debug Info**
    - Input: `{prompt}`
    - Intent: `{intent_tag}`
    - Confidence: `{confidence:.2f}`
    - Threshold: `0.3`
    """)

    # Lowered threshold to 0.3
    if confidence > 0.3:
        response = engine.get_response(intent_tag)
    else:
        response = engine.get_fallback_response()
    
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})