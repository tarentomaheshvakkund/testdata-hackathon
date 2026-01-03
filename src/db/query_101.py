"""Database query with SQL injection vulnerability."""
import sqlite3

def get_user(user_id):
    """Get user by ID - VULNERABLE to SQL injection."""
    conn = sqlite3.connect('database.db')
    # VULNERABLE: Direct string formatting in SQL
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    return conn.execute(query).fetchone()

def search_users(name):
    """Search users - VULNERABLE."""
    conn = sqlite3.connect('database.db')
    query = "SELECT * FROM users WHERE name LIKE '%" + name + "%'"
    return conn.execute(query).fetchall()
