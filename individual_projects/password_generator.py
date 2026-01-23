#BH 2nd pasword_generator.py
#Create function that runs the entire code
def code():
    print("Welcome to the password generator!")
    while True:
        choice = input("Would you like to create a password (p) or exit (e)?\n")
        #If statement for password generation conditional
        if choice == "p":
            #Ask user for criteria
            nums = input("Would you like to include numbers in your password? y/n\n")
            lowers = input("Would you like to include lowercase letters? y/n\n")
            uppers = input("Would you like to include uppercase letters? y/n\n")
            specials = input("Would you like to include special characters? y/n\n")
            length = int(input("How many character should your password have?\n"))
            #functions to make password fit criteria
            -0-
        #Break loop if they don't want to create a password
        elif choice == "e":
            break
        #Tell them that they had a typo if so
        else:
            print("That is not an option.\n")
code()