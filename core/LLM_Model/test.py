import os
import sqlite3
from dotenv import load_dotenv
import schedule
import time

from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import Chroma  # Updated import
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from blinklog.utils import getting_chunks_pdf

load_dotenv()
google_gemini_api = os.getenv("GOOGLE_API_KEY")
persist_directory = "db"
embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# Initialize text_splitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

from langchain.schema import Document  # Import the Document class

def update_knowledge_base():
    pdf_text_chunks = getting_chunks_pdf()
    
    # Process SQLite database
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    
    # Fetch all tables except the user model
    tables = [row[0] for row in cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")]
    tables = [table for table in tables if table != 'User']  # Exclude 'user' model
    
    db_text_chunks = []
    for table in tables:
        cursor.execute(f'SELECT * FROM {table}')
        rows = cursor.fetchall()
        for row in rows:
            text = ' '.join(map(str, row))  # Convert row data to a single string
            doc = Document(page_content=text)  # Create a Document object
            chunks = text_splitter.split_documents([doc])  # Pass Document objects to the splitter
            db_text_chunks.extend(chunks)
    
    conn.close()
    
    # Combine text chunks from both sources
    all_text_chunks = pdf_text_chunks + db_text_chunks
    
    # Update vector store
    global vectordb
    vectordb = Chroma.from_documents(
        documents=all_text_chunks,
        embedding=embedding,
        persist_directory=persist_directory
    )

update_knowledge_base()  # Initial load

schedule.every().hour.do(update_knowledge_base)

llm_model = ChatGoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=google_gemini_api)

system_prompt = (
    "You have an expertise on Municipal corporation and you are well aware about the Municipal Corporation Indore and You have all the information regarding the Indore."
    "You also have some additional data from the dataset of the IMC Indore."
    "Provide the answer concisely."
    "Provide the answer under 150 words."
    "Context: {context}"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)
question_answer_chain = create_stuff_documents_chain(llm_model, prompt)
chain = create_retrieval_chain(vectordb.as_retriever(), question_answer_chain)

class Memory:
    def __init__(self):
        self.history = []

    def add(self, entry):
        self.history.append(entry)
        if len(self.history) > 10:
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

while True:
    schedule.run_pending()
    time.sleep(1)
