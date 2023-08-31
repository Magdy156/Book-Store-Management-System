#!/usr/bin/python3
"""Section class"""


class Section:
    """Represents a section"""
    books = []

    def __init__(self, title) :
        """constructor"""
        self.__title = title

    def getTitle(self):
        """Return title of the section"""
        return (self.__title)

    def addBook(self, bookObj):
        """adds a Book to the books list"""
        Section.books.append(bookObj)

    def searchBookByTitle(self, bookTitle):
        """searches for a book in the book list by its title"""
        for book in Section.books:
            if book.getTitle() == bookTitle:
                return (book)
        return (None)

    def searchBookByAuthor(self, authorName):
        """ searches for all books in the book list by the author"""
        authorBooks = []
        for book in Section.books:
            if book.getAuthor() == authorName:
                authorBooks.append(book)
        return (authorBooks)

    def deleteBook(self, bookTitle):
        """it deletes a book from the book list using its title"""
        for book in Section.books:
            if book.getTitle() == bookTitle:
                Section.books.remove(book)

    def showBooks(self):
        """Return Books in the section"""
        return (Section.books)
