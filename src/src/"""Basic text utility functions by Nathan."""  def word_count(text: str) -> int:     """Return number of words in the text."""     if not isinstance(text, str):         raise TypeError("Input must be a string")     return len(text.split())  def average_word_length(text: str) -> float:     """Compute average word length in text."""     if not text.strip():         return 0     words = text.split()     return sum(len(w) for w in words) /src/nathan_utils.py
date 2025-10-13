"""Basic text utility functions by Nathan."""

def word_count(text: str) -> int:
    """Return number of words in the text."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return len(text.split())

def average_word_length(text: str) -> float:
    """Compute average word length in text."""
    if not text.strip():
        return 0
    words = text.split()
    return sum(len(w) for w in words) / len(words)

def clean_text(text: str) -> str:
    """Trim spaces and lowercase text."""
    return " ".join(text.strip().lower().split())
