#BH 2nd Classes
#Student class
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []
    def __str__(self):
        if (self.calculate_average() is None):
            average_grade = "N/A"
        else:
            average_grade = round(self.calculate_average(), 2)
        return f"Name: {self.name}, ID: {self.student_id}, Average Grade: {average_grade} ({self.determine_letter_grade()})"
    def add_grade(self, grade):
        self.grades.append(grade)
    def calculate_average(self):
        if (len(self.grades) == 0):
            return None
        return sum(self.grades) / len(self.grades)
    def determine_letter_grade(self):
        average = self.calculate_average()
        if average is None:
            return "N/A"
        elif average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
#GradeBook class
class GradeBook:
    def __init__(self):
        self.students = []
    def add_student(self, student):
        self.students.append(student)
    def search_students_by_name(self, name):
        matching_students = filter(lambda student: name in student.name, self.students)
        return list(matching_students)
    def search_students_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None