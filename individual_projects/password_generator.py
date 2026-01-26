#BH 2nd pasword_generator.py
#Create function that runs the entire code
def main():
    print("Welcome to the password generator!")
    while True:
        choice = input("Would you like to create a password (p) or exit (e)?\n")
        #If statement for password generation conditional
        if choice == "p":
            #Ask user for criteria
            length = int(input("How many characters should your password have?\n"))
            nums = input("Would you like to include numbers in your password? y/n\n")
            lowers = input("Would you like to include lowercase letters? y/n\n")
            uppers = input("Would you like to include uppercase letters? y/n\n")
            specials = input("Would you like to include special characters? y/n\n")
            password = []
            list = []
            if nums == "y":
                list.append(0), (1), (2), (3), (4), (5), (6), (7), (8), (9)
            if lowers == "y":
                list.append("q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m")
            if uppers == "y":
                list.append("Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M")
            if specials == "y":
                list.append("`","~","!","@","#","$","%","^","&","*","(",")","-","_","+","=","[]","]","{","}",";",":","'","\"","|","\\","<",",",".",">","/","?")
            for character in range(length):
                password.append(list)
            final = str
            for_loop_num = 0
            for i in password:
                
                final += password[for_loop_num]
                for_loop_num += 1
            print(final)
            #functions to make password fit criteria
        #Break loop if they don't want to create a password
        elif choice == "e":
            break
        #Tell them that they had a typo if so
        else:
            print("That is not an option.\n")
main()