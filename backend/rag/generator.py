import os
from typing import List
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = """
You are a helpful academic assistant for NPTEL courses.
Answer the question using ONLY the provided context.
If the answer is not present in the context, prefix the response with a '0'.\
Else prefix the answer with a 1
"""

class Generator:
    def __init__(self):
        self.model = genai.GenerativeModel(
            model_name="models/gemini-2.5-flash",
            system_instruction=SYSTEM_PROMPT
        )
    
    def generate_response(self,
                          query: str,
                          context_chunks: List[str]) -> List[str]:
        context = "\n\n".join(context_chunks)
        
        prompt = f"""
        Context: 
        {context}
        
        Question:
        {query}
        
        Answer:
        """
        
        response = self.model.generate_content(
            prompt,
            generation_config={
                "temperature" : 0.2,
                "max_output_tokens" : 512
            }
        )
        
        return response.text.strip()[1:]