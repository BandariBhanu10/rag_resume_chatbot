# rag_resume_chatbot
Resume RAG Chatbot - Upload PDF resumes and ask AI-powered questions. Built with Streamlit, LangChain, FAISS, and Groq API for intelligent document analysis.

# Resume RAG Chatbot

A Streamlit-based Retrieval-Augmented Generation (RAG) chatbot that allows users to upload PDF resumes and ask questions about them using AI.

## Features

✨ **PDF Resume Upload** - Upload and process PDF resumes  
🤖 **AI-Powered Answers** - Get intelligent responses based on resume content using Groq API  
🔍 **Semantic Search** - FAISS vector store for accurate information retrieval  
⚡ **Fast & Efficient** - Optimized text chunking and embeddings  
🔐 **Secure** - API keys stored in .env file  

## Tech Stack

- **Frontend:** Streamlit
- **LLM:** Groq API (llama-3.3-70b-versatile)
- **Framework:** LangChain
- **Vector Store:** FAISS
- **PDF Processing:** PyMuPDF
- **Language:** Python 3.11+

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/rag_resume_chatbot.git
   cd rag_resume_chatbot
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up API keys:**
   - Create a `.env` file in the root directory
   - Add your Groq API key:
     ```
     GROQ_API_KEY=your_api_key_here
     ```
   - Get your key from [Groq Console](https://console.groq.com)

## Usage

1. **Run the app:**
   ```bash
   streamlit run app.py
   ```

2. **Access the web interface:**
   - Open http://localhost:8502 in your browser

3. **Upload a resume:**
   - Click the file uploader
   - Select a PDF resume

4. **Ask questions:**
   - Type any question about the resume
   - Get AI-powered answers based on the content

## Project Structure

```
rag_resume_chatbot/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env                  # API keys (not committed)
├── .gitignore            # Git ignore rules
├── README.md             # This file
├── data/
│   └── sample.txt        # Sample data
└── resume/               # Uploaded resumes storage
```

## Requirements

- Python 3.11+
- pip
- Groq API key (free tier available)

## Troubleshooting

**"Model has been decommissioned":**
- Update the model name in `app.py`
- Check [Groq Deprecations](https://console.groq.com/docs/deprecations)

**"API key not found":**
- Ensure `.env` file exists in root directory
- Check GROQ_API_KEY is set correctly

**"PDF upload fails":**
- Ensure PDF is text-based (not scanned image)
- Maximum file size limits may apply

## Future Enhancements

- 🎯 Support for multiple resume formats (DOCX, TXT)
- 🧠 Better embeddings using sentence-transformers
- 📊 Resume analysis and scoring
- 💾 Chat history persistence
- 🔄 Batch resume processing

## License

MIT License

## Author

Created as a Resume RAG Chatbot application.

## Support

For issues and questions, please open an issue in the GitHub repository.

