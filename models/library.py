#!/usr/bin/python3
"""Library class"""
from models.book import Book
from models.section import Section
from storage.storageFile import FileStorage
storage = FileStorage()


class Library:
    """Represts a library"""

    sections = []
    profit = 0

    def __init__(self, title):
        """constructor"""
        self.__title = title

        # Reteriving Data
        booksData = storage.reload()
        # print(booksData)
        for title, bookData in booksData.items():
            book = Book(title, bookData["author"], bookData["cost"])
            sectionTitle = bookData["section"]

            isSection = None
            for section in self.sections:
                if section.getTitle() == sectionTitle:
                    isSection = section
                    break

            if isSection:
                isSection.addBook(book)
            else:
                section = Section(sectionTitle)
                section.addBook(book)
                self.addSection(section)

    def addSection(self, sectionName):
        """Adds section to the section list"""
        Library.sections.append(sectionName)
    
    def searchBookByTitle(self, bookTitle):
        """searches for a book in all sections by its title"""
        for section in Library.sections:
            book = section.searchBookByTitle(bookTitle)
            if book:
                return (book)
        return (None)
    
    def searchBookByAuthor(self, authorName):
        """ searches for all books in all sections by the author"""
        result = []
        for section in Library.sections:
            bookList = section.searchBookByAuthor(authorName)
            if bookList:
                result.extend(bookList)
        result = list(set(result))
        return (result)

    def sellaBook(self, bookTitle):
        """ 
        it deletes a book from the book list using its title 
        and add the book cost to profit
        """
        for section in self.sections:
            book = section.searchBookByTitle(bookTitle)
            if book:
                Library.profit += book.getCost()
                section.deleteBook(bookTitle)

    def getTotalProfit(self):
        """It return the total profit of the library"""
        return (Library.profit)

    def showBooks(self):
        """Return all books in the library"""
        result = []
        for section in Library.sections:
            bookList = section.showBooks()
            if bookList:
                result.extend(bookList)
        result = list(set(bookList))
        return (result)
