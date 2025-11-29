import json
from models import Book

def load_books(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Book.from_dict(item) for item in data]
    except FileNotFoundError:
        return FileNotFoundError("File not found")
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format in storage file")

def save_books(books, filepath):
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump([book.to_dict() for book in books], f, indent=2, ensure_ascii=False)
    except IOError as e:
        raise IOError(f"Failed to save books: {e}")