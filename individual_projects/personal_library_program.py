#BH 2nd personal library program
#Function to view the library
import csv
library_reader = csv.DictReader(open("individual_projects\library.csv"))
def save_library(library):
    with open("individual_projects\library.csv", "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames = ["title", "author", "year", "genre"])
        writer.writeheader()
        for book in library:    
            writer.writerow(book)
def load_library(library_reader):
    library = []
    for book in library_reader:
        library.append(book)
    return library
def view_library(library, is_detailed):
    if len(library) == 0:
        print("Your library is empty.\n")
    else:
        print("Here are the books in your library:\n")
    for book in library:
        if is_detailed:
            print(f" {book['title']} by {book['author']} released in {book['year']} under the genre {book['genre']}\n")
        else:
            print(f" {book['title']} by {book['author']}\n")
#Function to add a new item
def add_book(library):
    new_title = input("What is the title of the book?\n")
    new_author = input(f"Who is the author of {new_title}?\n")
    new_year = int(input(f"What year did {new_author} create {new_title}?\n"))
    new_genre = input(f"What genre is {new_title}?\n")
    library.append({"title" : new_title, "author" : new_author, "year" : new_year, "genre" : new_genre})
#Function to remove an item
def remove_book(library_reader):
    message = "Enter the number of the book you would like to remove.\n"
    book_num = 1
    view_library(library_reader, is_detailed=False)
    selected_book_num = int(input(message))
    if selected_book_num <= len(library_reader):
        del library_reader[selected_book_num - 1]
    else:
        print("That book is not in your library")
#Function to search the items
def search_book(library_reader):
    selected_option = input("What would you like to search by?\n 1. Title \n 2. Author \n")
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
    book_to_update = input("Select a book to update.\n")
#function to run the game
def start_library(library_reader):
    library = load_library(library_reader)
    while True:
    #ask user what they would like to do
        choice = input("What would you like to do? \n1. View my library (simple) \n2. View my library (detailed) \n3. Add to my library \n4. Remove from my library \n5. Search for a book in my library \n6. Update a book in my library \n7. Save my library \n8. Exit \n")
        if choice == "1":
    #Function to view the library  
            view_library(library, is_detailed=False)
        elif choice == "2":
            view_library(library, is_detailed=True)
        elif choice == "3":
    #Function to add a new item
            add_book(library)
        elif choice == "4":
    #Function to remove an item
            remove_book(library_reader)
        elif choice == "5":
    #Function to search the items
            search_book(library_reader)
        elif choice == "6":
    #Function to update an item
            update_book(library_reader)
        elif choice == "7":
    #Function to save the library
            save_library(library)
        elif choice == "8":
    #Exit the program
            print("Bye-bye!")
            break
        else:
    #Invalid input
            print("That is not an option.")
#Call main function
start_library(library_reader)