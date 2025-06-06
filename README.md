# 🚀 AI Business Plan Generator

An AI-powered web application that helps you generate customized business strategies based on industry, budget, and niche — powered by **Google Gemini**. The tool supports exporting your strategy to **PDF** and **DOCX** formats for quick and professional documentation.

---

## 🌟 Features

- 🔮 Generate intelligent business plans using Google Gemini
- 🏢 Customize by Industry, Budget, Business Type, and Timeframe
- 📄 Export strategies as PDF or DOCX
- 🖥️ Clean and modern Streamlit-based interface
- 📁 Includes sample strategies for reference
- 📦 Modular Python structure for easy updates and scaling

---

## 🖼️ Preview

![{9E989A24-217E-4D9D-88A6-4C454043F61A}](https://github.com/user-attachments/assets/9aa31d33-1747-4ad3-b909-31fa53c378ee)


---

## 📂 Folder Structure
![image](https://github.com/user-attachments/assets/95ef5a26-a50a-41f1-ad3c-a269b7c650af)

## 🚀 How to Run This Project

### ✅ Prerequisites

- Python 3.8+
- pip (Python package manager)
- Google Gemini API Key ([Get here](https://ai.google.dev/))

---

### 🔧 Step-by-Step Installation

#### 1. Clone the Repository

git clone https://github.com/your-username/AI-BusinessPlanGenerator.git
cd AI-BusinessPlanGenerator

#### 2. Create & Activate a Virtual Environment
Windows:

python -m venv .venv
.\.venv\Scripts\activate

macOS/Linux:

python3 -m venv .venv
source .venv/bin/activate

#### 3. Install Required Libraries

pip install -r requirements.txt

#### 4. Go to " https://aistudio.google.com/apikey " 

### - create a API Key , copy that key and place it Inside the src/utils/ directory at .env file.

#### 🔐 5. Set Up Environment Variables

Inside the src/utils/ directory, add your Gemini API key like this:

GEMINI_API_KEY=your_gemini_api_key_here


#### ▶️ 6. Run the Application
From the root folder (or inside src/), run:

streamlit run src/app.py

Then open the generated URL in your browser (usually http://localhost:8501).

#### 7.📝 Export Functionality
You can export generated business strategies to:

📄 PDF (saved in /sampleStrategyPlans/PDFS)

📄 DOCX (saved in /sampleStrategyPlans/DOCS)

Make sure the pdf_path or docx_path is correctly defined in the code before using the export function.

🧪 Example Inputs
Industry: Technology

Budget: $10k–$50k

Niche: AI-Powered Healthcare Analytics

Timeframe: Long-term (1–3 years)

📁 Sample Outputs
You can view pre-generated business plans in:

sampleStrategyPlans/PDFS/*.pdf

sampleStrategyPlans/DOCS/*.docx

💡 Tech Stack

Python 3.10

Streamlit

Google Generative AI (google-generativeai)

python-docx

fpdf

dotenv

🤝 Contributing
Fork the repository

Create a new branch: git checkout -b my-feature

Make changes and commit: git commit -m 'Add new feature'

Push to the branch: git push origin my-feature

Open a pull request ✅

📄 License
This project is licensed under the MIT License

👤 Author
Sahul


📧 Connect on GitHub
---
