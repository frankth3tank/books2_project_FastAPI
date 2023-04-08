from fastapi import FastAPI

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


