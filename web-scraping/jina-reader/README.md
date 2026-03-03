# Jina AI Reader for OpenClaw

[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-blue)](https://openclaw.ai)
[![Python](https://img.shields.io/badge/Python-3.8+-green)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

> Extract clean, readable content from any webpage using Jina AI's free service.

## ✨ Features

- 🚀 **No API Key Required** - Free to use, no authentication needed
- 📝 **Clean Markdown Output** - Converts messy HTML to readable Markdown
- 🐦 **Twitter/X Support** - Special handling for tweets and threads
- ⚡ **Lightweight** - Single Python script, minimal dependencies
- 🔧 **Easy Integration** - Works in OpenClaw sessions or standalone

## 📦 Installation

```bash
# Clone or download
git clone https://github.com/josecookai/awesome-openclaw-skills.git
cd awesome-openclaw-skills/web-scraping/jina-reader

# Make executable
chmod +x jina-reader.py

# Or copy to OpenClaw tools
cp jina-reader.py ~/.openclaw/workspace/tools/
```

## 🚀 Quick Start

### Command Line

```bash
# Read any webpage
python3 jina-reader.py "https://example.com/article"

# Extract Twitter/X content
python3 jina-reader.py -t "https://x.com/username/status/1234567890"

# Save to file
python3 jina-reader.py -s article.md "https://example.com"
```

### In OpenClaw

```python
# Get web content
fetch_with_jina("https://example.com/article")

# Get tweet
fetch_tweet("https://x.com/username/status/1234567890")
```

## 📖 Usage Examples

### Example 1: Research Assistant

```python
import sys
sys.path.insert(0, '~/.openclaw/workspace/tools')
from jina_reader import fetch_with_jina

# Collect sources for analysis
urls = [
    "https://example.com/crypto-news",
    "https://x.com/analyst/status/...",
    "https://docs.project.io"
]

for url in urls:
    result = fetch_with_jina(url)
    print(f"Title: {result['title']}")
    print(f"Content: {result['markdown_content'][:500]}...")
```

### Example 2: Twitter Thread Reader

```python
from jina_reader import fetch_tweet

# Extract full Twitter thread
tweet = fetch_tweet("https://x.com/crypnuevo/status/...")
print(tweet['tweet_text'])
```

### Example 3: News Aggregation

```bash
# Create daily news digest
python3 jina-reader.py -s news1.md "https://site1.com/article"
python3 jina-reader.py -s news2.md "https://site2.com/article"
python3 jina-reader.py -s news3.md "https://site3.com/article"

# Combine
cat news*.md > daily-digest.md
```

## 🔧 API Reference

### Functions

#### `fetch_with_jina(url)`

Extract content from any webpage.

**Parameters:**
- `url` (str): Target URL

**Returns:**
```python
{
    'title': 'Page Title',
    'url': 'http://...',
    'published_time': '...',
    'markdown_content': 'Clean markdown...'
}
```

#### `fetch_tweet(tweet_url)`

Extract Twitter/X content.

**Parameters:**
- `tweet_url` (str): Twitter/X status URL

**Returns:**
```python
{
    'title': '...',
    'tweet_text': 'Extracted content...',
    'markdown_content': '...'
}
```

## 🛠️ How It Works

This tool uses [Jina AI's r.jina.ai](https://r.jina.ai) service:

1. Sends URL to `https://r.jina.ai/http://<target-url>`
2. Jina AI fetches and processes the page
3. Returns clean Markdown content
4. Parses structured data (title, content, metadata)

**No browser automation needed!**

## ✅ Requirements

- Python 3.8+
- `requests` library

```bash
pip install requests
```

## 🎯 Use Cases

| Scenario | Command |
|----------|---------|
| Read article | `python3 jina-reader.py "https://..."` |
| Get tweet | `python3 jina-reader.py -t "https://x.com/..."` |
| Research | Use `fetch_with_jina()` in Python |
| Batch process | Loop through URLs |

## ⚠️ Limitations

- Rate limits apply for heavy usage
- Some JavaScript-heavy sites may not work perfectly
- Not suitable for pages requiring login
- Real-time dynamic content won't update

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Submit a Pull Request

## 📝 License

MIT License - feel free to use in personal and commercial projects.

## 🙏 Credits

- [Jina AI](https://jina.ai) for the r.jina.ai service
- [OpenClaw](https://openclaw.ai) community

---

Made with ❤️ by BoxATH (@chainblackbox)
