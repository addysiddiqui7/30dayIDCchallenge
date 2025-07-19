from fastapi import FastAPI , Depends , HTTPException
from pydantic import BaseModel
import uvicorn
#new necessary packages
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, Session

app = FastAPI()

# Database setup
DATABASE_URL = "sqlite:///./books.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# SQLAlchemy model
class BookDB(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    year = Column(Integer)

# Create tables
Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#from here the code is of previous model of day 26 
# and I changed it little bit as for sqlite

class Book(BaseModel):
    #'id: int' is removed as sqlite has index by default
    title: str
    author: str
    year: int

# this part -> 'library = []' is replaced 
# with actual database of sqlite

#from here we will implement CRUD end points

#GET – Retrieve all books
@app.get("/books")
def get_books(db: Session = Depends(get_db)):
    return db.query(BookDB).all()


#POST- Add a new book
@app.post("/books")
def add_book(book: Book, db: Session = Depends(get_db)):
    db_book = BookDB(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return {"message": "Book added successfully"}

#PUT - Update a book by id
@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book, db: Session = Depends(get_db)):
    book = db.query(BookDB).filter(BookDB.id == book_id).first()
    if book:
        for key, value in updated_book.dict().items():
            setattr(book, key, value)
        db.commit()
        return {"message": "Book updated successfully"}
    raise HTTPException(status_code=404, detail="Book not found")

#DELETE - remove a book by id
@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(BookDB).filter(BookDB.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
        return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")
