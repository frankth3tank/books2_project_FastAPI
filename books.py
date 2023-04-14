from typing import Optional
from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int
    
    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date
        
class BookRequest(BaseModel):
    id: Optional[int] = Field(title="id is not needed")
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)
    published_date: int = Field(gt=1000, lt=2024)
    
    class Config:
        schema_extra = {
            "example": {
                "title": "A new book",
                "author": "Frank Vargas",
                "description": "A new description of a book",
                "rating": 5,
                "published_date": 2023
            }
        }

BOOKS = [
    Book(1, "Computer Science Pro", "Frank Vargas", "Very good Book", 5, 2023),
    Book(2, "In search of lost time", "Marcel Proust", "The greatest book", 5, 1913),
    Book(3, "Ulysses", "James Joyce", "Amazing Book", 4, 1920),
    Book(4, "The Odyssey ", "Homer", "It's alright", 2, 1614),
    Book(5, "The Iliad", "Homer", "Good Book", 3, 1598),
]

@app.get("/books")
async def get_all_books():
    return BOOKS

@app.get("/books/{book_id}")
async def get_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Item not found")
        
@app.get("/books/")
async def get_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return

@app.get("/books/published/")
async def get_book_by_published_date(published_date: int = Query(gt=1000, lt=2024)):
    books_to_return = []
    for book in BOOKS:
        if book.published_date == published_date:
            books_to_return.append(book)
    return books_to_return

@app.post("/create-book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.dict())
    BOOKS.append(find_book_id(new_book))
    
@app.put("/books/update_book")
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changed = True
    if not book_changed:
        raise HTTPException(status_code=404, detail="Item not found")
            
@app.delete("/books/{book_id}")
async def delete_book(book_id: int = Path(gt=0)):
    book_deleted = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_deleted = True
            break
    if not book_deleted:
        raise HTTPException(status_code=404, detail="Item not found")

def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book
