import os

def extract_file_metadata(file_path):
    """Get basic info about a file.
    
    Args:
        file_path (str): The location of the file.
        
    Returns:
        dict: Includes name, type, and size in KB.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError("File does not exist.")
    
    file_name = os.path.basename(file_path)
    file_type = file_name.split(".")[-1]
    file_size = round(os.path.getsize(file_path) / 1024, 2)
    
    return {"name": file_name, "type": file_type, "size_kb": file_size}


def tokenize_text(text):
    """Break text into lowercase words.
    
    Args:
        text (str): A string of text.
        
    Returns:
        list: List of lowercase words.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    
    text = text.lower()
    words = text.split()
    return words


def count_word_frequency(words):
    """Count how many times each word appears.
    
    Args:
        words (list): List of words.
        
    Returns:
        dict: Word counts.
    """
    if not isinstance(words, list):
        raise TypeError("Input must be a list of words.")
    
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


def find_keyword_in_text(text, keyword):
    """Check if a keyword appears in a text.
    
    Args:
        text (str): The text to search.
        keyword (str): The word to find.
        
    Returns:
        bool: True if found, False if not.
    """
    if not all(isinstance(x, str) for x in [text, keyword]):
        raise TypeError("Both text and keyword must be strings.")
    
    return keyword.lower() in text.lower()


def make_snippet(text, keyword):
    """Make a short snippet showing where the keyword appears.
    
    Args:
        text (str): Full text.
        keyword (str): Word to highlight.
        
    Returns:
        str: Short snippet with keyword in the middle.
    """
    text_lower = text.lower()
    index = text_lower.find(keyword.lower())
    
    if index == -1:
        return text[:60] + "..." if len(text) > 60 else text
    
    start = max(0, index - 20)
    end = min(len(text), index + len(keyword) + 20)
    snippet = text[start:end]
    return f"...{snippet}..."
