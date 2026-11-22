class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        print("Parent Book class object created")

    def showInfo(self):
        print(f"""
        Title: {self.title}
        Author: {self.author}
        """)

class EBook(Book):
    def __init__(self, title, author, downloadable):
        super().__init__(title, author)
        self.downloadable = downloadable
        print("Child Ebook class object created")

    def download(self):
        print(f"{self.title} downloaded.")
        if self.downloadable == True: 
            print(f"{self.title} downloaded.")
        else:
            print("Book not downloadable.")
        


class AudioBook(Book):
    def __init__(self, title, author, playable):
        super().__init__(title, author)
        self.playable = playable
        print("Child Audiobook class object created")

    def playSample(self):
        if self.playable == True: 
            print(f"Playing sample of {self.title}")
        else:
            print("Sample not found.")


class Library():
    def __init__(self):
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        print(f"{book.title} is added in the library, {type(book)}.")

    def removeBook(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"{book} removed")
        else:
            print(f"{book} not found")

    def showAllBooks(self):
        print(f"""
        
        """)
        print("---Library Catalogue---")
        for i in self.books:
            print(i.title, type(i))

hpPB1 = Book("Harry Potter and the Philosophers Stone", "JK Rowling")
hpEB2 = EBook("Harry Potter and the Chamber of Secrets", "JK Rowling", True)
hpAB3 = AudioBook("Harry Potter and the Prsioner of Azkaban", "JK Rowling", True)
hpAB4 = AudioBook("Harry Potter and the Goblet of Fire", "JK Rowling", True)


library = Library()
library.addBook(hpPB1)
library.addBook(hpEB2)
library.addBook(hpAB3)
library.removeBook(hpAB3)
library.addBook(hpAB4)
library.showAllBooks()