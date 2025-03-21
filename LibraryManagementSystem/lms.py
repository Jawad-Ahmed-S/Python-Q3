class Book:
    def __init__(self, title, author, publication_year, genre):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.genre = genre
        self.readStatus = False

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Publication Year:", self.publication_year)
        print("Genre:", self.genre)
        print("Read Status:", "Yes" if self.readStatus else "No")


class LMS:
    def __init__(self):
        self.books = []
        self.read = 0

    def addBook(self, book):
        for b in self.books:
            if b.title == book.title:
                print("Book already exists")
                return
        self.books.append(book)
        print("Book added successfully")

    def removeBook(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print("Book removed successfully")
                return
        print("Book not found")

    def SearchBook(self, title):
        for book in self.books:
            if book.title == title:
                book.display()
                return
        print("Book not found")

    def displayStatistics(self):
        total_books = len(self.books)
        read_books = sum(1 for book in self.books if book.readStatus)

        print("Total Number of Books:", total_books)
        print("Percentage of Read Books:", (read_books / total_books * 100) if total_books > 0 else 0)


# Menu Interaction
library = LMS()

while True:
    print("\nMenu")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search for a Book")
    print("4. Display Statistics")
    print("5. Exit")
    
    choice = input("Enter a functionality: ").strip()

    if choice == "1":
        title = input("Enter title: ").strip()
        author = input("Enter author: ").strip()
        publication_year = input("Enter publication year: ").strip()
        genre = input("Enter genre: ").strip()

        book = Book(title, author, publication_year, genre)
        library.addBook(book)

    elif choice == "2":
        title = input("Enter title to remove: ").strip()
        library.removeBook(title)

    elif choice == "3":
        title = input("Enter title to search: ").strip()
        library.SearchBook(title)

    elif choice == "4":
        library.displayStatistics()

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")
