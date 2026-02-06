#BH 2nd Movie Recommender
#import csv
import csv
#main function that runs the code
def main():
    #one-time introduction to the application
    print("Welcome to the Movie Recommender!\n")
    #while loop so code repeats
    while True:
        #main menu
        continue_or_exit = input("Would you like to find a movie (m) or exit (e)?")
        if continue_or_exit == "m":
            
        elif continue_or_exit == "e":
            break
        else:
            print("That is not an option.")