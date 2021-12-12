"""
OOP(Object-oriented programming) is a programming paradigm
Provides a means of structuring programs so that properties and behaviors are bundled into individual objects
Objects are at the center of the OOP paradigm(a typical example or pattern of something; a pattern or model)
name
attributes
behavior

An object oriented program consist of objects that interact with each other
"""

"""
Class definition:
A class is like blueprint(a large-format reproduction, usually of an architectural or engineering plan.) for creating
objects
Classes provide a means of bundling data and functionality together
Each class instance can have attributes attached to it
Class instances can also have methods for modifying its state
All classes create objects and all objects contain characteristics called attributes

The __init__() method initializes  an objects initial attributes by giving them their default value
The double leading and trailing underscore is used for special for special variables ot methods

"""

"""
Self Variables:

The self parameter is reference to the current instance of the class 
Used to access variables that belong to the class 
When defining an instance method the first parameter of the method should always be self
"""

# class Person:
#     def __init__(self, first, last, age=0):
#         self.first_name = first
#         self.last_name = last
#         self.age = age


"""
Object definition:
While the class is the blueprint, an instance is concrete object of the type of the class 
In other words, a class is like a form or questionnaire, it defines the needed information
You can fill out multiple copies , but without the form as a guide you will not know what information is required
"""

# me = Person('Petter', 'Johnson', 25)
# print(me.first_name)
# print(me.last_name)
# print(me.age)

"""
Modifying attributes:
You can change the values of the attributes of an object after initialization
"""
# me.age += 1
# print(me.age)
"""
The change will be made only for that instance of the class (me)
"""
"""
Class attributes:
While instance attributes are specific to each object, class attributes are the same for all instance
"""

# class SecondPerson:
#     species = 'mammal'
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# sec_me = SecondPerson('Peter', 20)
# print(sec_me.species)

"""
Instance methods:
Instance methods are defined inside a class and are used to get the contents of an instance
They can also be used to perform operations with the attributes of our objects 
Like the __init__ method the first argument should always be self 
"""

# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def calc_human_age(self):
#         return self.age * 7
#
#
# an = Animal('Terra', 6)
# print(an.calc_human_age())

"""
Python OOP
Defining classes
Project architecture

-Splitting code into methods 
We use methods to split code into functional block 
Allows for easier debugging
A single method should complete a single task 
"""

"""
Classes

Classes provide means of building data functionality together
Classes create new types of objects that allow instances of that type to be made
Each class instance can have attributes for maintaining its state
Class instances can also have methods for modifying its states 
"""

# class Person:
#     def __init__(self, name, age):  # class method
#         self.name = name  # instance attribute
#         self.age = age


"""
The __init__ method 
When a class defines an __init__() method this method is invoked for the newly created class instance

Self keyword
Self is used to represent the instance of the class
You can access the attributes and methods of the class
It binds the attributes with the given arguments
"""

"""
Scope and Namespace(Local, Global, and Build-in Namespace)

Namespace
A mapping from names to objects
Example:
-Built-in name for example the abs() function
-Global names in a module
-Local names on a function invocation

There is no relation between names in different namespace 

Namespace order:
Built-in Namespace
Module: Global Namespace
Function: Local Namespace
"""

"""
Scope
A region in a program where a namespace is directly accessible 
In most of the cases there are at least three nested scopes:
-The innermost witch is searched first
-The scopes of any enclosing functions
-The next-to-last scope (module's global names)
-The outermost(built-in names)

Example:
"""

# def scopes():
#     def local_scope():
#         text = 'Local text'
#
#     def nonlocal_scope():
#         nonlocal text
#         text = 'nonlocal text'
#
#     def global_scope():
#         global text
#         text = 'global text'


"""
Class Object
They support two kinds of operations:
-Attribute
-References
-Instantiation

Attribute references
-Use standard syntax: obj.name
-Valid attribute names are the ones in the class's namespace

Instantiation
-uses function notation
"""

"""
Attribute References Example:
"""

# class MyClass:
#     i = 112345
#
#     def f(self):
#         return 'hello world'


"""
MyClass.i and MyClass.f are valid attribute references
Class attribute can also be assigned so you can change the value of MyClass.i by assignment
"""

"""
Instantiation Example
"""
# x = MyClass()
"""
Creates a new instance of the class and assigns this object to the local variable x
The instantiation operation creates an empty object
Many classes create objects with instances customized to a specific initial state
Therefore a class may define a special method named  __init__()
"""

"""
Classes and Instances 
Class object

Class objects support two kinds of operation:
-Attribute references can be addressed with object.attribute_name
-Instantiation class instantiation uses function notation

Example:
"""

# class Example:
#     text = 'Hello World'
#
#
# var = Example.text  # attribute reference
# e = Example()  # instantiation

"""
Instance Objects 

An individual object of a certain class 
-The instantiation operation creates an empty object
-To create objects with instances customized to a specific initial state we can define a special method named __init__()
Example:
"""

# class Animal():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# an = Animal('Terra', 6)

"""
The only operations understood by instance object are attribute references
There are two kinds of valid attribute names:
-data attributes 
-method
"""

"""
Data attributes
Data attributes do not need to be declared
-Like local variables they spring into existence when they are first assigned to
"""

# class Laptop:
#     def __init__(self, model, brand):
#         self.model = model
#         self.brand = brand
#
#
# laptop = Laptop("Swift", 'Acer')
# laptop.ram = 8
# print(laptop.ram)  # will print 8 without living a trace
# del laptop.ram

"""
Method 

A method is a function that belongs to an object
All attributes of a class  that are function objects define corresponding methods of its instance
-Valid method reference: x.say_hello
-Invalid method reference = X.number
"""

# class MyClass:
#     number = 749
#
#     def say_hello(self):
#         return 'Hello'
#
#
# m = MyClass()

"""
Method Object
What exactly happens when a method is called?
m.say_hello()
-The method was called without an argument even though the functional definition for say_hello() specified an argument
-The instance object is passed as the first argument of the function 
"""

"""
Method Objects Definition

When we reference a valid class attribute that is a function object method object is created by packing the instance 
object and the function object

If the method object is called with an argument list a new argument list is constructed  
"""

"""
Class and instance variables
Instance variables are unique to each instance
Class variables are for attributes and methods that are shared by all instances of the class 
Shared data can have surprising effects with mutable objects
Example: 
"""

# class Dog:
#     tricks = []  # mistaken use if a class variable
#
#     def __init__(self, name):
#         self.name = name
#
#     def add_trick(self, trick):
#         self.tricks.append(trick)
#
#
# f = Dog('Fido')
# t = Dog('Terra')
# f.add_trick('roll over')
# t.add_trick('play dead')
#
# print(f.tricks)  # shared by all dogs
#
#
# class DogC:  # Correct results
#     def __init__(self, name):
#         self.name = name
#         self.tricks = []  # create empty list for each dog
#
#     def add_tricks(self, trick):
#         self.tricks.append(trick)
#
#
# f = DogC('Fido')
# t = DogC('Terra')
# f.add_tricks('roll over')
# t.add_tricks('play dead')
#
# print(f.name, f.tricks)
# print(t.name, t.tricks)

"""
Good Practice:
"""

# class DogCanine:
#     kind = 'canine'  # class variable shared by all instance
#
#     def __init__(self, name):
#         self.name = name
#
#
# f = DogCanine('Fido')
# t = DogCanine('Terra')
#
# print(f.name, f.kind)  # the name is unique to instance but kind is shared
# print(t.name, t.kind)  # the name is unique to instance but kind is shared

"""
Attributes and Method 
Attributes and the __dict__

A special attribute of every module 
is __dict__

This is the dictionary containing the module's symbol table
object.__dict__

A dictionary or other mapping object used to store an object's (writable) attributes
"""

# class MyClass(object):
#     class_variable = 1
#
#     def __init__(self, i_var):
#         self.instance_variable = i_var
#
#
# foo = MyClass(2)
# bar = MyClass(3)
#
# print(MyClass.__dict__)
# print(foo.__dict__)
# print(bar.__dict__)

"""
Built-in functions for accessing attributes 

Attributes of a class can also be accessed using the following functions 
-getattr() - used to access the attribute of object
-hasattr() - used to check if an attribute exist or not
-setattr() - used to set an attribute
-delattr() - used to delete an attribute (if you are accessing the attribute after deleting it raises error "class has 
no attribute")
"""

# class Employ:
#     name = 'Harsh'
#     salary = '25000'
#
#     def show(self):
#         print(self.name, self.salary)
#
#
# emp = Employ()
# print(getattr(emp, 'name'))
# print(hasattr(emp, 'name'))
# setattr(emp, 'height', 172)
# print(getattr(emp, 'height'))
# delattr(emp, 'height')

"""
Static and class methods
Static Methods

A static methods is a method that knows nothing about the class or instance it called on
It's easy to turn a method into static method 
All we have to do is to add a line with @staticmethod in front of the method header
To call a static method we use the instance or the class
"""

# class Robot:
#     __counter = 0
#
#     def __init__(self):
#         type(self).__counter += 1
#
#     @staticmethod
#     def robot_instance():
#         return Robot.__counter
#
#
# print(Robot.robot_instance())
# r = Robot()
# print(r.robot_instance())
# r2 = Robot()
# print(r2.robot_instance())
# print(Robot.robot_instance())

"""
Class method

A class method on the other hand is a method that gets passed the class it was called on (or instance)
This is useful when you want the method to be a factory for the class 
All we have to do is to add a line with @classmethod in front of the method header 
"""

# from datetime import date
#
#
# class Persons:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def from_birth_year(cls, name, birth_year):
#         return cls(name, date.today().year - birth_year)
#
#     def display(self):
#         return print(self.name + ' age is: ' + str(self.age))
#
#
# person = Persons.from_birth_year('John', 1992)
# person.display()


"""
Encapsulation
Encapsulation Definition

Allows us to put restrictions and can prevent the accidental modification of date

How to control access?
-Using single underscore
-Using double underscore
-Using getter and setter methods to access private variables
"""

"""
Single underscore
Using a single leading underscore is merely a convention 
A name pre fixed with an underscore should be treated as a non-public method/variable
It does not make any variable or method private or protected 
"""

# class SomeClass:
#     def __init__(self, name, age=0):
#         self.name = name
#         self._age = age
#
#
# some_class = SomeClass('Peter', 25)
# print(some_class.name)
# print(some_class._age)

"""
Double underscore
To make a method or variable private you can do it by prefixing it with double underscore
It is still possible to access the private variable/method from outside the class  
"""

# class SecondSomeClass:
#     def __init__(self, name, age=0):
#         self.name = name
#         self.__age = age
#
#     def info(self):
#         print(self.name)
#         print(self.__age)
#
#
# ssc = SecondSomeClass('Petter', 30)
# ssc.info()  # accessing data truth class method
# print(ssc.name)  # accessing data directly from outside
# print(ssc.__age)  # AttributeError: 'SecondSomeClass' object has no attribute '__age'


"""
Getter and Setter methods

To access and change private variables accessor(getter) and mutators(setter) methods should be used as they are part of 
the class
"""

# class Student:
#     def __init__(self, name, age=0):
#         self.name = name
#         self.__age = age
#
#     def info(self):
#         print(self.name)
#         print(self.__age)
#
#     def get_age(self):
#         print(self.__age)
#
#     def set__age(self, age):
#         self.__age = age
#
#
# stu = Student('Sammy', 29)
# stu.info()  # accessing data using class method
# stu.set__age(26)
# stu.get_age()


"""
Getters and Setters 

The "Python-ic" way of defining getter and setter is using properties 
-By defining properties you can change the internal implementation of a class without affecting the program
"""

# class Dog:
#     def __init__(self, age=0):
#         self.__age = age
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         if age > 12:
#             self.__age = 12 * 7
#         else:
#             self.__age = age
#
#
# dog = Dog(6)
# print(dog.age)
# dog.age = 42
# print(dog.age)


"""
Private Methods

A private method is class method that should only be called from inside the class where it is defined 
To defined a privet method prefix the name with double underscore 
"""

# class Person:
#     def __init__(self):
#         self.first = 'Petter'
#         self.last = 'Parker'
#
#     def __full_name(self):
#         return f'{self.first} {self.last}'
#
#     def info(self):
#         return self.__full_name()
#
#
# person = Person()
# print(person.info())
# print(person.__full_name)  # AtributeError
# print(person._Person__full_name()) # Petter Parker


"""
Private Variables
Definition and Usage

A private variables can only be changed within a class method
Double underscore prefixed to a variable makes it private or nonpublic 
Object can hold crucial data and you do not want that data to be changeable from any where in the code
"""

# class Car:
#     def __init__(self):
#         self.__max_speed = 200
#
#     def drive(self):
#         print('Driving with ' + str(self.__max_speed))
#
#
# red_car = Car()
# red_car.drive()
# red_car.__max_speed = 100  # won't change because it is private
# red_car.drive()


"""
Change the private variable with getters/setters
"""

# class Car:
#     def __init__(self):
#         self.__max_speed = 260
#
#     def drive(self):
#         print('driving with ' + str(self.max_speed))
#
#     @property
#     def max_speed(self):
#         return self.__max_speed
#
#     @max_speed.setter
#     def max_speed(self, speed):
#         self.__max_speed = speed
#
#
# red_car = Car()
# red_car.drive()
# red_car.max_speed = 100
# red_car.drive()


"""
Inheritance
Definition and Benefits

Inheritance is the capability of one class to inherit the method and properties from another class

Benefits of Inheritance
-Code re-usability 
-All features to a class without modifying it
-It is transitive in nature
"""

# class Person:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def get_full_name(self):
#         return f'{self.first_name} {self.last_name}'
#
#
# class Student(Person):
#     pass
#
#
# student = Student('John', 'Smith')  # An object of class Student
# print(student.get_full_name())


"""
The super() Method 

The super() built-in returns a temporary object of the superclass
Allows you to call method of the superclass in your subclass
The primary use case of this is to extend the functionality of the inherited method 
"""

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_info(self):
#         return f'{self.name} is {self.age} old'
#
#
# class Students(Person):
#     def __init__(self, name, age, student_id):
#         super(Students, self).__init__(name, age)
#         self.student_id = student_id
#
#     def get_id(self):
#         return self.student_id
#
#
# person = Person('John', 29)  # creating an object of the superclass
#
# print(person.get_info())
#
# student = Students('Leo', 20, 10035)  # creating an object of the subclass
# print(student.get_info())
# print(student.get_id())


"""
Forms of Inheritance
-Single - When a child class inherits only a single parents class
-Multiple - When a child inherits from multiple parents classes
-Multilevel - When a child class becomes a parent class for another child class
-Hierarchical  - Involves multiple inheritance from the base or parent class
"""

"""
Multiple Inheritance 
"""

# class Father:
#     def __init__(self):
#         self.father_name = 'Tyler Evans'
#
#
# class Mother:
#     def __init__(self):
#         self.mother_name = 'Bet Williams'
#
#
# class Daughter(Father, Mother):
#     def __init__(self):
#         Father.__init__(self)  # calling constructors of both parents class
#         Mother.__init__(self)
#
#     def get_parent_info(self):
#         return f'{self.father_name} and {self.mother_name}'
#
#
# child = Daughter()
# print(child.get_parent_info())


"""
Multilevel inheritance
"""

# class Base:
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#
# class Child(Base):
#     def __init__(self, name, age):
#         super(Child, self).__init__(name)
#         self.age = age
#
#     def get_age(self):
#         return self.age
#
#
# class GrandChild(Child):
#     def __init__(self, name, age, address):
#         super(GrandChild, self).__init__(name, age)
#         self.address = address
#
#     def get_address(self):
#         return self.address
#
#
# grand_child = GrandChild('Grand', 19, '153')
# print(grand_child.name, grand_child.age, grand_child.address)

"""
Mixins
"""

# class Vehicle:
#     def __init__(self, position):
#         self.position = position
#
#     def travel(self, destination):
#         pass
#
#
# class RadioMixin:
#     def play_song(self, station_frequency):
#         return f'{station_frequency}'
#
#
# class Car(Vehicle, RadioMixin):
#     pass
#
#
# class Clock(RadioMixin):
#     pass
#
#
# car = Car('Sofia')
# clock = Clock()
# print(car.play_song(95.6))
# print(clock.play_song(103))

"""
If the base class doesn't define any of the variables that the mixins defines we can use both codes below and get 
similar result 

If you inherit multiple mixins to your class it is important to remember the order which python inherits those parents:
-Make the highest to lowest from left to right

class Car(Vehicle, RadioMixin):
pass

class Car(RadioMixin, Vehicle):
pass 
"""

"""
Polymorphism and Magic Methods
Polymorphism

Polymorphism is based on the Greek word "Many Forms"

In software engineering polymorphism means the usage of an object through the interface of their base class
-i.e Circle inherits Shape so a circle instance can be used for an instance of type Shape 
"""

# class Shape:
#     pass
#
#
# class Circle(Shape):
#     def __init__(self):
#         pass
#
#     def area(self):
#         pass
#
#     def perimeter(self):
#         pass
#
#
# def print_shape(s: Shape):
#     print(s.perimeter())
#     print(s.area())
#
#
# print(print_shape(Circle(3)))


"""
Implementing strong_type polymorphism
A word about Abstraction

In object oriented programing abstraction is one of three central principles

Through abstraction
-We hide all but the relevant data about an object to reduce complexity and increase efficiency
-Implementation details are hidden and must be accessed explicit
"""

"""
Abstract Classes

An abstract method is a method that is a method that is declared but contain no implementation
Abstract classes are classes that contain one or more abstraction methods 
Abstract classes may not be instantiated and require subclasses to provide implementations for the abstract methods

Abstract classes in Python

Python doesn't have true abstract classes and methods 
-It can be achieved but it is ugly
"""

# class Shape:
#     def __init__(self):
#         if type(self) == Shape:
#             raise TypeError('This is an abstract class')
#
#     def area(self):
#         raise TypeError('This is an abstract class')
#
#     def perimeter(self):
#         raise TypeError('This is an abstract class')

"""
Abstract classes with ABC module

Abstract class infrastructure can be implemented using the abstract base
classes(ABS) MODULE
-This module is called abc
"""

# from abc import ABC, abstractmethod

#
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
#     @abstractmethod
#     def perimeter(self):
#         pass


"""Example Abstract classes with ABC module"""

# class Animal(ABC):
#     def __init__(self, name):
#         self.name = name
#
#     @abstractmethod  # Decorator function that make method abstract
#     def sound(self):
#         raise NotImplementedError('Subclass must implement')
#
#
# class Dog(Animal):  # Inherit abstract class
#     def __init__(self, name):
#         super(Dog, self).__init__(name)
#
#     def sound(self):  # Implement the abstract class
#         print("Bark!")
#
#
# class Cat(Animal):
#     def __init__(self, name):
#         super(Cat, self).__init__(name)
#
#     def sound(self):  # Implement the abstract class
#         print("Meow!")

# dog = Dog('Willy')
# dog.sound()
# cat = Cat('Merry')
# cat.sound()
# animal = Animal('Terra')
# animal.sound()


"""
Magic Methods

Magic Methods in Python are the special methods which add "magic" to your class 

They are not meant to be invoked directly by you but internally from the class an a certain action 
For example when you add two numbers using the "+" operator the __add__() method will be called


Magic Methods in built-in classes

Built-in classes in python define many magic methods

Use the dir() function to see the magic methods inherited by a class in the "int" class
>>> dir(int)
[__abc__, __add__, __and__, ....]
"""

"""
Example :
If we have a class Person and we want to compare them by their age using using the > operator we can override the 
__gt__ magic method
"""

# class Person:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def __gt__(self, other):
#         return self.salary > other.salary
#
#
# person = Person('Sammy', 1000)
# person_two = Person('Max', 2000)
# print(person > person_two)

"""
Solid Principles 
Design Principles and Approaches 
Single Responsibility

Each class is responsible for only one thing and should have one reason to chang
A class which has many responsibility is coupling these responsibilities together which leads to 
complexity and fragility

"""

"""
Single Responsibility Principle(SRP) Violation

SRP states that classes should have one responsibility
Here we have two;
-student properties management
-student database management
"""

# class Student:
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#     def register(self, student):
#         pass


"""
SRP approaches

We can avoid the domino effect if the application change by splitting the class
Create another class that will handle the responsibility of staring a student to a database
"""

# class Student:
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#
# class StudentRecords:
#     def get_student(self, id):
#         pass
#
#     def register(self, student):
#         pass

"""
Open/Close Principle

Software entities like classes modules and functions should be open for extension but closed for modification

This can be achieved trough:
-Abstraction
-Mixins
-Monkey Patching
-Generic Functions(using overloading)
"""

"""
Open/Close Principle(OCP) Violation

Let's imagine that we want to make a 40% discount of the semester taxes to all students with grades above 5
"""

# class StudentTaxes:
#     def __init__(self, name, semester_tax, avg_grade):
#         self.name = name
#         self.semester_tax = semester_tax
#         self.avg_grade = avg_grade
#
#     def get_discount(self):
#         if self.avg_grade > 5:
#             return self.semester_tax * 0.4


"""
Letter we decide that we want to give 20% discount to students with grade above 4 adding to get_discount
"""

# class StudentTaxes:
#     def __init__(self, name, semester_tax, avg_grade):
#         self.name = name
#         self.semester_tax = semester_tax
#         self.avg_grade = avg_grade
#
#     def get_discount(self):
#         if self.avg_grade > 5:
#             return self.semester_tax * 0.4
#         elif self.avg_grade > 4:    # don't add that but create new class
#             return self.semester_tax * 0.2


"""
Don't change the class for additional discount but make new class for that and that inherited from StudentTaxes:
-For 20% discount to students with grade above 4 is better to create new class
"""

# class AdditionalDiscount(StudentTaxes):
#     def get_discount(self):
#         super(AdditionalDiscount, self).get_discount()
#         if 4 < self.avg_grade <= 5:
#             return self.semester_tax * 0.2

"""
Liskov Substitution
LSP Substitutability

Derived types must be completely substitutable for their base types 
Derived classes 
-Only extend functionality of the base class
-must not remove base class behavior student is substituted for Person
"""

"""
Remarks on the LSD

lSP is fundamental to a good object oriented software design because it emphasizes on of its core trains polymorphism
-It is about creating correct hierarchies so that classes derived from a base one are polymorphic along the parent one
-Carefully thinking that about new classes in the way that LSP suggests helps us to extend the hierarchy correctly
-We could say that LSP contributes to the OCP

"""

"""
Design Smell Violation

If the code checking the type of class
Overridden methods change their behavior 
Override a method of the super class by an empty method 
Base class depends on its subtypes
"""

"""
Interface Segregation

A client should not depend on methods it does not use
A good way of ensuring this is by separation through multiple inheritance

This is precisely the purpose of the mixins to provide multiple clients specific behaviors 

IPS is intended to keep a system decoupled and this easier to refactor change and redeploy

IPS Issues
Python doesn't have interfaces
Languages that have interfaces
-Breaking them up to much ends up with interfaces implementing interfaces 
"""

"""
ISP Violations

class shape draws rectangle and circle
class circle ot rectangle implementing the shape class must define the methods draw_rectangle() and draw_circle
"""

# class Shape:
#     def draw_rectangle(self):
#         raise NotImplementedError
#
#     def draw_circle(self):
#         raise NotImplementedError


"""
Class rectangle implements method draw_circle it has no use of
Class Circle implements method draw_rectangle 
"""

# class Rectangle(Shape):
#     def draw_rectangle(self):
#         pass
#
#
# class Circle(Shape):
#     def draw_rectangle(self):
#         pass
#
#     def draw_circle(self):
#       pass

"""
ISP Approaches

To make shape conform to IPS  principle we segregate the actions to different classes
Classes Circle and Rectangle can inherit from class Shape and implement their own draw behavior
"""

# class Shape:
#     def draw(self):
#         pass
#
#
# class Rectangle(Shape):
#     def draw(self):
#         pass
#
#
# class Circle(Shape):
#     def draw(self):
#         pass


"""
Dependency Inversion

Interesting design principle by which we protect our code by making it independent of things that are fragile volatile
or our of our control
Depend on abstractions not on concretions 
High-level modules should not depend on low-level modules both should depend on abstractions
Abstractions should not depend on details
Details should depend on abstractions

Dependency Injection

Software engineering technique for defining the dependencies among object 
Why use dependency injection
-Decreases coupling between a class and its dependency 
-Can be applied to legacy code as a refactoring because it doesn't require any change in code behavior
-Allow a client to remove all knowledge of a concrete implementation that is needs to use

Example:
"""

# class Email:
#     def send_email(self):
#         pass
#
#
# class Notification:
#     def __init__(self):
#         self._email = Email()  # notification depends on class Email
#
#     def promotional_notification(self):
#         self._email.send_email()


"""
Example Constructor Injection
"""

# class IMessageService:  # using abstraction
#     def send_message(self):
#         pass
#
#
# class Email(IMessageService):
#     def send_message(self):
#         pass
#
#
# class Notification:
#     def __init__(self, service: IMessageService):
#         self._service = service
#
#     def promotional_notification(self):
#         self._service.send_message()


"""
Dependency Injector Framework

Designed to be a unfilled tool that helps implement a dependency injection design pattern in formal and pythonic way

The key features of DI framework are:
-Easy, smart and pythonic style
-Obvious and clear structure
-Extensibility and flexibility
-High Performance
-Memory efficiency
-Thread safety  
"""