```python
import sys

def get_search_url():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        print("Please provide a search URL as an argument.")
        sys.exit(1)
```