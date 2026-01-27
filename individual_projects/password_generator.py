#BH 2nd pasword_generator.py
#import random module
import random
#Create function to grab rquired characters
def create_password(length, possible_chars):
    chosen_chars = random.choices(possible_chars, k=length)
    password = ''.join(chosen_chars)
    print(password, "\n")
def find_nums(possible_chars):
    nums = input("Would you like to include numbers in your password? y/n\n")
    if nums == "y":
        numbers = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
        possible_chars.extend(numbers)
def find_lowers(possible_chars):
    lowers = input("Would you like to include lowercase letters? y/n\n")
    if lowers == "y":
        lowers = ("q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m")
        possible_chars.extend(lowers)
def find_uppers(possible_chars):
    uppers = input("Would you like to include uppercase letters? y/n\n")
    if uppers == "y":
        uppers = ("Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M")
        possible_chars.extend(uppers)
def find_specials(possible_chars):
    specials = input("Would you like to include special characters? y/n\n")
    if specials == "y":
        specials = ("`","~","!","@","#","$","%","^","&","*",",","-","_","+","=","[","]","{","}",";",":","'","\"","|","\\","<",",",".",">","/","?")
        possible_chars.extend(specials)
#Create function that runs the entire code
def main():
    print("Welcome to the password generator!")
    while True:
        choice = input("Would you like to create a password (p) or exit (e)?\n")
        #If statement for password generation conditional
        if choice == "p":
            #Ask user for criteria
            possible_chars = []
            length = int(input("How many characters should your password have?\n"))
            find_nums(possible_chars)
            find_lowers(possible_chars)
            find_uppers(possible_chars)
            find_specials(possible_chars)
            if possible_chars == []:
                print("You must select at least one character type!\n")
                continue
            print("Here are four possible passwords:\n")
            for i in range(4):
                create_password(length, possible_chars)
            #functions to make password fit criteria
        #Break loop if they don't want to create a password
        elif choice == "e":
            break
        #Tell them that they had a typo if so
        else:
            print("That is not an option.\n")
main()