import sqlite3
from typing import List, Any

# Assuming db_conn is initialized globally or passed as a dependency
# For production code, ensure db_conn is managed via a connection pool or context manager.

def get_user_data(db_conn: sqlite3.Connection, user_id: Any) -> List[tuple]:
    """
    Fetches user data using parameterized queries to prevent SQL injection.
    """
    query = "SELECT * FROM users WHERE id = ?"
    
    cursor = db_conn.cursor()
    try:
        cursor.execute(query, (user_id,))
        return cursor.fetchall()
    finally:
        cursor.close()

def get_even_numbers(numbers: List[int]) -> List[int]:
    """
    Returns a list of even numbers using a list comprehension for 
    improved performance and readability.
    """
    return [num for num in numbers if num % 2 == 0]
