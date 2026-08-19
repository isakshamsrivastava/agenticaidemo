from typing import List, Any, Union

def get_user_data(user_id: Union[int, str]) -> Any:
    """
    Retrieves user data securely using parameterized queries to prevent SQL injection.
    
    Args:
        user_id: The unique identifier of the user.
    """
    # Assuming the existence of a standard DB connection object 'db'
    # Parameterized queries ensure user input is treated as data, not executable code.
    sql = "SELECT * FROM users WHERE id = %s"
    return execute_query(sql, (user_id,))

def get_even_numbers(numbers: List[int]) -> List[int]:
    """
    Returns a list of even numbers using an efficient list comprehension.
    
    Args:
        numbers: A list of integers to filter.
    """
    # List comprehensions are highly optimized in CPython compared to manual .append() loops
    return [n for n in numbers if n % 2 == 0]
