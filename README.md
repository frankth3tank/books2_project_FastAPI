# Books2 Project with FastAPI
This is a simple CRUD (Create, Read, Update, Delete) application built with Python's FastAPI framework. The application is designed to manage a catalog of books, allowing users to create, read, update, and delete books from the catalog.

## Prerequisites
Before you can use this application, you will need to have the following installed on your machine:

- Python 3.7 or higher
- pip

## Installation
1. Clone this repository to your local machine.
```
git clone https://github.com/frankth3tank/books2_project_FastAPI.git
```
2. Change into the project directory.
```
cd books2_project_FastAPI
```
3. Create a virtual environment and activate it.
```
python -m venv env
source env/bin/activate
```
4. Install the dependencies.
```
pip install -r requirements.txt
```

## Usage
1. Start the API server.
```
uvicorn books2:app --reload
```
2. Navigate to http://localhost:8000/docs in your web browser to access the Swagger UI. Here, you can test the different endpoints available in the API.

## Endpoints
- `GET /books` Returns a list of all books.
- `GET /books/{book_id}` Returns the details of a single book by providing the id.
- `GET /books/?book_rating` Returns a list of all books that match a specific rating.
- `GET /books/published/?published_date` Returns a list of all books that match a specific published date.
- `POST /books/create_book` Creates a new book.
- `PUT /books/update_book` Updates the details of a book that matches the id.
- `DELETE /books/{book_id}` Deletes a book that matches the id.

## Contributing
If you would like to contribute to this project, please open a pull request. We welcome contributions of all kinds, including bug fixes, new features, and documentation improvements.

## License
This project is licensed under the MIT License.