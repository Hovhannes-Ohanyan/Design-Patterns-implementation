from abc import ABC, abstractmethod

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

class Prototype(ABC):

    @abstractmethod
    def copy(self):
        ...

class Student2(Prototype):


    def copy(self, prototype):
        self.name = prototype.name
        self.age = prototype.age

prototype = Student("Hamo", 15)
student2 = Student2()
student2.copy(prototype)
print(isinstance(student2, Student))
print(student2.name, student2.age)


