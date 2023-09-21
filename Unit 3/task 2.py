class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_studenstudents (students_list) :
  #sort the list of students in descending order of CGPA
  sorted_students = sorted(students_list, key= lambda students:students.cgpa,reverse= True)
  
#Syntax - lamda arg:exp
return sorted_students
  
  
  #Example usage:
students = [
    Student("Alice", "101", 3.8),
    Student("Bob", "102", 3.5),
    Student("Charlie", "103", 4.0),
    Student("David", "104", 3.7)
]

sorted_students = sorted_students(students)

for student in sorted_students:
    print(" Name:{},Eoll number:{}".format(student.name, student.roll_number, student.cgpa)) 