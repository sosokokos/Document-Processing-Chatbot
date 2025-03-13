# DocumentAI


## **Overview**
AmedAI is a Python-based document processing and chatbot system that utilizes LangChain for text processing and OpenAI embeddings for similarity search. It integrates with Pinecone to store and query vectorized document chunks efficiently.
---

## **Features**
- Load PDF documents from local storage or online sources
- Convert PDFs to text for processing
- Chunk text into smaller segments (~200 words per chunk)
- Convert text chunks into embeddings using OpenAI
- Store embeddings in a Pinecone vector database
- Perform similarity search to retrieve relevant document sections
- Query a chatbot with context-aware responses based on document data

---
# Usage
## 1. Load Data
- The system provides two methods for loading PDFs:
  - uploaderOnline(link): Uses OnlinePDFLoader from LangChain to load documents from a URL
  - uploaderLocal(path): Uses UnstructuredPDFLoader from LangChain to load documents from a local file
- After loading, the PDF is converted into a text document

## 2. Process Data
- Text is split into chunks (~200 words each)
- The openAIEmbeddings() function converts each chunk into a numerical vector representation

## 3. Store Data in Pinecone
- A Pinecone index is initialized with a dimension of 1536, optimized for OpenAI’s embeddings
- The generated embeddings are uploaded to the Pinecone cloud database

## 4. Interact with the Chatbot
- When running main.py, the program provides a CLI menu with options to:
  - Upload more documents
  - Query the chatbot
  - Querying the chatbot:
- The input question is vectorized using OpenAI embeddings
- A similarity search is performed in Pinecone using cosine similarity
- The three most relevant chunks are retrieved and used as context in an OpenAI API request
- The chatbot responds based on the retrieved document information
- If no relevant data is found, the chatbot notifies the user
