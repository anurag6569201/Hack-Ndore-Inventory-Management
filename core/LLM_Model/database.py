import sqlite3
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

# function for fetching the table names from the sqlite3 database
def fetch_table_name():
    conn = sqlite3.connect('../../db.sqlite3')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    table_names = [table[0] for table in tables]
    conn.close()
    return table_names

print(fetch_table_name())

['assets_manage_asset', 'assets_manage_vehicle', 'core_problem', 'core_ambulance', 'core_bedsinventory', 'core_o2inventory', 'core_staffmember', 'maintain_maintenancetask', 'core_labor', 'core_attendance', 'core_taskassignment', 'core_task']