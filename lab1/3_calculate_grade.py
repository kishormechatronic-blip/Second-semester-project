class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

        # calculate average grade
        self.average_grade = sum(grades) / len(grades)
 
student1 = Student("Charlie", [80, 90, 85])

print("Name:", student1.name)
print("Grades:", student1.grades)
print("Average Grade:", student1.average_grade)