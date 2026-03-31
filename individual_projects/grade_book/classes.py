#BH 2nd Classes
#Student class
class Student:
    #Add __init__ and __str__ methods
    def __init__(self, name, student_id, grade_level):
        self.name = name
        self.student_id = student_id
        self.grade_level = grade_level
        self.grades = []
    def __str__(self):
        if (self.calculate_average() is None):
            average_grade = "N/A"
        else:
            average_grade = self.calculate_average()
        return f"Name: {self.name}, ID: {self.student_id}, Average Grade: {average_grade} ({self.determine_letter_grade()}), Grade Level: {self.grade_level}, Academic Standing: {self.determine_academic_standing()}"
    #Add a method to assign a grade to a student
    def add_grade(self, grade):
        self.grades.append(grade)
    #Add a method for calculating the average grade for a student.
    def calculate_average(self):
        if (len(self.grades) == 0):
            return None
        return round(sum(self.grades) / len(self.grades), 2)
    #Add a method for determining the letter grade for a student based on their average grade.
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
    #Add a similar method for finding a student's academic standing.
    def determine_academic_standing(self):
        average = self.calculate_average()
        if average is None:
            return "N/A"
        elif average >= 90:
            return "Honor Roll"
        elif average >= 80:
            return "Good Standing"
        else:
            return "Needs Improvement"
#GradeBook class
class GradeBook:
    #Add __init__ method for grade book as well
    def __init__(self):
        self.students = []
    #Add a method for adding a student.
    def add_student(self, student):
        self.students.append(student)
    #Add a method allowing the user to search for students by name and by ID.
    def search_students_by_name(self, name):
        matching_students = filter(lambda student: name.lower() in student.name.lower(), self.students)
        return list(matching_students)
    def search_students_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None
    #Add a method for calculating the class average, highest grade, lowest grade, and total number of students in the class.
    def calc_max_min_average(self):
        grades = []
        for student in self.students:
            average = student.calculate_average()
            if average is not None:
                grades.append(average)
        if len(grades) == 0:
            return None
        return {
            "highest": max(grades),
            "lowest": min(grades),
            "average": round(sum(grades) / len(grades), 2),
            "total_students": len(self.students)
        }