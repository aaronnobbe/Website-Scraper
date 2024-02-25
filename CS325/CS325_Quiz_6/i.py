class AddRemove:
    #add and remove books from the library
    def addBook(self, title):
        print(f"adding: {title}")

    def removeBook(self, title):
        print(f"Removing: {title}")

class Search:
    # search by title, author and genre
    def searchByTitle(self, title):
        print(f"Searching for book by title: {title}")

    def searchByAuthor(self, author):
        print(f"Searching for book by author: {author}")

    def searchByGenre(self, genre):
        print(f"Searching for book by genre: {genre}")

class BorrowReturn:
    # borrow and return from the library
    def borrowBook(self,book,name):
        print(f"{name} is borrowing: {book}")

    def returnBook(self,book,name):
        print(f"{name} is returning: {book}")

class ReportGenerator:
    #genereate reports for borrowing, overdue books and popularity.
    def BorrowingReport(self):
        print("Generating borrowing report...")

    def OverdueReport(self):
        print("Generating overdue books report...")

    def PopularityReport(self):
        print("Generating popularity report...")

class Library:
    def __init__(self):
        self.add_remove = AddRemove()
        self.search = Search()
        self.borrow_return = BorrowReturn()
        self.reports = ReportGenerator()

if __name__ == "__main__":
    library = Library()
    library.add_remove.addBook("a really entertaining one")
    library.search.searchByTitle("the best book eva")
    library.borrow_return.borrowBook("To kill a mockery burd", "My grandma jamma")
    library.reports.BorrowingReport()