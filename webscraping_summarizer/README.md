# 📰 Web Article Summarizer

A Streamlit application that scrapes web articles and generates AI-powered summaries using Groq's Mixtral model.

## Features

- 🔗 **Web Scraping**: Extract articles from any URL using newspaper3k
- 🤖 **AI Summarization**: Generate concise summaries using Groq's Mixtral-8x7b model
- 📊 **Article Analysis**: Display reading time, keywords, and full text
- 🎨 **Beautiful UI**: Clean Streamlit interface with emojis and expandable sections

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Get Groq API Key

1. Visit [Groq Console](https://console.groq.com/)
2. Sign up or log in
3. Create a new API key
4. Copy the API key

### 3. Environment Setup

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Replace `your_groq_api_key_here` with your actual Groq API key.

### 4. Run the Application

```bash
streamlit run web_scraper_summarizer.py
```

The application will open in your browser at `http://localhost:8501`

## Usage

1. **Enter URL**: Paste any article URL in the text input
2. **Click Summarize**: The app will scrape the article and generate a summary
3. **View Results**: 
   - Article title and reading time
   - AI-generated summary in bullet points
   - Extracted keywords
   - Full article text (expandable)

## Example URLs to Test

- News articles from major publications
- Blog posts
- Technical documentation
- Research papers

## Dependencies

- **Streamlit**: Web application framework
- **newspaper3k**: Article extraction and parsing
- **LangChain**: LLM integration framework
- **Groq**: High-performance LLM API
- **python-dotenv**: Environment variable management

## Troubleshooting

### Common Issues

1. **API Key Error**: Make sure your `.env` file is in the project root and contains the correct API key
2. **Article Extraction Failed**: Some websites may block scraping. Try different articles
3. **Dependencies**: Run `pip install -r requirements.txt` to install all dependencies

### Supported Article Types

- News articles
- Blog posts
- Documentation pages
- Most text-based web content

## License

This project is open source and available under the MIT License. 