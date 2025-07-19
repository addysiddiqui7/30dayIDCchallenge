from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int

library = []

#from here we will implement CRUD end points

#GET – Retrieve all books
@app.get("/books")
def get_books():
    return library


#POST- Add a new book
@app.post("/books")
def add_book(book: Book):
    library.append(book)
    return {"message": "Book added successfully"}

#PUT - Update a book by id
@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    for index, book in enumerate(library):
        if book.id == book_id:
            library[index] = updated_book
            return {"message": "Book updated successfully"}
    return {"error": "Book not found"}

#DELETE - remove a book by id
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for book in library:
        if book.id == book_id:
            library.remove(book)
            return {"message": "Book deleted successfully"}
    return {"error": "Book not found"}
