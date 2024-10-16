import requests

# OpenAI API key (replace with your own)
OPENAI_API_KEY = 'your_openai_api_key'
LLM_URL = "https://api.openai.com/v1/chat/completions"

# Function to get insights from the LLM
def generate_insights(prompt):
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
    }
    
    response = requests.post(LLM_URL, headers=headers, json=data)
    return response.json()['choices'][0]['message']['content']
