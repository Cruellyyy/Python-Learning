class Book:
    def __init__(self, title, author, available):
        self.title = title
        self.author = author
        self.available = available

    def show_info(self):
        print("Title = ", self.title)
        print("Author =", self.author)
        print("Avaiable =", self.available)
    def borrow(self,):
        if (self.available == True):
            borrowerName = input("Enter ur name ")
            print(f"The book titled \"{self.title}\" has been borrowed to \"{borrowerName}\"")
            self.available = False
        elif(self.available == False):
            print(f"The book titled \"{self.title}\" is not available at the moment")
    def return_book(self):
        if (self.available == False):
            returningPersonName = input("Enter ur name ")
            self.available = True
            print(f"The book titled \"{self.title}\" has been returned by \"{returningPersonName}\"")
        elif(self.available == True):
            print(f"How can u return a book which is already present there?")

booksDetails = [Book("The Alchemist", "Paulo Coelho", True),
                Book("The Power of Now", "Eckhart Tolle", True),
                Book("Atomic Habits", "James Clear", True),
                Book("The Subtle Art of Not Giving a F*ck", "Mark Manson", False),
                Book("The 48 Laws of Power", "Robert Greene", True)]



while True:
    bookname = input("Enter the name of the book u want ")
    for Book in booksDetails:#for is loop, book is like (i), the loop will run for every book in bookdetails
     if(Book.title.lower() == bookname.title.lower()):#by this we would compare every book in the list with the input
        print("\nEnter 1 to show book info \n2 to borrow book \nand 3 to return book\n")
        method = int(input("Enter the method "))
        if(method == 1):
            Book.show_info()
        elif(method == 2):
            Book.borrow()
        elif(method == 3):
            Book.return_book()
        else:
            print("Invalid method")#so cuz of loop, it will run and try to compare every book in the list until the if statemet is meat, so its like brute force guessing from the list, so for every wrong book guess there will be a error msg hence there would be many error even for one input

            