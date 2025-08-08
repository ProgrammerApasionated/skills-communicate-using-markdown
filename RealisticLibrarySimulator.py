# Program that simulates a library

def menu():
    print("-.1. Show all the books.-")
    print("-.2. Show all the books available.-")
    print ("-.3.- Lend a book.-")
    print ("-.4.- Return a book.-")
    print("-.5. Show all the books lent.-")
    print("-.6. Show all the specs of a book with its title.-")
    print("-.7. Add a book.-")
    print("-.8. Erase a book .-")

def read_specs(i: int) -> None:
    print(f"Book {i + 1}")
    print("-" * 30)
    print(f"Title:            {Library[i][0]}")
    print(f"Author:           {Library[i][1]}")
    print(f"Publication date: {Library[i][2]}")
    print(f"Pages:            {Library[i][3]}")
    print("-" * 30)
    print()

def show_all_books():
    for i in range(len(Library)):
        read_specs(i)
def only_available_books():
    for i in range(len(Library)):
        if Library[i][4] == False:
            read_specs(i)

def lend_book():
    available = []
    print("Available books to lend:")
    for i, book in enumerate(Library):
        if not book[4]:
            print(f"{len(available)+1}. {book[0]} by {book[1]}")
            available.append(i)
    if not available:
        print("No books are available to lend.")
        return
    while True:
        option = input("Choose a book number to lend: ")
        if option.isdigit():
            option = int(option)
            if 1 <= option <= len(available):
                idx = available[option - 1]
                Library[idx][4] = True
                print("The book has been lent.")
                break
        print("Please enter a valid book number.")

def return_book():
    lent_books= []
    print ("Lent books:")
    for i in range(len(Library)):
        if Library[i][4] == True:
            print(f"{i + 1}. {Library[i][0]} by {Library[i][1]}")
            lent_books.append(i)
    if not lent_books:
        print("No books are currently lent.")
        return 
    while True:
        option = input("Choose a book number to return: ")
        if option.isdigit():
            option = int(option)
            if 1 <= option <= len(lent_books):
                index = lent_books[option - 1]
                Library[index][4] = False
                print("The book has been returned.")
                break
        print("Please enter a valid book number.")


def show_lent_books():
    lent_books = []
    print("Lent books:")
    for i in range(len(Library)):
        if Library[i][4] == True:
            read_specs(i)
            lent_books.append(i)
    if not lent_books:
        print("No books are currently lent.")

def show_book_specs_by_title():
    title = input("Enter the title of the book: ")
    found = False
    for i in range(len(Library)):
        if Library[i][0].lower() == title.lower():
            read_specs(i)
            found = True
            break
    if found == False:
        print("Book not found.")
def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    publication_date = input("Enter the publication date (e.g., 1st of January): ")
    while True:
        pages = input("Enter the number of pages: ")
        if pages.isdigit():
            pages = int(pages)
            break
        print("Please enter a valid number for pages.")
    state = input("Is the book lent? (yes/no): ").strip().lower() == 'yes'
    
    new_book = [title, author, publication_date, pages, state]
    Library.append(new_book)
    print("Book added successfully.")

def erase_book():
    found = False
    title = input("Enter the title of the book to erase: ")
    for i in range(len(Library)):
        if Library[i][0].lower() == title.lower():
            del Library[i]
            print("Book erased successfully.")
            found = True
            break
    if found == False:
        print("Book not found.")

    
# Some books that I absolutely love
book1 = ["The right move", "Liz Tomforde", "4th of February", 426,False]
book2 = ["Saving 6", "Cloe Walsh", "16th of May", 560,False]
book3 = ["Once upon a broken heart", "Stephanie Garber", "30th of June", 432,False]
book4 = ["Twisted love", "Ana Huang", "28th of September", 384,False]
# This is the way the books are formed: book_example = ["Title", "Author", "Publication date", "Pages", "State (lent or not)"]
# The state is False if the book is available and True if it is lent

# Add the library by adding all the books inside it
Library = [book1, book2, book3, book4]

# And with all the functions defined, we can now create a menu to interact with the library
while True:
    menu()  
    option = input("Choose an option (or 'q' to quit): ")
    if option == "1":   
        show_all_books()
    elif option == "2":
        only_available_books()
    elif option == "3":
        lend_book()
    elif option == "4":
        return_book()
    elif option == "5":
        show_lent_books()
    elif option == "6":
        show_book_specs_by_title()
    elif option == "7":
        add_book()
    elif option == "8":
        erase_book()
    else:
        if option.lower() == "q":
            print("Library updated, See you next time! ;)")
            break
        else:
            print("Please choose a valid option.")
        