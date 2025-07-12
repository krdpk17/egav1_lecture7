import google.generativeai as genai
#from google.generativeai import types
import numpy as np
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

genai.configure(api_key=api_key)

sentence = "How does AlphaFold work?"

response = genai.embed_content(
    #model="models/text-embedding-004",  # Recommended embedding model
    model="gemini-embedding-exp-03-07", 
    content=sentence
)

# The response is a dict with 'embedding' key
embedding_vector = np.array(response["embedding"], dtype=np.float32)

print(f"🔢 Vector length: {len(embedding_vector)}")
print(f"📈 First 10 values: {embedding_vector[:10]}")
