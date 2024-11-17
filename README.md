# Website Summarizer

A Python tool that uses Ollama and LLMs to generate concise summaries of web content.

## Description

This tool fetches content from any given website URL, processes the text content, and uses Ollama (with LLaMA model) to generate a summary. Users can optionally specify a maximum word count for the summary.

## Features

- Web content extraction with BeautifulSoup
- Automatic removal of scripts, styles, and images from content
- Configurable summary length
- Integration with Ollama API
- Support for environment variables

## Prerequisites

- Python 3.9+
- Ollama installed and running locally
- Active internet connection

## Installation

1. Clone the repository: 
```bash
git clone <repository-url>
cd website-summarizer
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate # On Windows, use .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory with:
OLLAMA_HOST=http://localhost:11434/api/chat

## Usage

Run the script:
```bash
python main.py
```

Follow the prompts to:
1. Enter the website URL you want to summarize
2. Specify maximum word count (or 0 for no limit)

## Project Structure

```
website-summarizer/
├── main.py           # Main application file
├── Website.py        # Website class for content extraction
├── requirements.txt  # Project dependencies
├── .env             # Environment variables (create this)
└── README.md        # This file
```

## Dependencies

- requests: For HTTP requests
- beautifulsoup4: For HTML parsing
- python-dotenv: For environment variable management
- ipython: For display functionality
- ollama: For LLM integration

