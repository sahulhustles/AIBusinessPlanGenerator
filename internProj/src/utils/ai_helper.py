from .config import get_gemini_client

def generate_business_strategy(prompt: str) -> str:
    """
    Generate business strategy using Google Gemini Flash
    """
    try:
        model = get_gemini_client()
        response = model.generate_content(
            f"""You are a senior business consultant. {prompt}
            Format the response in Markdown with these sections:
            ## Executive Summary
            ## Market Analysis  
            ## Operational Plan
            ## Financial Projections
            ## Marketing Strategy
            ## Risk Assessment
            ## Implementation Timeline
            
            Use bullet points and clear headings."""
        )
        return response.text
        
    except Exception as e:
        return f"API Error: {str(e)}"