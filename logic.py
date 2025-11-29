import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def get_gemini_model():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return None
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-2.0-flash')

def identify_stack(context):
    model = get_gemini_model()
    if not model:
        return "Error: GEMINI_API_KEY not found in .env file."
    
    prompt = f"""
    Analyze the following file structure and content of a software project:
    
    {context}
    
    Identify the main programming language, framework, and any key tools used (e.g., Docker, specific libraries).
    Provide a concise summary.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error calling Gemini: {str(e)}"

def generate_workflow(context, workflow_type):
    model = get_gemini_model()
    if not model:
        return "Error: GEMINI_API_KEY not found in .env file."
    
    prompt = f"""
    You are a DevOps expert. Based on the following project context:
    
    {context}
    
    Generate a GitHub Actions YAML workflow for: {workflow_type}.
    
    Ensure the workflow is best practice, uses appropriate actions (e.g., actions/checkout, setup-python/node), and is ready to be saved to .github/workflows/.
    Return ONLY the YAML code block.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error calling Gemini: {str(e)}"
