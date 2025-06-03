class LibraryItem:
    
    def __init__(self, title, author, year):
        self.title= title
        self.author = author
        self.year = year
        self.available = True
    
    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}) "
    
    def check_out(self):
        if self.available:
            print(f"Checking out {self.title}...")
            self.available = False
        else:
            print(f"{self.title} is currently unavailable.")
            
    def check_in(self):
        if not self.available:
            print(f"Checking in {self.title}...")
            self.available = True
        else:
            print(f"{self.title} is already checked in.")
            
class Book(LibraryItem):
    def __init__(self, title, author, year, genre):
        super().__init__(title, author, year)
        self.genre = genre
    
    def __str__(self):
        return f"{super().__str__()} ( Genre: {self.genre})"
    
class User:
    
    def __init__(self, name):
        self.name= name
        
    def borrow_item(self, item):
        print(f"{self.name} is borrowing {item.title}.")
        item.check_out()
    
    def return_item(self, item):
        print(f"{self.name} is returning {item.title}.")
        item.check_in()
        
Library = []

book1 = Book("1984", "George Orwell", 1949, "Dystopian")
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction")

Library.append(book1)
# Library.append(book2)

user = User("Alice")
user.borrow_item(book1)
# user.borrow_item(book1)

user.return_item(book1)


print("Current Library Items:")
for item in Library:
    print(item)

    
                              