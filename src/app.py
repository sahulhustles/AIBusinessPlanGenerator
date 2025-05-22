import streamlit as st
from utils.ai_helper import generate_business_strategy
from datetime import datetime
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
    </style>
    """, unsafe_allow_html=True)

inject_css()

# App Interface
st.title("🚀 AI Business Strategy Generator")
# Change the subtitle to:
st.markdown("Generate comprehensive business strategies powered by Google Gemma 7B")

with st.form("strategy_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        industry = st.selectbox(
            "Industry",
            ("Technology", "Healthcare", "Finance", "Retail", "Manufacturing", "Other"),
            index=0
        )
        business_type = st.text_input("Business Type/Niche")
        
    with col2:
        budget = st.selectbox(
            "Budget Range",
            ("Under $10k", "$10k-$50k", "$50k-$100k", "$100k+"),
            index=1
        )
        timeframe = st.selectbox(
            "Implementation Timeframe",
            ("Short-term (0-6 months)", "Mid-term (6-12 months)", "Long-term (1-3 years)"),
            index=2
        )
    
    unique_value = st.text_area("Unique Value Proposition", height=100)
    submitted = st.form_submit_button("Generate Strategy")

if submitted:
    with st.spinner("🧠 Generating strategy..."):
        prompt = f"""
        Create a comprehensive business strategy for a {industry} company in {business_type}.
        Requirements:
        - Budget: {budget}
        - Timeframe: {timeframe}
        - Unique Value: {unique_value}
        
        Structure:
        1. Executive Summary
        2. Market Analysis
        3. Operational Plan
        4. Financial Projections
        5. Marketing Strategy
        6. Risk Assessment
        7. Implementation Timeline
        """
        
        strategy = generate_business_strategy(prompt)
        
        # Display results
        tab1, tab2 = st.tabs(["Strategy Report", "Raw Output"])
        
        with tab1:
            st.subheader(f"{industry} Strategy Report")
            st.markdown(f"**Business Type:** {business_type}")
            st.markdown(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
            st.divider()
            st.markdown(strategy.replace('\n', '\n\n'))
            
        with tab2:
            st.code(strategy, language="markdown")
            
        # Download feature
        st.download_button(
            label="📥 Download Strategy",
            data=strategy,
            file_name=f"{industry.replace(' ', '_')}_strategy.md",
            mime="text/markdown"
        )
