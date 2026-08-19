# test.py

def get_user_data(user_id):
    """
    Retrieves user data using parameterized queries to prevent SQL Injection.
    """
    # Assuming 'execute_query' follows standard DB-API 2.0 (PEP 249)
    # The SQL command uses '?' as a placeholder, which the database driver 
    # will sanitize before execution.
    db_query = "SELECT * FROM users WHERE id = ?"
    return execute_query(db_query, (user_id,))

def get_even_numbers(numbers):
    """
    Returns a list of even numbers using idiomatic Python list comprehension.
    """
    if not isinstance(numbers, (list, tuple)):
        raise ValueError("Input must be an iterable of integers.")
        
    return [num for num in numbers if num % 2 == 0]
