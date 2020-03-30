class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


class Student(Person):

    def __init__(self, first_name, last_name, age, class_name):
        super().__init__(first_name, last_name, age)
        self.class_name = class_name


class Teacher(Person):

    def __init__(self, first_name, last_name, age, salary):
        super().__init__(first_name, last_name, age)
        self.salary = salary
