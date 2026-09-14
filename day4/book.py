class Book:
    def __init__(self, name, author, price):
        self.name = name
        self.author = author
        self.price = price

    def display_info(self):
        print(f"Book Name : {self.name}")
        print(f"Author    : {self.author}")
        print(f"Price     : ${self.price}")


# Example usage:
my_book = Book("Atomic Habits", "James Clear", 15.99)
my_book.display_info()