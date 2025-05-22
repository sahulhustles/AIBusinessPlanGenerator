import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def get_gemini_client():
    return genai.GenerativeModel('gemini-2.0-flash')

# Initialize configuration
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))