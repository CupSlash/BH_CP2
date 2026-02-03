#BH 2nd simple morse code translator
#set languages
morse_alpha = (".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..",)
english_alpha = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")

#set functions for translating morse to english
def trans_morse_to_english(morse_input, morse_alpha, english_alpha):
    morse_input_letters = morse_input.split(" ")
    translated_word = ""
    for morse_input_letter in morse_input_letters:
        translated_char = trans_morse_char_to_english(morse_input_letter, morse_alpha, english_alpha)
        if translated_char is not None:
            translated_word += translated_char
        else:
            print(f"The message contains invalid morse code: {morse_input_letter}")
            return
    print("The message says: " + translated_word + "\n")
    
def trans_morse_char_to_english(morse_char, morse_alpha, english_alpha):
    for morse_alpha_index, morse_alpha_value in enumerate(morse_alpha):
        if morse_char == morse_alpha_value:
            return english_alpha[morse_alpha_index]
    return None

#set functions for translating english to morse
def trans_english_to_morse(english_input, morse_alpha, english_alpha):
    translated_word = ""
    for english_input_letter in english_input:
        translated_char = trans_english_char_to_morse(english_input_letter, morse_alpha, english_alpha)
        if translated_char is not None:
            translated_word += translated_char + " "
        else:
            print(f"The message contains invalid english character: {english_input_letter}")
            return
    print("The message says: " + translated_word + "\n")

def trans_english_char_to_morse(english_char, morse_alpha, english_alpha):
    for english_alpha_index, english_alpha_value in enumerate(english_alpha):
        if english_char == english_alpha_value:
            return morse_alpha[english_alpha_index]
    return None

#function with while loop to run the main code
def main():
    #Greet user
    print("Welcome to the morse/english translator!\n")
    while True:
        choice = input("Would you like to translate from morse code into english (e), english to morse code (m), or leave (l)?\n")
        if choice == "e":
            morse_input = input("Please enter the morse code you would like to translate, with spaces between each letter:\n")
            trans_morse_to_english(morse_input, morse_alpha, english_alpha)
        elif choice == "m":
            english_input = input("Please enter the english you would like to translate into morse code only using letters A-Z:\n").lower()
            trans_english_to_morse(english_input, morse_alpha, english_alpha)
        # Break loop if they want to leave
        elif choice == "l":
            break
        # Tell them that they had a typo if so
        else:
            print("that isn't an option\n")

#call main
main()