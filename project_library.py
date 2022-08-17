# Books library

class Library:
    def __init__(self, list, name):
        self.booksList = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have following books in our library: {self.name}")
        for book in self.booksList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book database has been updated. You can take the book now")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    def addBook(self, book):
        self.booksList.append(book)
        print("Book has been added to the book list")

    def returnBook(self, book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    mrunu = Library([" 1) The God of small things", "2) The white Tiger", "3) The Guid",
    "4) Train to pakistan" , "5) Agnipath", "6) In custody", "7) End of the Era", "8) My Struggle",
    "9) My Truth, Eternal India", "10) Arthashastra", "11) My Nation My Life", "12) Aag Ka Dariya",
    "13) Economic History of India", "14) Agni Veena: Kazi Nasrul Islam","15) Ancient Mariner: Coleridge",
    "16) Animal Farm: George Orwell", "17) Arms and the Man: G.B.Shaw" , "18) Ben Hur: Lewis Wallace"
    "19) Around the World in eighty day ...","20) Sapiens: A Brief History of Humankind by Yuval Noah Harari", 
    "21) Long Walk to Freedom by Nelson Mandela" , "22) The Rise and Fall of the Dinosaurs:"
    "23) A New History of Their Lost World by Steve Brusatte", "24) A Brief History of Time by Stephen Hawking" ,
    "25) Freakonomics: A Rogue Economist Explores the Hidden Side of Everything " , 
    "26) The Age of Surveillance Capitalism: The Fight for a Human Future at the New Frontier of Power" ,
    "27) Uncanny Valley by Anna Wiener"], "Dhyanchand")

    while(True):
        print(f"Welcome to the {mrunu.name} library. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print("Please enter a valid option")
            continue

        else:
            user_choice = int(user_choice)


        if user_choice == 1:
            mrunu.displayBooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend:")
            user = input("Enter your name")
            mrunu.lendBook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add:")
            mrunu.addBook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return:")
            mrunu.returnBook(book)

        else:
            print("Not a valid option")


        print("Press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()

            elif user_choice2 == "c":
                continue

