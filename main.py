#!/usr/bin/python3
"""GUI Handling"""
from models.library import Library
import PyQt5.QtWidgets as qtw


class GUI(qtw.QWidget):
    """Represents a GUI"""
    def __init__(self):
        super().__init__()
        #title
        self.setWindowTitle("Book Store System")
        # vertical Layout
        self.setLayout(qtw.QVBoxLayout())

        # initialising our Library
        self.library = Library("Main Library")
        
        # show books elements
        self.showLabel = qtw.QLabel("Show All Books")
        self.showButton = qtw.QPushButton("Show")
        self.showButton.clicked.connect(self.showAll)

        # search by book title elements
        self.searchByTitle_label = qtw.QLabel("Search By Book Title:")
        self.searchByTitle_input = qtw.QLineEdit()
        self.searchByTitle_button = qtw.QPushButton("Search")
        self.searchByTitle_button.clicked.connect(self.searchBook)

        # search by author name elements
        self.searchByAuthor_label = qtw.QLabel("Search By Author Name:")
        self.searchByAuthor_input = qtw.QLineEdit()
        self.searchByAuthor_button = qtw.QPushButton("Search")
        self.searchByAuthor_button.clicked.connect(self.searchAuthor)

        # sell elements
        self.sellLabel = qtw.QLabel("Sell Book:")
        self.sellInput = qtw.QLineEdit()
        self.sellButton = qtw.QPushButton("Sell")
        self.sellButton.clicked.connect(self.sellBook)

        # profit elements
        self.profitLabel = qtw.QLabel("Get Your profits:")
        self.profitButton = qtw.QPushButton("Get the Profit")
        self.profitButton.clicked.connect(self.getProfit)

        # Add components to layout
        self.layout().addWidget(self.showLabel)
        self.layout().addWidget(self.showButton)

        self.layout().addWidget(self.searchByTitle_label)
        self.layout().addWidget(self.searchByTitle_input)
        self.layout().addWidget(self.searchByTitle_button)

        self.layout().addWidget(self.searchByAuthor_label)
        self.layout().addWidget(self.searchByAuthor_input)
        self.layout().addWidget(self.searchByAuthor_button)

        self.layout().addWidget(self.sellLabel)
        self.layout().addWidget(self.sellInput)
        self.layout().addWidget(self.sellButton)

        self.layout().addWidget(self.profitLabel)
        self.layout().addWidget(self.profitButton)

        self.setLayout(self.layout())
        self.show()

    def showAll(self):
        books = self.library.showBooks()
        if books:
            for book in books:
                bookInfo = f"Title: {book.getTitle()}\nAuthor: {book.getAuthor()}\nCost: {book.getCost()}"
                qtw.QMessageBox.information(self, 
                                            "Book Found", 
                                            bookInfo)
        else:
            qtw.QMessageBox.information(self, 
                                        "Books Not Found", 
                                        f"We need goods")

    def searchBook(self):
        title = self.searchByTitle_input.text()
        # print(title)
        if title:
            book = self.library.searchBookByTitle(title)
            if book:
                book_info = f"Title: {book.getTitle()}\nAuthor: {book.getAuthor()}\nCost: {book.getCost()}"
                qtw.QMessageBox.information(self, 
                                            "Book Found", 
                                            book_info)
            else:
                qtw.QMessageBox.information(self, 
                                            "Book Not Found", 
                                            f"No book found with the title '{title}'.")
        else:
            qtw.QMessageBox.information(self, 
                                        "Invalid Input",
                                        "Please enter a title to search.")

    def searchAuthor(self):
        title = self.searchByAuthor_input.text()
        # print(title)
        if title:
            books = self.library.searchBookByAuthor(title)
            # print(books)
            if books:
                for book in books:
                    bookInfo = f"Title: {book.getTitle()}\nAuthor: {book.getAuthor()}\nCost: {book.getCost()}"
                    qtw.QMessageBox.information(self, 
                                                "Book Found", 
                                                bookInfo)
            else:
                qtw.QMessageBox.information(self, 
                                            "Books Not Found", 
                                            f"No book found for the author '{title}'.")
        else:
            qtw.QMessageBox.information(self, 
                                        "Invalid Input",
                                        "Please enter a title to search.")

    def sellBook(self):
        title = self.sellInput.text()
        # print(title)

        if title:
            self.library.sellaBook(title)
            qtw.QMessageBox.information(self, 
                                        "Book Sold", 
                                        f"The book '{title}' has been sold.")
        else:
            qtw.QMessageBox.information(self,
                                            "Invalid Input", 
                                            "Please enter a title to sell.")

    def getProfit(self):
        profit = self.library.getTotalProfit()
        if profit:
            qtw.QMessageBox.information(self, 
                                        "profit", 
                                        f"The total profit = {profit}")
        else:
            qtw.QMessageBox.information(self, 
                                        "profit", 
                                        f"The total profit = 0")


app = qtw.QApplication([])
window = GUI()

# Run the program
app.exec_()
