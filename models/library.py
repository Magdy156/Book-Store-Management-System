#!/usr/bin/python3
"""Library class"""


class Library:
    """Represts a library"""

    __sections = []
    __profit = 0
    def __init__(self, title):
        """constructor"""
        self.__title = title

    def addSection(self, sectionName):
        """Adds section to the section list"""
        Library.__sections.append(sectionName)
    
    def searchBookByTitle(self, bookTitle):
        """searches for a book in all sections by its title"""
        for section in Library.__sections:
            book = section.searchBookByTitle(bookTitle)
            if book:
                return (book)
        return (None)
    
    def searchBookByAuthor(self, authorName):
        """ searches for all books in all sections by the author"""
        bookList = []
        for section in Library.__sections:
            book_list = section.searchBookByAuthor(authorName)
            if book_list:
                bookList.extend(book_list)
        return (bookList)

    def sellaBook(self, bookTitle):
        """ it deletes a book from the book list using its title 
            and add the book cost to profit
        """
        book = Library.searchBookByTitle(bookTitle)
        if book:
            for section in Library.__sections:
                section.deleteBook(bookTitle)
            Library.__profit += book.getCost()

    def getTotalProfit(self):
        """It return the total profit of the library"""
        return (Library.__profit)
