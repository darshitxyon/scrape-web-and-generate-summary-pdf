```python
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(text):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=text,
        temperature=0.5,
        max_tokens=500
    )
    return response.choices[0].text.strip()
```