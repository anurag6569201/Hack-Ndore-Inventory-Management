from langchain_community.vectorstores import Chroma
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

def getting_chunks_csv():
    csvs_directory = os.path.join(BASE_DIR, 'media/pdfs')
    documents = []

    for filename in os.listdir(csvs_directory):
        if filename.endswith('.csv'):
            file_path = os.path.join(csvs_directory, filename)
            df = pd.read_csv(file_path)

            text = df.to_string(index=False)
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            chunks = text_splitter.split_text(text)
            
            # Convert text chunks to Document objects
            for chunk in chunks:
                documents.append(Document(page_content=chunk))

    return documents
