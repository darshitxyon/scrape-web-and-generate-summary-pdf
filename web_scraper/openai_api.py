```python
import openai
from config import OPENAI_API_KEY, MAX_SUMMARY_LENGTH

openai.api_key = OPENAI_API_KEY

def summarize_text(text):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=text,
        max_tokens=MAX_SUMMARY_LENGTH,
        temperature=0.5,
    )
    return response.choices[0].text.strip()
```