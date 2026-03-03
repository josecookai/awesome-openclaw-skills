---
name: jina-reader
version: 1.0.0
description: >-
  Extract clean, readable content from any webpage using Jina AI's r.jina.ai service.
  Perfect for reading articles, Twitter/X threads, documentation, and any web content
  without needing browser automation or API keys.
  
  Features:
  - Extract main content from any URL
  - Convert to clean Markdown
  - Twitter/X thread support
  - No authentication required
  - Fast and lightweight
  
  Use cases:
  - Reading articles without paywalls
  - Extracting Twitter/X content
  - Summarizing web pages
  - Data collection from websites
  
author: BoxATH (@chainblackbox)
license: MIT
tags:
  - web-scraping
  - content-extraction
  - twitter
  - markdown
  - no-api-key
  - jina-ai
requires:
  - python3
  - requests
---

# Jina AI Reader for OpenClaw

Extract clean, readable content from any webpage using Jina AI's free service.

## Overview

This Skill provides a lightweight way to extract content from websites without needing:
- Browser automation
- API keys
- Complex scraping logic
- JavaScript rendering

Perfect for:
- 📰 Reading news articles
- 🐦 Extracting Twitter/X threads
- 📚 Research and documentation
- 🤖 Feeding web content to LLMs

## Installation

```bash
# Copy the script to your OpenClaw tools directory
cp jina-reader.py ~/.openclaw/workspace/tools/
chmod +x ~/.openclaw/workspace/tools/jina-reader.py
```

Or use directly:
```bash
python3 jina-reader.py <url>
```

## Usage

### Command Line

```bash
# Basic usage
python3 jina-reader.py "https://example.com/article"

# Twitter/X mode
python3 jina-reader.py -t "https://x.com/username/status/1234567890"

# JSON output
python3 jina-reader.py -j "https://example.com"

# Save to file
python3 jina-reader.py -s output.md "https://example.com"
```

### In OpenClaw Sessions

```python
# Import and use
import sys
sys.path.insert(0, '~/.openclaw/workspace/tools')
from jina_reader import fetch_with_jina, fetch_tweet

# Get any webpage
result = fetch_with_jina("https://example.com/article")
print(result['markdown_content'])

# Get Twitter thread
tweet = fetch_tweet("https://x.com/username/status/1234567890")
print(tweet['tweet_text'])
```

## API Reference

### `fetch_with_jina(url)`

Extract content from any webpage.

**Parameters:**
- `url` (str): Target webpage URL

**Returns:**
```python
{
    'title': 'Page Title',
    'url': 'http://...',
    'published_time': '...',
    'markdown_content': 'Clean markdown...',
    'raw_content': 'Full response...'
}
```

### `fetch_tweet(tweet_url)`

Extract Twitter/X content with special handling.

**Parameters:**
- `tweet_url` (str): Twitter/X status URL

**Returns:**
```python
{
    'title': 'Username on X: "Tweet..."',
    'url': 'http://...',
    'tweet_text': 'Extracted tweet content...',
    'markdown_content': 'Full markdown...'
}
```

## Examples

### Example 1: Read a News Article
```bash
python3 jina-reader.py \
  "https://www.bloomberg.com/news/article"
```

### Example 2: Extract Twitter Thread
```bash
python3 jina-reader.py -t \
  "https://x.com/elonmusk/status/1234567890"
```

### Example 3: Research Assistant
```python
urls = [
    "https://example.com/crypto-article",
    "https://x.com/analyst/status/...",
    "https://docs.openclaw.ai"
]

for url in urls:
    content = fetch_with_jina(url)
    summarize(content['markdown_content'])
```

## How It Works

This Skill uses [Jina AI's r.jina.ai](https://r.jina.ai) service, which:
1. Fetches the target URL
2. Extracts main content using AI
3. Converts to clean Markdown
4. Returns structured data

**Advantages:**
- ✅ No API key needed
- ✅ Handles JavaScript-rendered content
- ✅ Removes ads and clutter
- ✅ Preserves article structure
- ✅ Works with paywalled content (sometimes)

## Limitations

- Rate limits may apply for heavy usage
- Some heavily JavaScript-dependent sites may not work perfectly
- Dynamic content (real-time updates) won't be captured
- Not suitable for pages requiring authentication

## Troubleshooting

### "Connection timeout"
Try increasing timeout in the script or check your network connection.

### "Empty content"
Some websites block scraping. Try accessing via browser first.

### "Not a valid URL"
Ensure URL includes protocol (https://) and is properly encoded.

## Contributing

Feel free to submit issues and PRs:
- Add new output formats
- Improve error handling
- Add proxy support
- Enhance Twitter extraction

## Credits

- Jina AI for providing the r.jina.ai service
- OpenClaw community for the framework

## License

MIT License - feel free to use in personal and commercial projects.
