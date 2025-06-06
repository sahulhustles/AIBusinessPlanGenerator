import streamlit as st
from utils.ai_helper import generate_business_strategy
from utils.export_helper import export_to_docx, export_to_pdf
from datetime import datetime
import os
import tempfile

# Custom CSS with professional styling
def inject_css():
    st.markdown("""
    <style>
        .stTextInput input, .stSelectbox select, .stTextArea textarea {
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            padding: 12px;
        }
        .stButton button {
            background-color: #2563eb;
            color: white;
            border-radius: 8px;
            padding: 12px 24px;
            transition: all 0.3s;
        }
        .stButton button:hover {
            background-color: #1d4ed8;
            transform: scale(1.05);
        }
        .download-btn {
            margin-top: 20px;
            gap: 10px;
        }
        .stTabs [data-baseweb="tab-list"] {
            gap: 5px;
        }
        .stTabs [data-baseweb="tab"] {
            background: #050505;
            border-radius: 8px 8px 0 0;
            padding: 10px 20px;
        }
        .stMarkdown h1 {
            color: #292F36;
        }
    </style>
    """, unsafe_allow_html=True)

inject_css()

# App Interface
st.title("🚀 AI Business Plan Generator")
st.markdown("Generate comprehensive business plans powered by Google Gemini")

with st.form("business_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        industry = st.selectbox(
            "Industry",
            ["Technology", "Retail", "Food & Beverage", "Healthcare", "Manufacturing", "Other"]
        )
        business_name = st.text_input("Business Name [Minimum 2 words]")
        
    with col2:
        budget = st.selectbox(
            "Budget Range",
            ["Under $10k", "$10k-$50k", "$50k-$100k", "$100k+"]
        )
        timeframe = st.selectbox(
            "Implementation Timeframe [Approx.]",
            ["Short-term (0-6 months)", "Mid-term (6-12 months)", "Long-term (1-3 years)"]
        )
    
    unique_value = st.text_area(
        "Value Proposition [Minimum 20 words]", 
        height=100
    )
    
    submitted = st.form_submit_button("Generate Business Plan")

if submitted:
    with st.spinner("🧠 Generating your business plan..."):
        # Initialize paths
        docx_path, pdf_path = None, None
        
        try:
            prompt = f"""
            Create a comprehensive business plan for {business_name}, a {industry} company.
            Requirements:
            - Budget: {budget}
            - Timeframe: {timeframe}
            - Unique Value: {unique_value}
            
            Include these sections:
            1. Executive Summary
            2. Market Analysis
            3. Products/Services
            4. Marketing Strategy
            5. Operational Plan
            6. Financial Projections
            7. Risk Assessment
            """
            
            plan = generate_business_strategy(prompt)
            
            # Display results
            tab1, tab2 = st.tabs(["Business Plan", "Raw Output"])
            
            with tab1:
                st.subheader(f"{business_name} Business Plan")
                st.markdown(f"**Industry:** {industry}")
                st.markdown(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
                st.divider()
                st.markdown(plan.replace('\n', '\n\n'))
                
            with tab2:
                st.code(plan, language="markdown")
            
            # Export section
            st.subheader("Export Options")
            col1, col2 = st.columns(2)
            
            with col1:
                docx_path = export_to_docx(plan, business_name.replace(" ", "_"))
                with open(docx_path, "rb") as f:
                    st.download_button(
                        label="📥 Download DOCX",
                        data=f,
                        file_name=f"{business_name.replace(' ', '_')}_plan.docx",
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )
            
            with col2:
                pdf_path = export_to_pdf(plan, business_name.replace(" ", "_"))
                with open(pdf_path, "rb") as f:
                    st.download_button(
                        label="📥 Download PDF",
                        data=f,
                        file_name=f"{business_name.replace(' ', '_')}_plan.pdf",
                        mime="application/pdf"
                    )
        
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
        
        finally:
            # Cleanup temporary files
            for path in [docx_path, pdf_path]:
                if path and os.path.exists(path):
                    try:
                        os.remove(path)
                    except:
                        pass  # Silent fail if file couldn't be deleted

if __name__ == "__main__":
    # Create necessary directories
    os.makedirs("data", exist_ok=True)
    os.makedirs("temp", exist_ok=True)