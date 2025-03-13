import os
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
import pinecone
import loader as load



def main():
    print("------------------Hello User--------------------")
    displayMenu()


def displayMenu():
    print("---------Select one of the options---------")
    print("0. Exit the Program")
    print("1.  Upload documents")
    print("2.  Ask Chatbot")
    userInput = input("Your selection: ")

    if userInput == str(0):
        return
    elif userInput == str(1):
        print("------------------Uploading Documents---------------------")
        print("1. Locally stored (Filepath)")
        print("2. Online storage (Link to website)")
        inputDocStorage = input("Where is your PDF document stored? ")

    elif userInput == str(2):
        askQuestion()
        return
    else:
        print("Invalid input, try again")
        displayMenu()

def askQuestion():
    userInput = input("Enter your question here: ")
    searchResult = querry(userInput)
    print("The answer to your question > " + userInput + " < is == " + searchResult)

    anotherQuestion = input("Do you want to ask additional question? (Yes/No) : ")
    if anotherQuestion == "YES" or "Yes" or "yes" or "Y" or "y":
        askQuestion()
    elif anotherQuestion == "NO" or "No" or "no" or "N" or "n":
        return
    else:
        return

def querry(input):
    query = input

    OpenAiKey = "key123"
    PineconeKey = "key234"

    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', OpenAiKey)
    PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY', PineconeKey)
    PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV', 'us-west')

    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_API_ENV)

    vectorstore = Pinecone.from_existing_index(index_name='test', embedding=embeddings)
    documents = vectorstore.similarity_search(query)

    llm = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)
    chain = load_qa_chain(llm, chain_type="stuff")

    docs = documents[:3]

    return chain.run(input_documents=docs, question=query)

main()