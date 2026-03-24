#BH 2nd classes.py
#example 1
class Dog:
    def __init__(self, name, breed, age):
        self.name = name.capitalize()
        self.breed = breed.title()
        self.age = age
    def __str__(self):
        return f"Name: {self.name}\nBreed: {self.breed}\nAge: {self.age}"
    def speak(self):
        return "Bark"
doug = Dog("Doug", "Golden Retriever", 3)
print(doug.speak())
#example 2
class ClassSubject:
    def __init__(self, name, room = None, teacher = "Ms. LaRose"):
        self.name = name.title()
        self.room = room
        self.teacher = teacher
    def __str__(self):
        return f"Name: {self.name}Room: {self.room}Teacher: {self.teacher}"
first = ClassSubject("Computer Programming 2", 200)
second = ClassSubject("Computer Programming 2", 200)
third = ClassSubject("Computer Science Principles", 200)
print(first, second, third)