"""
Design Patterns

General and reusable solution to common problems in software design
A template for solving given problems
Add additional layers of abstraction in order to reach flexibility

What do does design patterns solve?

Patterns solve software structural problems like:
-Abstraction
-Encapsulation
-Separation of concerns
-Coupling and cohesion
-Separation of interface and implementation
"""

"""
Elements of a design pattern

Patter name - increases vocabulary of designers
Problems - intent  context and when to apply
Solution - Abstract code
Consequences - Results and trade offs
"""

"""
Benefits and Drawbacks 

Benefits:
-Names form a common vocabulary
-Enable large scale reuse of software architectures
-Help improve developer communications 
-Can speed up the development

Drawbacks
-Do not lead to a direct code reuse
-Deceptively simple
-Developers may suffer from pattern overload and over design
-Validate by experience and discussion not by automated testing
-Should be used only if understood well 
"""

"""
Types of Design Patterns

Main Type
-Creation patterns
    -Deal with initialization and configuration of classes and objects
-Structural patterns
    -Describe ways to assemble objects to implement new functionality
    -Composition of classes and objects
-Behavioral patterns 
    -Deal with dynamic interactions among societies of classes 
    -Distribute responsibility 
"""

"""
Creating Patterns

Purposes
-Deal with object creation mechanisms
-Trying to create objects in a manner suitable to the situation
-Two main ideas:
    -Encapsulation knowledge about which classes the system uses
    -Hiding how instances of these classes are created 
"""

"""
List of Creation Patterns

1:Singleton
2:Simple Factory
3:Factory Method
4:Abstract Factory
5:Builder
6:Prototype
7:Fluent Interface
8:Object Pool
9:Lazy Initialization
"""

"""
Creational Patterns in Python

The language it self provides us with create objects in an elegant fashion
We rarely need to implement anything on top, like singleton or factory
Factories are abstraction on top of constructors
Builder are abstraction on top of factories
"""

"""
Singleton

The singleton pattern is used when we want to guarantee that only one instance of given classes exists during runtime
The singleton  is considered an anti-pattern because:
-It makes the code more complex and less useful 
-It introduces unnecessary restrictions
-It is hard to test

Example:
"""

"""Example Singleton"""


def singleton(cls):
    instance = [None]

    def wrapper(*args, **kwargs):
        if instance[0] is None:
            instance[0] = cls(*args, **kwargs)
        return instance[0]

    return wrapper


@singleton
class DBConnection(object):

    def __init__(self):
        """Initialize your database connection here."""
        pass

    def __str__(self):
        return 'Database connection object'


"""Factory Method"""
from abc import ABC, abstractmethod


class DataExporter(ABC):
    @abstractmethod
    def export(self, data):
        pass


class CsvDataExporter(ABC):
    @abstractmethod
    def export(self, data) -> str:
        pass


class DataExporterFactory(ABC):
    @abstractmethod
    def get_exporter(self) -> DataExporter:
        pass


class CsvDataExporterFactory(DataExporterFactory):
    def get_exporter(self) -> DataExporter:
        return CsvDataExporter()


"""Abstract Factory"""
from abc import ABC, abstractmethod
import json


class JsonDataExporter(ABC):
    @abstractmethod
    def export(self, data) -> str:
        pass


class CsvDataExporter(ABC):
    @abstractmethod
    def export(self, data) -> str:
        pass


class DataExporterFactory(ABC):

    @abstractmethod
    def get_json_exporter(self) -> JsonDataExporter:
        pass

    @abstractmethod
    def get_csv_exporter(self) -> CsvDataExporter:
        pass
