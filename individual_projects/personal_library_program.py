#BH 2nd personal library program
#Function to view the library
import csv
with open("individual_projects\library.csv", "a", newline='') as f:
    writer = csv.DictReader(f,fieldname = {"title", "author"})
    writer.writerow({"title" : title, "author" : author, "year" : year, "genre" : genre})
library_reader = csv.DictReader(open("individual_projects\library.csv"))
def view_library(library_reader):
    if len(library_reader) == 0:
        print("Your library is empty.\n")
        return
    print("Here are the books in your library:\n")
    for book in library_reader:
        print(f"{book[0]} by {book[1]}\n")
#Function to add a new item
def add_book(library_reader):
    new_title = input("What is the title of the book?\n")
    new_author = input(f"Who is the author of {new_title}?\n")
    new_year = input(f"What year did {new_author} create {new_title}?\n")
    new_genre = input(f"What genre is {new_title}?\n")
    new_book = (new_title, new_author)
    library_reader.append(new_book)
#Function to remove an item
def remove_book(library):
    message = "Enter the number of the book you would like to remove.\n"
    book_num = 1
    for book in library:
        message += f"{book_num}. {book[0]} by {book[1]}\n"
        book_num += 1
    selected_book_num = int(input(message))
    if selected_book_num <= len(library):
        del library[selected_book_num - 1]
    else:
        print("That book is not in your library")
#Function to search the items
def search_book(library_reader):
    selected_option= input("What would you like to search by?\n 1. Title \n 2. Author \n")
    book_found = False
    if selected_option == "1":
        title_to_search_for = input("What book title would you like to search for?\n")
        for book in library_reader:
            if book[0] == title_to_search_for:
                print(f"{book[0]} by {book[1]}\n")
                book_found = True
    elif selected_option == "2":
        author_to_search_for = input("What author would you like to search for?\n")
        for book in library_reader:
            if book[1] == author_to_search_for:
                print(f"{book[0]} by {book[1]}\n")
                book_found = True
    if book_found == False:
        print("No search results.")
def update_book(library_reader):
    print(library_reader)
    update_book = input("Select a book to update.\n")
#function to run the game
def start_library(library_reader):
    while True:
    #ask user what they would like to do
        choice = input("What would you like to do? \n1. View my library \n2. Add to my library \n3. Remove from my library \n4. Search for a book in my library \n5. Update a book in my library \n6. Exit \n")
        if choice == "1":
    #Function to view the library
            view_library(library_reader)
        elif choice == "2":
    #Function to add a new item
            add_book(library_reader)
        elif choice == "3":
    #Function to remove an item
            remove_book(library_reader)
        elif choice == "4":
    #Function to search the items
            search_book(library_reader)
        elif choice == "5":
    #Function to update an item
            update_book(library_reader)
        elif choice == "6":
            print("Bye-bye!")
            break
        else:
            print("That is not an option.")
start_library(library_reader)