from typing import List, Any

def get_user_data(user_id: int) -> Any:
    """
    Retrieves user data securely using parameterized queries.
    Prevents SQL injection by separating the query structure from the data.
    """
    # Assuming the use of a standard DB-API 2.0 driver (e.g., sqlite3, psycopg2)
    # The placeholder '?' is standard for many SQL drivers.
    sql_query = "SELECT * FROM users WHERE id = ?"
    return execute_query(sql_query, (user_id,))

def get_even_numbers(numbers: List[int]) -> List[int]:
    """
    Filters even numbers using a list comprehension for efficiency
    and improved readability.
    """
    return [num for num in numbers if num % 2 == 0]

def execute_query(query: str, params: tuple) -> Any:
    """
    Mock wrapper for database execution to demonstrate parameter passing.
    In production, this would interface with a connection object.
    """
    # Implementation logic for db connection execution would go here
    pass
