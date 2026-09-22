"""Starter code for the Building REST APIs with FastAPI assignment."""

from fastapi import FastAPI

app = FastAPI(title="Book Catalog API")

books = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"id": 2, "title": "Frankenstein", "author": "Mary Shelley"},
]


@app.get("/")
def read_root():
    """Return a health check for the API."""
    pass


@app.get("/books")
def read_books():
    """Return all books in the catalog."""
    pass


# Add the remaining endpoints from the assignment below.
# Run with: uvicorn starter-code:app --reload