#BH 2nd personal library program
#imports
import csv
import copy
#create library reader
library_reader = csv.DictReader(open("individual_projects\library.csv"))
#Function to print books
def print_books(books, is_detailed):
    book_num = 0
    for book in books:
        book_num += 1
        if is_detailed:
            print(f"{book_num}. {book['title']} by {book['author']} released in {book['year']} under the genre {book['genre']}\n")
        else:
            print(f"{book_num}. {book['title']} by {book['author']}\n")
#new save library function
def save_library(library):
    with open("individual_projects\library.csv", "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames = ["title", "author", "year", "genre"])
        writer.writeheader()
        for book in library:    
            writer.writerow(book)
#Function to load library from csv
def load_library(library_reader):
    library = []
    for book in library_reader:
        library.append(book)
    return library
#Function to view the library
def view_library(library, is_detailed):
    if len(library) == 0:
        print("Your library is empty.\n")
    else:
        print("Here are the books in your library:\n")
    print_books(library, is_detailed)
#Function to add a new item
def add_book(library):
    new_title = input("What is the title of the book?\n")
    new_author = input(f"Who is the author of {new_title}?\n")
    new_year = int(input(f"What year did {new_author} create {new_title}?\n"))
    new_genre = input(f"What genre is {new_title}?\n")
    library.append({"title" : new_title, "author" : new_author, "year" : new_year, "genre" : new_genre})
#Function to remove an item
def remove_book(library):
    view_library(library, is_detailed=False)
    selected_book_num = int(input("Enter the number of the book you would like to remove.\n"))
    if selected_book_num <= len(library) and selected_book_num >= 1:
        del library[selected_book_num - 1]
    else:
        print("That book is not in your library.")
#Function to search the items
def search_book(library):
    selected_option = input("What would you like to search by?\n 1. Title \n 2. Author \n 3. Year \n 4. Genre\n")
    matching_books = []
    if selected_option == "1":
        title_to_search_for = input("What book title would you like to search for?\n")
        for book in library:
            if book["title"] == title_to_search_for:
                matching_books.append(book)
    elif selected_option == "2":
        author_to_search_for = input("What author would you like to search for?\n")
        for book in library:
            if book["author"] == author_to_search_for:
                matching_books.append(book)
    elif selected_option == "3":
        year_to_search_for = input("What year would you like to search for?\n")
        for book in library:
            if book["year"] == year_to_search_for:
                matching_books.append(book)
    elif selected_option == "4":
        genre_to_search_for = input("What genre would you like to search for?\n")
        for book in library:
            if book["genre"] == genre_to_search_for:
                matching_books.append(book)
    else:
        print("That is not an option.")
    if matching_books == []:
        print("No search results.")
    else:
        print("Here are the qualifying books:\n")
        print_books(matching_books, is_detailed = True)
#Function for updating books
def update_book(library):
    view_library(library, is_detailed = True)
    selected_book_num = int(input("Enter the number of the book you would like to remove.\n"))
    if selected_book_num <= len(library) and selected_book_num >= 1:
        book = library[selected_book_num - 1]
        section_to_update = input("Would you like to edit the book's title (t), author (a), year (y), or genre (g)?")
        if section_to_update == "t":
            new_title = input("What is the new title of the book?")
            book["title"] = new_title
        elif section_to_update == "a":
            new_author = input("What is the new author of the book?")
            book["author"] = new_author
        elif section_to_update == "y":
            new_year = input("What is the new year of the book?")
            book["year"] = new_year
        elif section_to_update == "g":
            new_genre = input("What is the new genre of the book?")
            book["genre"] = new_genre
        else:
            print("That is not an option.")
    else:
        print("That book is not in your library.")
#function to run the game
def start_library(library_reader):
    library = load_library(library_reader)
    library_copy = copy.deepcopy(library)
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
            remove_book(library)
        elif choice == "5":
    #Function to search the items
            search_book(library)
        elif choice == "6":
    #Function to update an item
            update_book(library)
        elif choice == "7":
    #Function to save the library
            save_library(library)
            library_copy = copy.deepcopy(library)
        elif choice == "8":
    #Exit the program
            if library != library_copy:
                save = input("You have unsaved changes. Would you like to save them? y/n\n")
                if save == "y":
                    save_library(library)
            print("Bye-bye!")
        else:
    #Invalid input
            print("That is not an option.")
#Call main function
start_library(library_reader)