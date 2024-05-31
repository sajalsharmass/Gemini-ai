import os
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
from gemini_utility import (load_gemini_pro, gemini_pro_vision_response)

working_directory = os.path.dirname(os.path.abspath(__file__))

# page configuration setting
st.set_page_config(page_title="SS_Gemini", layout="centered")

with st.sidebar:
    selected = option_menu("Gemini AI", ["ChatBot", "Image Captioning"], menu_icon='robot', icons=['chat-dots','file-earmark-image'], default_index=0)

def translate_role_for_steamlit(user_role):
    if user_role == 'model':
        return "assisstant"
    else:
        return user_role

if selected == "ChatBot":
    model = load_gemini_pro()

    if "chat_session" not in st.session_state:
        st.session_state.chat_session = model.start_chat(history=[])

    st.title("ChatBot")

    for message in st.session_state.chat_session.history:
        with st.chat_message(translate_role_for_steamlit(message.role)):
            st.markdown(message.parts[0].text)
    
    user_prompt = st.chat_input("Ask Anything...")

    if user_prompt:
        st.chat_message("user").markdown(user_prompt)

        gemini_response = st.session_state.chat_session.send_message(user_prompt)

        with st.chat_message("assisstant"):
            st.markdown(gemini_response.text)

if selected == "Image Captioning":
    st.title("Snap Narrate")

    uploaded_image = st.file_uploader("Upload an Image...", type=["jpg", "jpeg", "png"])

    if st.button("Generate Caption"):
        image = Image.open(uploaded_image)

        col1, col2 = st.columns(2)

        with col1:
            resized_image = image.resize((800,500))
            st.image(resized_image)
        
        default_prompt = "write a short caption for this image"

        caption = gemini_pro_vision_response(default_prompt, image)

        with col2:
            st.info(caption)
