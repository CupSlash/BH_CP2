#BH 2nd Movie Recommender
#functions for searching by a quality
def search_by_title():
    pass
def search_by_director():
    pass
def search_by_genre():
    pass
def search_by_rating():
    pass
def search_by_length():
    pass
def search_by_actors():
    pass
#main function that runs the code
def main():
    #one-time introduction to the application
    print("Welcome to the Movie Recommender!\n")
    #while loop so code repeats
    while True:
        #main menu
        choice = ("Would you like to find a movie by title (t), director (d), genre (g), rating (r), length (l), notable actors (a), or exit (e)?")
        if choice == "t":
            search_by_title()
        elif choice == "d":
            search_by_director
        elif choice == "g":
            search_by_genre
        elif choice == "r":
            search_by_rating
        elif choice == "l":
            search_by_length
        elif choice == "a":
            search_by_actors
        elif choice == "e":
            print("See you later!")
        else:
            print("That is not an option.")
main()