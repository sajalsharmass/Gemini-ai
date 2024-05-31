import os
import json
import google.generativeai as genai

working_directory = os.path.dirname(os.path.abspath(__file__))

config_file_path = f"{working_directory}/config.json"
config_data = json.load(open(config_file_path))

google_api_key = config_data["GOOGLE_API_KEY"]

genai.configure(api_key=google_api_key)

def load_gemini_pro():
    gemini_pro = genai.GenerativeModel("gemini-pro")
    return gemini_pro

def gemini_pro_vision_response(prompt, image):
    gemini_pro_vision_model = genai.GenerativeModel("gemini-pro-vision")
    response = gemini_pro_vision_model.generate_content([prompt, image])
    result = response.text
    return result