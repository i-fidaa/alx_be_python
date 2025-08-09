class Book:
    def __init__(self, title, author, year):
        """Constructor - runs when a new Book object is created"""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor - runs when a Book object is deleted"""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation - for printing in a readable way"""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation - for recreating the object in code form"""
        return f"Book('{self.title}', '{self.author}', {self.year})"
