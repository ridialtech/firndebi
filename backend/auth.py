"""Simple authentication module."""

def authenticate(username: str, password: str) -> bool:
    """Return True if credentials are correct."""
    if not username or not password:
        return False
    return username == "admin" and password == "secret"
