class Book:

    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    
    def borrow(self):
        self.is_borrowed = True
    
    def return_book(self):
        self.is_borrowed = False
    
    def display(self):
        print(f"'{self.title}' by {self.author}")

    def __str__(self, value):
        return self.title == value

class Ebook(Book):
    def __init__(self, title, author,file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def display(self):
        super().display()
        print(f"Size : {self.file_size}")
    
Library = []

while True:
    print("1. Add Book")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Show Books")
    print("5. Exit")

    while True:
        try:
            choice = int(input("Enter your choice : "))
            break
        except ValueError:
            print("Enter a valid number from the menu")
    
    if choice == 5:
        break

    match choice:
        case 1:
            title = input("Enter the title of the book : ")
            author = input("Enter the name of the author : ")
            is_ebook = input("Is your book an e-book [Y/N] : ")
            if is_ebook.lower() == "y":
                file_size = int(input("Enter the size of the Ebook: "))
                book = Ebook(title,author,file_size)
            else:    
                book = Book(title,author)
            Library.append(book)

        case 2:
            title = input("Enter the title of the book you want to borrow")
            for item in Library:
                if item.__str__(title):
                    if item.is_borrowed == True:
                        print("Book is borrowed by someone else")
                    else:
                        item.borrow()

        case 3:
            title = input("Enter the title of the book you want to return")
            for item in Library:
                if item.__eq__(title):
                    item.is_borrowed = False
            
        case 4:
            for item in Library:
                item.display()

        case _:
            print("Invalid Choice")