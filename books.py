from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    
    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        
class BookRequest(BaseModel):
    id: Optional[int] = Field(title="id is not needed")
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)
    
    class Config:
        schema_extra = {
            "example": {
                "title": "A new book",
                "author": "Frank Vargas",
                "description": "A new description of a book",
                "rating": 5
            }
        }
    

BOOKS = [
    Book(1, "Computer Science Pro", "Frank Vargas", "Very good Book", 5),
    Book(2, "In search of lost time", "Marcel Proust", "The greatest book", 5),
    Book(3, "Ulysses", "James Joyce", "Amazing Book", 4),
    Book(4, "The Odyssey ", "Homer", "It's alright", 2),
    Book(5, "The Iliad", "Homer", "Good Book", 3),
]

@app.get("/books")
async def get_all_books():
    return BOOKS

@app.get("/books/{book_id}")
async def get_book(book_id: int):
    for book in BOOKS:
        if book.id == book_id:
            return book

@app.post("/create-book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.dict())
    BOOKS.append(find_book_id(new_book))

def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book
