from langchain.document_loaders import UnstructuredPDFLoader, OnlinePDFLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone
import os

links = ['Link1',
         'Link2',
         'Link3',]


def main2():
    print("Hello")
    for i in range(len(links)):
        uploaderOnline(links[i])
        print("Uploading " + str(i) + "th document")
    print("done with all")


def uploaderOnline(link):
    print("---------------------------------------------------------------------")
    loader = OnlinePDFLoader(link)
    data = loader.load()

    print(f'You have {len(data)} document(s) in your data (before processing)')

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=0)
    texts = text_splitter.split_documents(data)
    print(f'You have {len(texts)} document(s) (after processing)')

    OpenAiKey = "key123"
    PineconeKey = "key234"
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', OpenAiKey)
    PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY', PineconeKey)
    PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV', 'us-west')

    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

    pinecone.init(
        api_key=PINECONE_API_KEY,
        environment=PINECONE_API_ENV
    )
    index_name = "test"

    docsearch = Pinecone.from_texts([t.page_content for t in texts], embeddings, index_name=index_name)
    print("Succesfully updated database")

def uploaderLocal(path):
    print("---------------------------------------------------------------------")
    loader = UnstructuredPDFLoader(path)
    data = loader.load()

    print(f'You have {len(data)} document(s) in your data (before processing)')

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=0)
    texts = text_splitter.split_documents(data)
    print(f'You have {len(texts)} document(s) (after processing)')

    OpenAiKey = "key123"
    PineconeKey = "key234"
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', OpenAiKey)
    PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY', PineconeKey)
    PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV', 'us-west')

    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

    pinecone.init(
        api_key=PINECONE_API_KEY,
        environment=PINECONE_API_ENV
    )
    index_name = "test"

    docsearch = Pinecone.from_texts([t.page_content for t in texts], embeddings, index_name=index_name)
    print("Succesfully updated database")

main2()

