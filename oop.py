class Student:
    name = "Harshu"
    age = 17

print(Student)

class Student:

    def study(self):
        print("Student is studying")

student1 = Student()
student1.study()



class Student:

    def show(self):
        print("Hello")

s1 = Student()
s1.show()



class Student:

    def __init__(self):
        print("Student created")

s1 = Student()




class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Harshu", 17)
s2 = Student("Rahul", 18)

print(s1.name)
print(s2.name)


class Student:

    def __init__(self):
        print("Object created")

    def __del__(self):
        print("Object destroyed")

s1 = Student()
del s1


class Animal:

    def eat(self):
        print("Animal eats")


class Dog(Animal):

    def bark(self):
        print("Dog barks")


d = Dog()

d.eat()
d.bark()


class A:
    def show(self):
        print("A")


class B(A):
    pass


obj = B()
obj.show()


class A:
    def showA(self):
        print("A")


class B(A):
    def showB(self):
        print("B")


class C(B):
    def showC(self):
        print("C")


obj = C()

obj.showA()
obj.showB()
obj.showC()


#one child multiple parents 
class Father:
    def skills1(self):
        print("Coding")


class Mother:
    def skills2(self):
        print("Cooking")


class Child(Father, Mother):
    pass


c = Child()

c.skills1()
c.skills2()


#Hierarchical inheritance

#one  parent → multiple children.
class Animal:

    def eat(self):
        print("Eating")


class Dog(Animal):
    pass


class Cat(Animal):
    pass


d = Dog()
c = Cat()

d.eat()
c.eat()

#Polymorphism
class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")


d = Dog()
c = Cat()

d.sound()
c.sound()


#Method overriding
class Animal:

    def sound(self):
        print("Animal sound")


class Dog(Animal):

    def sound(self):
        print("Bark")


d = Dog()
d.sound()

#super()
class Animal:

    def __init__(self):
        print("Animal constructor")


class Dog(Animal):

    def __init__(self):
        super().__init__()
        print("Dog constructor")


d = Dog()

#encapsulation
class Student:

    def __init__(self):
        self.__marks = 90

s = Student()

#Abstract
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Bark")


#class method
class Student:

    school = "ABC School"

    @classmethod
    def change_school(cls, name):
        cls.school = name


Student.change_school("XYZ School")

print(Student.school)


#static method 
class Student:

    @staticmethod
    def hello():
        print("Hello Student")


Student.hello()

