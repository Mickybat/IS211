class Book:
    author = " "
    title = " "

    def __init__(self, titleName, authorName):
        self.title = titleName
        self.author = authorName

    def display(self):
        print(f"\'{self.title}\', written by {self.author}")


obj1 = Book("Of Mice and Men", "John Steinbeck")
obj2 = Book("To killl a Mockingbird", "Harper Lee")

obj1.display()
obj2.display() 