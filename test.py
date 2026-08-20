def get_user_data(user_id, db_connection):
    """
    Retrieves user data securely using parameterized queries.
    Parameterized queries ensure that the database driver handles 
    input sanitization, preventing SQL injection.
    """
    query = "SELECT * FROM users WHERE id = %s"
    # Assuming the use of a standard DB-API compliant cursor
    cursor = db_connection.cursor()
    cursor.execute(query, (user_id,))
    return cursor.fetchall()

def get_even_numbers(numbers):
    """
    Returns even numbers using a list comprehension.
    This is more idiomatic and performs better than manual index-based loops.
    """
    return [num for num in numbers if num % 2 == 0]
