from Student import Student

# class Student:
#
#     def __init__(self, name, major, gpa, is_on_probation):
#         self.name = name
#         self.major = major
#         self.gpa = gpa
#         self.is_on_probation = is_on_probation

student1 = Student("Geralt", "Witcher", 3.7, False)
student2 = Student("Jaskier", "Bard", 2.5, True)
student3 = Student("Ciri", "Witcher", 4.0, False)

print(student1.name)
print(student1.major)
print(student2.name)
print(student2.is_on_probation)
print(student3.name)
print(student3.gpa)

print(student1.name, student1.major, student1.gpa,
      student1.is_on_probation)

print(student1.on_honor_roll())
print(student2.on_honor_roll())
print(student3.on_honor_roll())
