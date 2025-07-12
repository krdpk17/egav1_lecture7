EGAv1 Lecture 7 - Embeddings Project
====================================

This project demonstrates how to use Google Generative AI to generate text embeddings using Python.

Setup Instructions:
-------------------
1. Create and activate a Python virtual environment:
   $ python3 -m venv venv
   $ source venv/bin/activate

2. Install dependencies:
   $ pip install google-generativeai numpy python-dotenv

3. Set your Google Generative AI API key:
   - Create a `.env` file in the project directory with the following line:
     GEMINI_API_KEY=your_api_key_here

Usage:
------
- Run the embeddings script:
  $ python3 embeddings.py

This will print the length and first 5 values of the embedding vector for a sample sentence.

Example Output:
---------------
🔢Vector length: 3072
📈 First 10 values: [ 0.01765655  0.01203792  0.01580679 -0.06208311 -0.04674176  0.02804125
  0.01237462 -0.01945324  0.01953902  0.03887416]

Notes:
------
- Make sure your API key is valid and has access to the embedding model.
- For more information, see the official Google Generative AI documentation. 