import os
from openai import OpenAI

_openai_client = None

def get_openai_client():
    """Get or initialize the OpenAI client."""
    global _openai_client
    
    if _openai_client is not None:
        return _openai_client
    
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OpenAI API Key not configured")
    
    api_key = api_key.strip()
    _openai_client = OpenAI(api_key=api_key)
    return _openai_client