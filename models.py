class Book:
    def __init__(self, title, author, year, isbn=None, quotes=None):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.quotes = quotes or []

    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'isbn': self.isbn,
            'quotes': self.quotes
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)