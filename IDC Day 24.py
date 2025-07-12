'''Create a dataclass to represent a library book with fields for 
title, author, ISBN, and publication year, 
including a method to display book details'''
from dataclasses import dataclass
@dataclass
class Library:
    title : str
    author : str
    ISBN : int
    publication_year : int

    def book_info(self):
        return (
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"ISBN: {self.ISBN}\n"
            f"Publication Year: {self.publication_year}"
        )
    
Book1 = Library(
    title = "To Kill a Mockingbird",
    author = "Harper Lee",
    ISBN = 9780061120084,
    publication_year = 1960
)

print(Book1.book_info())

