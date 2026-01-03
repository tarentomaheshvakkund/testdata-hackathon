"""Service with debug prints."""

def get_user(user_id):
    print(f"Getting user: {user_id}")
    user = fetch_from_db(user_id)
    print(f"Found: {user}")
    return user
