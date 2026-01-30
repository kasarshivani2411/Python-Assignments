# Write a python program to implement a class named BookStore with the following specifications:
# The class should contain two instance variables:
    # Name(Book Name)
    # Author(Book Author)
# The class should contain one class variable:
    # NoOfBooks(initialize it to 0)
# Define a constructor (__init__) that accepts Name and Author and initializes instance variables.
# Inside the constructor, increment the class variable NoOfBooks by 1, whenever the new object is created 
# Implement as instance method:
    # Display() - should display book details in the format:
    # <BookName> by <Author>. No of books: <NoOfBooks>

# Example usage:
# obj1 = BookStore("Linux System Programming", "Robert Love")
# obj1.Display()    # Linux System Programming by Robert Love. No of Books: 1

# obj2 = BookStore("C Programming", "Dennis Ritchie")
# obj2.Display()    # C Programming by Dennis Ritchie. No of Books: 2

class BookStore:
    NoOfBooks = 0

    def __init__(self, Name, Author):
        self.BookName = Name
        self.AuthorName = Author

        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def Display(self):
        print(f"{self.BookName} by {self.AuthorName}. No of Books: {BookStore.NoOfBooks}")

    
def main():
    obj1 = BookStore("Linux System Programming", "Robert Love")
    obj1.Display()

    obj2 = BookStore("C Programming", "Dennis Ritchie")
    obj2.Display()

if __name__ == "__main__":
    main()