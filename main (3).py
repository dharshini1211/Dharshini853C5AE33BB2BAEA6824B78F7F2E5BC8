"""
Implement a function sort_students that takes a list of student objects as input and sorts the 
list based on their CGPA(Cumulative Gradepoint Aerage) in descending order.Each student object 
has the following attributes: name (String),roll_(string), and Cgpa(float).Test the function
with different inputlist of students.
"""

class Student:

  def __init__(self,name, roll_number,cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_student(student_list):
  # sort the list of students in descending order of CGPA.
  sorted_students = sorted(student_list, 
       key=lambda student:student.cgpa,
                     reverse = True)
  #Syntax _lambda arg:exp
  return  sorted_students


# Example usage:
students =[
Student("Hari", "A123", 7.8),
Student("Srikanth", "A124", 8.9),
Student("saumya", "A125", 9.1),
Student("mahidhar", "A126", 9.9),
]

sorted_students = sort_student(students)

# print the sorted list of students
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,
                                         student.roll_number,
                       student.cgpa))
                                                       
  

  
  

  
  