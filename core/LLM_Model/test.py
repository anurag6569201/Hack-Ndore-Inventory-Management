from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_community.vectorstores import Chroma
from blinklog.utils import getting_chunks_csv

import os
from dotenv import load_dotenv

load_dotenv()
google_gemini_api=os.getenv("GOOGLE_API_KEY")

text_chunks=getting_chunks_csv()

persist_directory="db"
embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vectordb=Chroma.from_documents(
    documents=text_chunks,
    embedding=embedding,
    persist_directory=persist_directory
)
vectordb.persist()
vectordb=None
vectordb=Chroma(persist_directory=persist_directory,embedding_function=embedding)


retriver=vectordb.as_retriever()

llm_model=ChatGoogleGenerativeAI(model="models/gemini-1.5-flash-latest",google_api_key=google_gemini_api)

system_prompt = (
    "You have an expertise on Muncipal corporation and you are well aware about the Muncipal Corporation Indore and You have all the information regarding the Indore"
    "You also have some additional data from the dataset of the IMC indore"
    "Provide the answer consisely"
    "use only the information you have dont be to grammatically"
    "Provide the answer Under 150 words"
    "Context: {context}"
)

from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)
question_answer_chain = create_stuff_documents_chain(llm_model, prompt)
chain = create_retrieval_chain(retriver, question_answer_chain)

# Basic memory class
class Memory:
    def __init__(self):
        self.history = []

    def add(self, entry):
        self.history.append(entry)
        if len(self.history) > 10:  # Limit the history size
            self.history.pop(0)

    def get_context(self):
        return " ".join(self.history)

memory = Memory()

def get_response(query):
    try:
        context = memory.get_context()
        response = chain.invoke({"input": query, "context": context})
        answer = response.get('answer', '')
        memory.add(f"User: {query}\nAI: {answer}")
        return answer
    except Exception as e:
        return "Sorry, I couldn't process your request."
