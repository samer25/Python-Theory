"""
Building Rock solid software
Testing

The first level of software testing
-The smallest testable parts of a software are tested
Validates that each unit of the software performs as designed
Types of testing
-unit testing
-integration testing
-system testing

Testing changes the convention of writing code:
-Less abstract
-Test specific causes

Triple A pattern
-Arrange
-Act
-Assert

Draw backs from manual testing

Not structured
Not repeatable
Less accuracy
Not as easy as it should be
Requires more time and resources


Moving away from manual testing

We need a structured approach that:
-Allows refactoring
-Reduces the cost of change
-Decreases the number of defects in the code
Bonus:
-Improves design
"""

"""
Unit Testing

Unit testing is a type of software testing where individual units or components of a software are tested
The purpose is ti validate that each unit of the software code performs as expected 
Unit testing is done during the development(coding phase) of an application by the developers

Automated Testing

Done through an automation tool
Higher accuracy
Better reporting capabilities 
Increased coverage 
Improved bug detection
Increased re-usability
Stability
"""

"""
Unit testing framework

Individual units or components are being tested
Validate each unit to perform as expected
A unit may be an individual:
-Function
-Method
-Procedure
-Module
-object
"""

"""
Concepts behind unittest

Test fixture
-A baseline for running tests to ensure is a fixed environments in which tests are run so that results are repeatable
Test case
-A set of conditions used to determine if a system works correctly
Test suite
-A collection of testcases used to test a software if it has same specified set of behaviors
Test runner 
-A component which sets up the execution of tests and provides the outcome to the user 
"""
import unittest


class SimpleTest(unittest.TestCase):
    def test_upper(self):
        result = 'Foo'.upper()
        expected_result = 'FOO'
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()

"""
Running the Test

The possible outcomes are:
-OK - all test passed
-Fail - one or many tests failed and an AssertionError exception is raised
-Error - the tests raised an exception other that AssertionError
"""

"""
Basic Unittest Terms

-unittest.TestCase - create test cases by subclassing it
-assertEqual() / assetNotEqual() - tests the the two arguments are equal/unequal in value
-assertTrue() / assertFalse() - tests that the argument has a boolean value True/False
-assertIn() / assertNotIn() - tests that the first argument is in/ in not in the second
-assertRaises() - raises a specific exception
-unittest.main() - provides a command line interface to the test script
-setUp() - prepares the test fixture 
    The method is called immediately before the test method
    
Test Example

If we have a class Person with methods get_full_name() and get_info():  
"""


class Person:
    def __init__(self, first, last, age):
        self.first_name = first
        self.last_name = last
        self.age = age

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_info(self):
        return f'{self.first_name} {self.last_name} is {self.age} old!'


"""
We can test both methods using the code below:
"""

import unittest


class PersonTest(unittest.TestCase):
    def setUp(self):
        self.person = Person('Lue', 'Peterson', 25)

    def test_get_full_name(self):
        result = self.person.get_full_name()
        expected = 'Lue Peterson'
        self.assertEqual(result, expected)

    def test_get_info(self):
        result = self.person.get_info()
        expected = 'Lue Peterson is 25 old!'
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

"""
Unittest Modules

Advantages to placing the test code in a separate module:
-Test module can be run stand alone from the command line
-The test code can more easily be separated from snipped code
-Tested code can be refactored more easily 
-If the testing strategy changes there is no need to change the source code

Example Unittest Modules

Testing the class Person from previous example:
- Create the test in separate module
* Project
- __init__.py
- person.py
* tests
- __init__.py
- test_person.py

Include them in a package in order to be able to make proper imports from the modules

import unittest
from project.person import Person

class PersonTest(unittest.TestCase):
    def setUp(self):
        self.person = Person('Lue', 'Peterson', 25)

    def test_get_full_name(self):
        result = self.person.get_full_name()
        expected = 'Lue Peterson'
        self.assertEqual(result, expected)

    def test_get_info(self):
        result = self.person.get_info()
        expected = 'Lue Peterson is 25 old!'
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
"""

"""
Mocking

In simple English mocking is make a replica or imitation of something 

In programming an object that you want to test may have dependencies on other complex objects

Used to:
-Simulate the behavior of the real objects
-Isolate the behavior of an object

Based on the action -> assertion pattern 
Designed for use with unittest

Example:

In unit testing we want ro test methods of one class in isolation but classes are not isolated
Thy are using services and methods from other classes
We mock the services and methods from other classes and simulate the real behavior
"""

"""
How to write good tests
Assertion messages

Assertions can show messages
-Helps with diagnostics

def get_info(self):
    result = self.person.get_info()
    expected = 'lue Peterson is 25 old!  # Assertion message
    self.assertEqual(result, expected)
"""

"""
DRY (Dont Repeat Yourself) 
"""


# class DogTests(unittest.TestCase):
#     def setUp(self):
#         self.dog = Dog('Terra', 6)  # Executes before each test
#
#     def test_init(self):
#         self.assertEqual(self.dog.species, 'Terra')
#         self.assertEqual(self.dog.age, 6)
#
#     def test_get_full_info(self):
#         result = self.dog.get_full_info()
#         expected = 'Dog: Terra, 4 years old'
#         self.assertEqual(result, expected)


"""
Naming Tests
Test names
-Should use business domain terminology  
-Should be descriptive amd readable

Incorrect:
test_increment_number(self): ...
test_test1(self): ...
test_transfer(self): ...

Correct:
test_deposit_x_euro_should_increase_balance_with_x_euro(self): ...
test_deposit_negative_euro_should_not_increase_balance(self): ...
"""

"""
Seven Testing Principles

1: Testing is context dependent:
-Testing is done differently in different context
Example:
Safety critical software is tested differently from an e-commerce setl 

2: Exhaustive testing is impossible 
-All combinations of inputs and preconditions are usually almost infinity number
-Testing everything is not feasible 
-Except for trivial cases
-Risk analysis and priorities should be used to focus testing efforts

3: Early testing is always preferred 
-Testing activities shall be started as early as possible
-And shall be focused on defined objectives 
-The later a bug is found the more it costs!

4: Defect clustering
-Testing effort shall be focused proportionally 
-To the expected and later observed defect density of modules
-A small number of modules usually contains most of the defects discovered
-Responsible for most of the operational features 

5: Pesticide paradox 
-Same tests repeated over and over again tend to lose their effectiveness 
-Previously undetected defects remain undiscovered 
-New and modified test cases should be developed

6:Testing shows presence of defects
-Testing can show that defects are present
-Cannot prove that there are no defects
-Appropriate testing reduces the probability for defects 

7: Absence of errors fallacy
-Finding and fixing defects it self does not help in these cases:
    -The system built is unusable 
    -Does not fulfill the user needs and expectations
"""