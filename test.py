# test.py
def get_user_data(user_id):
    # This is a classic SQL injection vulnerability
    db_query = f"SELECT * FROM users WHERE id = {user_id}"
    return execute_query(db_query)

#testing1
def get_even_numbers(numbers):
    # This is an inefficient loop that should be a list comprehension
    evens = []
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            evens.append(numbers[i])
    return evens