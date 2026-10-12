
class Book():
    def __init__(self, book_id, title, author, total_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

    def display_info(self):
        print(f"Book ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Total Copies: {self.total_copies}")
        print(f"Available Copies: {self.available_copies}")

class Member():
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        # Dictionary: Book_Id --> number of copies
        self.borrowed_books = {}

class Library():
    def __init__(self):
        self.books = {}
        self.members = {}

    # Add new Book
    def add_book(self):
        book_id = input("Enter Book ID:")

        if book_id in self.books:
            print("Book already exist")

            return

        title = input("Enter Book Title:")
        author = input("Enter Author name: ")
        total_copies = int(input("Enter no. of copies:"))

        book = Book(book_id, title, author, total_copies)

        self.books[book_id] = book

        print("Book add successfully")

    # Display books
    def display_books(self):
        if not self.books:
            print("Books are not available in Library")

            return

        for book_id, book in self.books.items():
            print("============================")
            print(f"Book ID: {book_id}")
            print("============================")
            book.display_info()

    # Search book (by ID)
    def search_book(self):
        book_id = input("Enter Book ID to search:")

        book = self.books.get(book_id, None)

        if book is None:
            print("Book is not available.")

            return

        book.display_info()

    # Add Member
    def add_member(self):
        member_id = input("Enter member ID: ")

        if member_id in self.members:
            print("Member already exists")

            return

        name = input("Enter member name: ")

        member = Member(member_id, name)

        self.members[member_id] = member

        print("Member registered successfully")

    # Issue a book
    def issue_book(self):
        book_id = input("Enter book ID: ")
        member_id = input("Enter Member ID: ")

        book = self.books.get(book_id, None)
        member = self.members.get(member_id, None)

        if book is None:
            print("Book does not exist in Records!!!")

            return

        if member is None:
            print("Member is not registered!!!")

            return

        if book.available_copies == 0:
            print("No copies available for issue!!!")

            return

        book.available_copies -= 1

        member.borrowed_books[book_id] = member.borrowed_books.get(book_id, 0) + 1

        print(f"{book.title} issued to {member.name}")

    def return_book(self):
        book_id = input("Enter Book ID: ")
        member_id = input("Enter Member ID: ")

        book = self.books.get(book_id, None)
        member = self.members.get(member_id, None)

        if book is None:
            print("Book not found!!!")

            return

        if member is None:
            print("Member not found!!!")

            return

        # if member borrowed this book
        book_borrowed = member.borrowed_books.get(book_id, 0)

        # if member not borrowed this book
        if book_borrowed == 0:
            print(f"This {member_id} have not borrowed this book {book_id}")

            return

        if book.available_copies >= book.total_copies:
            print("Rejected, Stock Limit reached")

            return

        book.available_copies += 1
        member.borrowed_books[book_id] -= 1

        if member.borrowed_books[book_id] == 0:
            del member.borrowed_books[book_id]

        print(f"Book {book.title} Returned Successfully")

    def delete_book(self):
        book_id = input("Enter Book ID to DELETE: ")

        book = self.books.get(book_id, None)

        if book is None:
            print("Book does not Exist...")

        # if book copies are issued then do not delete it
        if book.available_copies != book.total_copies:
            print("Unable to Delete this book. Some books are issued")

            return

        del self.books[book_id]

        print("Book deleted successfully")

library = Library()

while True:
    print("=============================")
    print("Enter {1} to ADD Book")
    print("Enter {2} to DISPLAY Books")
    print("Enter {3} to SEARCH Book")
    print("Enter {4} to ADD Member")
    print("Enter {5} to ISSUE Book")
    print("Enter {6} to RETURN Book")
    print("Enter {7} to DELETE Book")
    print("Enter {e} to exit")
    print("=============================")

    choice = input("Enter your Choice: ")

    if choice == "1":
        library.add_book()
    elif choice == "2":
        library.display_books()
    elif choice == "3":
        library.search_book()
    elif choice == "4":
        library.add_member()
    elif choice == "5":
        library.issue_book()
    elif choice == "6":
        library.return_book()
    elif choice == "7":
        library.delete_book()
    elif choice == "e":
        print("Program is Exiting")
        break
    else:
        print("Invalid Choice")