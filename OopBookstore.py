class BookStore:

    NoOfBooks = 0

    def __init__(self,name,author):
        self.name = name
        self.author = author
        BookStore.NoOfBooks += 1

    def Display(self):
        print(f"{self.name}by{self.author}.No of books:{BookStore.NoOfBooks}")
        
obj1 = BookStore("Linux system programming","Robert love")
obj1.Display()

obj2 = BookStore("C Programming","Dennis Rithcie")
obj2.Display()

    

