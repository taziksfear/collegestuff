class Student:
    def __init__(self, name, surname, grades):
        self.name = name
        self.surname = surname
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

    def is_excellent(self):
        return self.average_grade() >= 4.5

student = Student("Иван", "Иванов", [5, 5, 4, 5])
print(student.average_grade())
print(student.is_excellent())