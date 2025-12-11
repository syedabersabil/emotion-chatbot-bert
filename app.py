"""Emotion-Based Chatbot - Streamlit Web Interface"""
import streamlit as st
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from src.chatbot_logic import get_bot_reply

# Page config
st.set_page_config(
    page_title="Emotion Chatbot",
    page_icon="🧠",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
.stTextInput > div > div > input {
    font-size: 16px;
}
.emotion-badge {
    display: inline-block;
    padding: 4px 12px;
    border-radius: 12px;
    font-size: 14px;
    font-weight: 600;
    margin: 4px 0;
}
.happy { background-color: #fef3c7; color: #92400e; }
.sad { background-color: #dbeafe; color: #1e3a8a; }
.angry { background-color: #fee2e2; color: #991b1b; }
.anxious { background-color: #e9d5ff; color: #581c87; }
</style>
""", unsafe_allow_html=True)

# Title and description
st.title("🧠 Emotion-Based Chatbot")
st.markdown("""
Yeh chatbot **BERT** (NLP model) use karke tumhari emotions detect karta hai aur accordingly reply deta hai.

**Emotions detected:** Happy 😊 | Sad 😔 | Angry 😤 | Anxious 😟
""")

st.divider()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.emotions = []

# Display chat history
for i, message in enumerate(st.session_state.messages):
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
        # Show emotion badge for bot messages
        if message["role"] == "assistant" and i < len(st.session_state.emotions):
            emotion = st.session_state.emotions[i]
            st.markdown(
                f'<span class="emotion-badge {emotion}">Detected: {emotion}</span>',
                unsafe_allow_html=True
            )

# Chat input
if prompt := st.chat_input("Type your message here..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get bot response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            emotion, reply, metadata = get_bot_reply(prompt)
            
        st.markdown(reply)
        
        # Show emotion badge
        st.markdown(
            f'<span class="emotion-badge {emotion}">Detected: {emotion}</span>',
            unsafe_allow_html=True
        )
        
        # Show confidence (optional debug info)
        with st.expander("View Detection Details"):
            st.json(metadata)
    
    # Save assistant message
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.session_state.emotions.append(emotion)

# Sidebar
with st.sidebar:
    st.header("About")
    st.markdown("""
    **Tech Stack:**
    - BERT (DistilBERT) for emotion classification
    - Transformers library (Hugging Face)
    - Streamlit for web UI
    
    **Model:**
    `bhadresh-savani/distilbert-base-uncased-emotion`
    
    **Emotions:**
    - 😊 Happy
    - 😔 Sad
    - 😤 Angry
    - 😟 Anxious
    """)
    
    st.divider()
    
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.session_state.emotions = []
        st.rerun()
    
    st.markdown("---")
    st.markdown("👨‍💻 Built with ❤️ for NLP learning")
