#BH 2nd portfolio class
#Imports
import tkinter as tk
import os
#Portfolio class
class Portfolio:
#__init__ method (This is where I'll set up project info)
    def __init__(self, root):
        self.root = root
        self.root.title("Programming Portfolio")
        self.root.geometry("600x450")
        self.base_folder = "individual_projects"
        self.selected = ""
        self.projects = {
            "Fractal Generator": {
                "desc": "An application that creates a custom sierpinski triangle.\n\u2022 I learned how to run a recursive function from this projcet. \n\u2022 The biggest challenge was learning how to place the triangles in the correct location using recursion.",
                "file": "\\fractal_generator\\main.py",
            },
            "Financial Calculator": {
                "desc": "A calculator for managing your finances. \n\u2022 From this project I learned how to perform various financial calculations. \n\u2022 Calculating savings time and budget allocation were the most difficilt parts of this project.",
                "file": "\\financial_calculator.py",
            },
            "Morse Translator": {
                "desc": "A tool to translate English to Morse code and Morse code to English. \n\u2022 I learned how to use lists and function to translate letters between two languages. \n\u2022 This whole project was pretty difficult. The hardest part was probably creating functions for translating individual characters and then using those funtions to translate whole words.",
                "file": "\morse_translator.py",
            },
            "Movie Recommender": {
                "desc": "An application to filter a list of movies to find one that is just right for you. \n\u2022 This project taught me advanced mechanics in using csv files. \n\u2022 This project was pretty difficult. I think the hardest part was creating the filter by length function.",
                "file": "\movie_recommender.py",
            },
        }
        self.build_gui()
#Create the build gui method to set up the GUI for the portfolio app.
    def build_gui(self):
        tk.Label(self.root, text="Programming Portfolio", font=("Arial", 18)).pack(pady=10)
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill="both", expand=True)
        projects_frame = tk.Frame(main_frame)
        projects_frame.pack(side="left", padx=10)
        information_frame = tk.Frame(main_frame)
        information_frame.pack(side="right", fill="both", expand=True)
        tk.Label(projects_frame, text="Projects:").pack()
        tk.Label(information_frame, text="Info:").pack()
        self.info_box = tk.Text(information_frame, height=15, wrap="word")
        self.info_box.pack(fill="both", expand=True)
        for name in self.projects:
            tk.Button(
                projects_frame,
                text=name,
                width=25,
                command=lambda n=name: self.select_project(n)
            ).pack(pady=3)
        tk.Button(self.root, text="Run Project", command=self.run_project).pack(pady=10)
#Method that allows you to select a project
    def select_project(self, name):
        self.selected = name
        self.info_box.delete("1.0", tk.END)
        self.info_box.insert(tk.END, self.projects[name]["desc"])
#Method that allows you to run the selected project
    def run_project(self):
        if self.selected == "":
            self.info_box.delete("1.0", tk.END)
            self.info_box.insert(tk.END, "Please pick a project.")
            return
        file_path = self.base_folder + "/" + self.projects[self.selected]["file"]
        if not os.path.exists(file_path):
            self.info_box.delete("1.0", tk.END)
            self.info_box.insert(tk.END, "File not found:\n" + file_path)
            return
        os.system("python " + file_path)