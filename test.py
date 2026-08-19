# test.py
from typing import List, Any

def get_user_data(user_id: int) -> Any:
    """
    Retrieves user data securely using parameterized queries to prevent SQL injection.
    Note: 'execute_query' must support parameter binding (e.g., using '?' or '%s').
    """
    # Fix: Use parameter binding instead of f-string interpolation
    query = "SELECT * FROM users WHERE id = %s"
    return execute_query(query, (user_id,))

def get_even_numbers(numbers: List[int]) -> List[int]:
    """
    Filters even numbers using a list comprehension for better performance 
    and idiomatic readability.
    """
    # Fix: Use list comprehension for efficient, Pythonic filtering
    return [n for n in numbers if n % 2 == 0]
