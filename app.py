import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.vectorstores import FAISS
from langchain.embeddings.base import Embeddings

# Load API Key
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("❌ GROQ_API_KEY not found in .env file")
    st.info("**How to fix:**\n1. Get your Groq API key from https://console.groq.com/keys\n2. Open `.env` file in this folder\n3. Add: `GROQ_API_KEY=your_groq_key_here`\n4. Save and refresh this page")
    st.stop()

# Validate API key format
if not GROQ_API_KEY.startswith("gsk_"):
    st.error("❌ Invalid Groq API key format. Should start with 'gsk_'")
    st.info(f"Current key starts with: {GROQ_API_KEY[:10]}...")
    st.stop()

try:
    client = Groq(api_key=GROQ_API_KEY)
except Exception as e:
    st.error(f"❌ Failed to authenticate with Groq: {str(e)}")
    st.info("Your API key may be expired or invalid. Get a new one from https://console.groq.com/keys")
    st.stop()

# Streamlit UI
st.set_page_config(page_title="Resume RAG Chatbot", layout="wide")
st.title("📄 Resume RAG Chatbot")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

if not uploaded_file:
    st.info("👆 Upload a PDF resume to get started")
    st.stop()

# Save PDF
with open("resume.pdf", "wb") as f:
    f.write(uploaded_file.getbuffer())

# Load PDF
try:
    loader = PyMuPDFLoader("resume.pdf")
    documents = loader.load()
except Exception as e:
    st.error(f"Error loading PDF: {str(e)}")
    st.stop()

if not documents:
    st.error("No readable text found in PDF")
    st.stop()

# Split text
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
docs = splitter.split_documents(documents)

# Simple local embeddings
class SimpleEmbeddings(Embeddings):
    def embed_documents(self, texts):
        return [[float(hash(t + str(i)) % 100) for i in range(384)] for t in texts]
    def embed_query(self, text):
        return [float(hash(text + str(i)) % 100) for i in range(384)]

vectorstore = FAISS.from_documents(docs, SimpleEmbeddings())

st.success(f"✅ Resume loaded! ({len(docs)} chunks)")

query = st.text_input("Ask a question about your resume:")

if query:
    with st.spinner("Thinking..."):
        # Retrieve relevant docs
        retrieved_docs = vectorstore.similarity_search(query, k=3)
        context = "\n\n".join([d.page_content for d in retrieved_docs])
        
        # Generate answer using Groq
        prompt = f"""Use this resume context to answer the question.
If you cannot find the answer in the context, say "I don't know".

CONTEXT:
{context}

QUESTION: {query}

ANSWER:"""
        
        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that answers questions based on resume content."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=1024
            )
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"❌ API Error: {str(e)}")
            if "API Key" in str(e) or "Unauthorized" in str(e):
                st.info("Your API key is invalid. Get a new one from https://console.groq.com/keys")
            elif "Rate limit" in str(e):
                st.warning("⏳ Rate limit exceeded. Try again in a moment.")
            st.stop()