"""
School

Make a class structure in python representing people at school. Make a base class called Person,
a class called Student, and another one called Teacher. Try to find as many methods and attributes
as you can which belong to different classes, and keep in mind which are common and which are not.
For example, the name should be a Person attribute, while salary should only be available to the teacher.
"""

from school import Student, Teacher

if __name__ == "__main__":
    student = Student("Peter", "Ivanov", 15, "10-Б")
    print(student.__dict__)
    teacher = Teacher("Maria", "Petrova", 35, 15000)
    print(teacher.__dict__)
