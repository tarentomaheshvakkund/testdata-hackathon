"""Insecure pickle deserialization."""
import pickle

def load_data(data_bytes):
    """VULNERABLE to pickle attacks."""
    return pickle.loads(data_bytes)
