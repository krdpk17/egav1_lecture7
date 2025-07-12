import google.generativeai as genai
#from google.genai import types
import numpy as np
from scipy.spatial.distance import cosine
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables")
genai.configure(api_key=api_key)

def get_embedding(text: str, task="RETRIEVAL_DOCUMENT") -> np.ndarray:
    res = genai.embed_content(
        model="gemini-embedding-exp-03-07",
        content=text
        #config=types.EmbedContentConfig(task_type=task)
    )
    return np.array(res["embedding"], dtype=np.float32)

# 🎯 Phrases to compare
sentences = [
    "How does AlphaFold work?",
    "How do proteins fold?",
    "What is the capital of France?",
    "Explain how neural networks learn.",
    "Tell the name of capital of France?"
]

# 🧠 Get embeddings
embeddings = [get_embedding(s) for s in sentences]

# 🔁 Compare all pairs using cosine similarity
def cosine_similarity(v1, v2):
    return 1 - cosine(v1, v2)  # 1 = perfect match

print("🔍 Semantic Similarity Matrix:\n")
for i in range(len(sentences)):
    for j in range(i + 1, len(sentences)):
        sim = cosine_similarity(embeddings[i], embeddings[j])
        print(f"\"{sentences[i]}\" ↔ \"{sentences[j]}\" → similarity = {sim:.3f}")
