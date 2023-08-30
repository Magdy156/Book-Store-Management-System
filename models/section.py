#!/usr/bin/python3
"""Section class"""


class Section:
    """Represents a section"""
    __books = []

    def __init__(self, title) :
        """constructor"""
        self.__title = title

    def getTitle(self):
        """Return title of the section"""
        return (self.__title)

    def addBook(self, bookObj):
        """adds a Book to the books list"""
        Section.__books.append(bookObj)

    def searchBookByTitle(self, bookTitle):
        """searches for a book in the book list by its title"""
        for book in Section.__books:
            if book.getTitle() == bookTitle:
                return (book)
        return (None)

    def searchBookByAuthor(self, authorName):
        """ searches for all books in the book list by the author"""
        authorBooks = []
        for book in Section.__books:
            if book.getAuthor() == authorName:
                authorBooks.append(book)
        return (authorBooks)

    def deleteBook(self, bookTitle):
        """it deletes a book from the book list using its title"""
        for book in Section.__books:
            if book.getTitle() == bookTitle:
                Section.__books.remove(bookTitle)
                break

    def showBooks(self):
        """prints all the books in the section"""
        for book in Section.__books:
            print(f"Title: {book.getTitle()}")
            print(f"Author: {book.getAuthor()}")
            print(f"Cost: {book.getCost()}")
            print("--------------------------------")
