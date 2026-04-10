#BH 2nd main.py
import tkinter as tk
class Menu:
    def __init__(self, root):
        self.root = root
        self.root.title("Briggs Hardy - Programming Portfolio")
        self.projects = {
            "Fractal Generator": "An application that creates a custom sierpinski triangle.\u2022 I learned how to run a recursive function from this projcet. \u2022 The biggest challenge was learning how to place the triangles in the correct location using recursion.",
            "Financial Calculator": "A calculator for managing your finances. \u2022 From this project I learned how to perform various financial calculations. \u2022 Calculating savings time and budget allocation were the most difficilt parts of this project.",
            "Morse Translator": "A tool to translate English to Morse code and Morse code to English. \u2022 I learned how to use lists and function to translate letters between two languages. \u2022 This whole project was pretty difficult. The hardest part was probably creating functions for translating individual characters and then using those funtions to translate whole words.",
            "Movie Recommender": "An application to filter a list of movies to find one that is just right for you. \u2022 This project taught me advanced mechanics in using csv files. \u2022 This project was pretty difficult. I think the hardest part was creating the filter by length function."
        }
        self.selected_project = None
        self.create_widgets()

    def create_widgets(self):
        tk.Label(text="Programming Portfolio", font=("TkDefaultFont", 20)).pack()
        desc = ("This Project allows you to interact with some of the python projects I am most proud of. Start by selecting a project from the list and then selecting the 'Run Selected Project' button.")
        tk.Label(text=desc, justify="center", pady=10).pack()
        tk.Label(self.root, text="Applications:", font=("TkDefaultFont", 12)).pack(anchor="w", padx=50)
        tk.Label(self.root, text="App Info:", font=("TkDefaultFont", 12)).pack(anchor="w", padx=50, pady=(20, 5))

root = tk.Tk()
app = Menu(root)
root.mainloop()


#FILE PATHS
#Fractal Generator: C:\Users\cupsl\Dev\BH_CP2\BH_CP2\individual_projects\fractal_generator
#Financial Calculator: C:\Users\cupsl\Dev\BH_CP2\BH_CP2\individual_projects\financial_calculator
#Morse Translator: C:\Users\cupsl\Dev\BH_CP2\BH_CP2\individual_projects\morse_translator
#Movie Recommender: C:\Users\cupsl\Dev\BH_CP2\BH_CP2\individual_projects\movie_recommender