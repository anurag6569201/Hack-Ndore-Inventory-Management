import os
import sqlite3
from dotenv import load_dotenv
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_chroma import Chroma
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()
google_gemini_api = os.getenv("GOOGLE_API_KEY")

tables_list_obj = ['assets_manage_asset', 'assets_manage_vehicle', 'core_problem', 'core_ambulance', 'core_bedsinventory', 'core_o2inventory', 'core_staffmember', 'maintain_maintenancetask', 'core_labor', 'core_attendance', 'core_taskassignment', 'core_task']

def fetch_table_data_chunks(table_list):
    conn = sqlite3.connect('db.sqlite3')  # Ensure this path is correct
    table_data = {}
    ̀
    try:
        with conn:
            cursor = conn.cursor()
            
            for table_name in table_list:
                try:
                    cursor.execute(f"SELECT * FROM {table_name};")
                    rows = cursor.fetchall()
                    
                    cursor.execute(f"PRAGMA table_info({table_name});")
                    columns = cursor.fetchall()
                    headers = [column[1] for column in columns]
                    
                    if rows:
                        table_data[table_name] = {"headers": headers, "rows": rows}
                
                except sqlite3.Error as e:
                    print(f"Error processing table {table_name}: {e}")
    
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    
    docs = [
        f"Table: {table_name}\nHeaders: {', '.join(data['headers'])}\nRow: {', '.join(map(str, row))}"
        for table_name, data in table_data.items()
        for row in data['rows']
    ]
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    text = '\n'.join(docs)
    chunks = text_splitter.split_text(text)
    
    documents = [Document(page_content=chunk) for chunk in chunks]
    
    print(f"Generated {len(documents)} documents with content.")
    return documents

text_chunks = fetch_table_data_chunks(tables_list_obj)

if not text_chunks:
    raise ValueError("text_chunks is empty")

persist_directory = "db"
embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vectordb = Chroma.from_documents(documents=text_chunks, embedding=embedding, persist_directory=persist_directory)

retriever = vectordb.as_retriever()
llm_model = ChatGoogleGenerativeAI(model="models/gemini-1.5-pro", google_api_key=google_gemini_api)

system_prompt = (
    "You are an expert on the Municipal Corporation of Indore with access to detailed data. "
    "Answer questions based on this information, using concise and relevant details from the dataset. "
    "Context: {context}"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)
question_answer_chain = create_stuff_documents_chain(llm_model, prompt)
chain = create_retrieval_chain(retriever, question_answer_chain)

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
    context = memory.get_context() + f" Recent query: {query}"
    print(f"Query: {query}\nContext: {context}")
    try:
        response = chain.invoke({"input": query, "context": context})
        answer = response.get('answer', '')
        print(f"Answer: {answer}")
        memory.add(f"User: {query}\nAI: {answer}")
        return answer
    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, I couldn't process your request."
