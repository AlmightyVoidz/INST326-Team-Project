"""Basic text utility functions by Nathan."""

def word_count(text: str) -> int:
    """Return number of words in the text."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return len(text.split())

def average_word_length(text: str) -> float:
    """Compute average word length in text."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    words = text.split()
    if not words:
        return 0.0
    return sum(len(w) for w in words) / len(words)

def clean_text(text: str) -> str:
    """Trim spaces and lowercase text."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return " ".join(text.strip().lower().split())

def contains_keyword(text: str, keyword: str) -> bool:
    """Check if keyword appears in text (case-insensitive)."""
    if not isinstance(text, str) or not isinstance(keyword, str):
        raise TypeError("Both inputs must be strings")
    return keyword.lower() in text.lower()

def summarize_text(text: str, limit: int = 10) -> str:
    """Return the first `limit` words of text."""
    if not isinstance(text, str):
        raise TypeError("Text must be a string")
    if not isinstance(limit, int) or limit <= 0:
        raise ValueError("Limit must be a positive integer")
    return " ".join(text.split()[:limit])
