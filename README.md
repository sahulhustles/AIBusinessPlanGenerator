# 🧠 AI Business Plan Generator

[![Live on Streamlit](https://img.shields.io/badge/Live%20Demo-Click%20Here-brightgreen?style=for-the-badge&logo=streamlit)](https://aibusinessplangenerator.streamlit.app/)
[![Made with Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Built%20With-Streamlit-red?style=for-the-badge&logo=streamlit)](https://streamlit.io/)
[![Google Gemini](https://img.shields.io/badge/AI%20Model-Google%20Gemini-blueviolet?style=for-the-badge&logo=google)](https://ai.google.dev/)
[![MIT License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![Open in GitHub](https://img.shields.io/badge/GitHub-View%20Source-181717?style=for-the-badge&logo=github)](https://github.com/sahulhustles/AIBusinessPlanGenerator)

---

### ✨ Generate AI-Powered Business Strategies Instantly!

**AI Business Plan Generator** helps you create full-length business strategies tailored to your industry, budget, niche, and timeline — all in seconds using **Google Gemini AI**. Export your plan as professional **PDF** or **DOCX** files directly from the browser.

---

## 🚀 Key Features

- 🔮 AI-generated business strategy content (Executive Summary, Financial Plans, etc.)
- 🏷️ Custom input options for industry, budget, niche, and timeframe
- 📄 One-click export to **PDF** and **DOCX**
- 🧠 Powered by **Google Gemini** (Generative AI)
- ⚡ Live on [Streamlit](https://aibusinessplangenerator.streamlit.app/)
- 📦 Built with modular, clean Python code
- 🌐 Easy local setup via `.env` and `requirements.txt`

---

# If you want to use this Business Plan Generator for free , you can checkout this link - https://aibusinessplangenerator.streamlit.app/

## 📸 Live Preview

[App Preview] ![{C0053AFB-783C-40FA-86F9-00FA97D61A80}](https://github.com/user-attachments/assets/de8312e9-732f-4e28-a738-45243dbb4862)



---

## 🛠️ Built With

- **Python 3.10**
- [Streamlit](https://streamlit.io/)
- [Google Generative AI (Gemini)](https://ai.google.dev/)
- `python-docx`, `fpdf`, `pdfkit`, `dotenv`


## 📄 Quick Start (if you need it locally in your machine)

# Clone the project
git clone https://github.com/sahulhustles/AIBusinessPlanGenerator.git
cd AIBusinessPlanGenerator

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # or
.\venv\Scripts\activate on Windows

# Install requirements
pip install -r requirements.txt

# Add your API key in src/utils/.env (optional)
GEMINI_API_KEY=your_gemini_api_key

# Run the app
streamlit run src/app.py


# 🔐 Environment Setup
You can use the provided .env.example file inside src/utils/:

cd src/utils/.env.example src/utils/.env
Then paste your API key into .env.

📝 Export Paths
sampleStrategyPlans/PDFS/*.pdf

sampleStrategyPlans/DOCS/*.docx

📬 Author
Built with ❤️ by @sahulhustles
Connect • Collaborate • Contribute 🤝

📄 License
Licensed under the MIT License.
