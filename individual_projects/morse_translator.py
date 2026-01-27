#BH 2nd simple morse code translator
#set variables
morse_letter = (".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..",)
english_letter = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
#set functions
def trans_morse_to_english(morse_letter, english_letter):
def trans_english_to_morse(morse_letter, english_letter):
#introduce user
print("Welcome to the morse/english translator!\n")
#while loop to run the main code
while True:
    choice = input("Would you like to translate from morse code into english (e), english to morse code (m), or leave (l)?\n")
    if choice == "e":
        trans_morse_to_english()
    elif choice == "m":
        trans_english_to_morse()
    elif choice == "l":
        break
    else:
        print("that isn't an option\n")