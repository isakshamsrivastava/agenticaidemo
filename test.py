from typing import List, Any

# Assuming a standard DB driver interface that supports parameterization
# e.g., sqlite3, psycopg2, or similar.
def get_user_data(user_id: int) -> Any:
    """
    Retrieves user data securely using parameterized queries to prevent SQL injection.
    """
    # Vulnerability fixed: Using parameter placeholders (?) instead of f-strings.
    # The database driver will safely escape the user_id input.
    query = "SELECT * FROM users WHERE id = ?"
    return execute_query(query, (user_id,))

def get_even_numbers(numbers: List[int]) -> List[int]:
    """
    Filters for even numbers using a list comprehension for better performance
    and readability.
    """
    # Modernized: List comprehension replaces manual indexing loop.
    return [num for num in numbers if num % 2 == 0]

def execute_query(query: str, params: tuple = ()) -> Any:
    """
    Placeholder for the database execution logic.
    """
    # This would typically be your database cursor execution method.
    pass
