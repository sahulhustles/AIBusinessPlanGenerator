from .config import get_ai_client
import time

def generate_business_strategy(prompt: str, retries: int = 3, delay: int = 10) -> str:
    """
    Generate business strategy using Groq API (Llama 3), with retry logic.
    """
    client = get_ai_client()
    full_prompt = f"""You are a senior business consultant. {prompt}
            Format the response in Markdown with these sections:
            ## Executive Summary
            ## Market Analysis  
            ## Operational Plan
            ## Financial Projections
            ## Marketing Strategy
            ## Risk Assessment
            ## Implementation Timeline
            
            Use bullet points and clear headings."""
            
    for attempt in range(retries):
        try:
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": full_prompt,
                    }
                ],
                model="llama-3.3-70b-versatile",
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            error_msg = str(e)
            if "429" in error_msg or "rate limit" in error_msg.lower():
                if attempt < retries - 1:
                    time.sleep(delay * (attempt + 1))
                    continue
            raise RuntimeError(f"API Error: {error_msg}")
            
    raise RuntimeError("Failed to generate plan after multiple retries due to API limits.")