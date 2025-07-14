"""
This file contains the tools for the LLM.
"""
import sqlite3
from langchain_core.tools import tool


@tool("insert_data", return_direct=True)
def insert_data(query: str) -> bool:
    """
    Insert data into the database.
    """
    conn = sqlite3.connect("data.db")
    conn.execute(query)
    conn.commit()
    conn.close()
    return True


@tool("read_data", return_direct=True)
def read_data(query: str) -> list:
    """
    Read data from the database.
    """
    conn = sqlite3.connect("data.db")
    result = conn.execute(query).fetchall()
    conn.close()
    return result


@tool("update_data", return_direct=True)
def update_data(query: str) -> bool:
    """
    Update data in the database.
    """
    conn = sqlite3.connect("data.db")
    conn.execute(query)
    conn.commit()
    conn.close()
    return True


@tool("fetch_schema", return_direct=True)
def fetch_schema() -> list:
    """
    Fetch the schema of the database.
    """
    conn = sqlite3.connect("data.db")
    result = conn.execute("PRAGMA table_list").fetchall()
    conn.close()
    return result


@tool("create_table", return_direct=True)
def create_table(query: str) -> bool:
    """
    Create a table in the database.
    """
    conn = sqlite3.connect("data.db")
    conn.execute(query)
    conn.commit()
    conn.close()
    return True
