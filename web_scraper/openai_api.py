```python
import openai
from typing import List

openai.api_key = 'your-api-key'

def summarize_text(texts: List[str]) -> List[str]:
    summaries = []
    for text in texts:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=text,
            max_tokens=500
        )
        summaries.append(response.choices[0].text.strip())
    return summaries
```