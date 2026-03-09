import streamlit as st

st.title('Chatbot')

user_input = st.text_input('You:')

if user_input:
    st.text('Chatbot: Hello! How can I help you today?')
