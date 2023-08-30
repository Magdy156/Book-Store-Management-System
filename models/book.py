#!/usr/bin/python3
"""Book class"""


class Book:
    """Represents a book"""

    def __init__(self, title, author, cost) :
        """constructor"""
        self.__title = title
        self.__author = author
        self.__cost = cost

    def getTitle(self):
        """Return title of the book"""
        return (self.__title)

    def getAuthor(self):
        """Return author of the book"""
        return (self.__author)

    def getCost(self):
        """Return cost of the book"""
        return (self.__cost)
