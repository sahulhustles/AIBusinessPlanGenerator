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

![App Screenshot](./preview.png) <!-- Replace with actual image path if needed -->

---

## 📂 Folder Structure

.
├── .venv/ # Python virtual environment
├── sampleStrategyPlans/ # Sample exported strategies
│ ├── DOCS/
│ └── PDFS/
├── src/
│ ├── data/
│ ├── temp/
│ ├── utils/
│ │ ├── ai_helper.py # Handles Google Gemini prompts
│ │ ├── config.py # Gemini API key config
│ │ └── export_helper.py # Exports to PDF/DOCX
│ └── app.py # Main Streamlit application
├── .env # Environment variable (not pushed)
├── requirements.txt # All dependencies
├── style.css # Custom CSS styles
└── README.md
---

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

bash
Copy
Edit
python -m venv .venv
.\.venv\Scripts\activate
macOS/Linux:

bash
Copy
Edit
python3 -m venv .venv
source .venv/bin/activate

#### 3. Install Required Libraries
bash
Copy
Edit
pip install -r requirements.txt

#### 🔐 4. Set Up Environment Variables
Inside the src/utils/ directory, create a .env file and add your Gemini API key like this:

env
Copy
Edit
GEMINI_API_KEY=your_gemini_api_key_here


#### ▶️ 5. Run the Application
From the root folder (or inside src/), run:

bash
Copy
Edit
streamlit run src/app.py
Then open the generated URL in your browser (usually http://localhost:8501).

#### 6.📝 Export Functionality
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
