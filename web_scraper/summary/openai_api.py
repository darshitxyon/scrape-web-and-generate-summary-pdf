```python
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(text):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=f"{text}\n\nSummarize:",
        temperature=0.3,
        max_tokens=500
    )

    summary = response.choices[0].text.strip()
    return summary
```