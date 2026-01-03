"""Cryptography with weak algorithms."""
import hashlib

def hash_password(password):
    """Hash using MD5 - WEAK."""
    return hashlib.md5(password.encode()).hexdigest()

def hash_data(data):
    """Hash using SHA1 - WEAK."""
    return hashlib.sha1(data.encode()).hexdigest()
