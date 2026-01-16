#BH 2nd personal library program
#Define the library
library = set()
#Function to add a new item
def add_book():
    new_book = input("What would you like to add to your library?\n")
    library.add(new_book)
#Function to remove an item
def remove_book():
    print(library)
    old_book = input("What book would you like to remove from your library?\n")
    if old_book in library:
        library.remove(old_book)
    else:
        print("That book is not in your library")
#Function to search the items
def search_book():
    book_to_search_for = input("What book would you like to search for?\n")
    if book_to_search_for in library:
        print("That book is in your library!")
    else:
        should_cpu_add_book = input("That book is not in your library, would you like me to add it? y/n\n")
        if should_cpu_add_book == "y":
            library.add(book_to_search_for)
        else:
            pass
#function to run the game
def start_library():
    while True:
    #ask user what they would like to do
        choice = input("What would you like to do? \n1. View my library \n2. Add to my library \n3. Remove from my library \n4. Search for a book in my library \n5. Exit \n")
        if choice == "1":
            print(library)
        elif choice == "2":
    #Function to add a new item
            add_book()
        elif choice == "3":
    #Function to remove an item
            remove_book()
        elif choice == "4":
    #Function to search the items
            search_book()
            exit
        elif choice == "5":
            print("Bye-bye!")
            break
        else:
            print("That is not an option.")
start_library()