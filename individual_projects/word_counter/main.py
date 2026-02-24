#BH 2nd main.py
#imports
from time_handling import *
from file_handling import *
#define menu function
def menu():
    #introduction
    print("Welcome to the Word Counter!")
    file_path = input("Please enter the file path to your document:").strip()
    #while true loop for menu options until user exits
    while True:
        #Ask user for what they would like to do
        choice = input("--- Document Word Counter ---\n1. Update document info\n2. View document\n3. Add content to document\n4. Exit\nEnter your choice (1-4):")
        #Update document info, view document, add content to document, or exit based on user input
        if choice == '1':
            content_parts = get_content_parts(file_path)
            user_content = content_parts['user_content']
            word_count = len(user_content.split()) 
            timestamp = get_timestamp()
            update_document_info(file_path, word_count, timestamp)
            print("Document info updated successfully!", f"Word Count: {word_count}")
        elif choice == '2':
            content_parts = get_content_parts(file_path)
            print(f"Document Content:\n{content_parts['user_content']}")
        elif choice == '3':
            new_content = input("Enter new content to add to the document:")
            add_content_to_document(file_path, new_content)
            print("Content added successfully!")
        elif choice == '4':
            print("See you later!")
            break
        #Invalid choice handling
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
#Run the menu function to start the program
menu()