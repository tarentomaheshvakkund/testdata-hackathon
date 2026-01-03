"""Configuration with hardcoded secrets."""

API_KEY = "sk-1234567890abcdef1234567890abcdef"
AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE123456789"
DATABASE_PASSWORD = "SuperSecretPassword123!"

def get_db_connection():
    password = "admin123"
    return f"postgresql://admin:{password}@localhost/db"
