"""
A data type is a classification that specifies which type of value a variable has and what type of operations can be
applied to it to it
In Python the following data types are:
- Numeric types: int, float, complex
- String
- List, Set, Tuple, Dictionary
-Boolean
"""
type_int = int(25)

type_float = float(2.2)

type_complex = complex(1 + 2j)

print(type(type_int))
print(type(type_float))
print(type(type_complex))

"""
String
A string is a sequence of characters
Computers do not deal with characters, they deal with numbers
A character is stored and manipulated as a combination of 0s and 1s
In python, a string is sequence of unicode characters
"""
"""
Methods 
-str() function converts the specified value into a string
-split() method splits a string into a list
-isdigit() check if a character is a digit
-isupper()/islower() check if a character is upper/lower case
-upper()/lower() convert to upper/lower case
-fstrip()/lstrip()/strip() - removes white spaces in start/end or both
-replace() method to replace a specified phrase with another specified phrase
if you want to replace a word more that once add count 
txt.replace("banana", apple, 2)
"""

"""
Python is a dynamic language 
Variable are not directly associated with any particular value type
Any variable can be assigned and re-assigned value of all types
"""
value = int(12)
print(value)
value = str('Car')
print(value)
value = float(1.2)
print(value)

"""
String used to represent textual data 
Each element in the string Occupies a position in the string 
The length of a string is the number of element in it
The string literals in python are surrounded by either single or double quotation mark
String are immutable unlike in languages like C
Python string are immutable
"""
student_name = 'Sammy Mahamid'
for i in range(len(student_name)):
    print(f'index: {i}')

"""Boolean represents a logical entity and can have two value:
-True
-False
"""
boolean_true = True
boolean_false = False

"""List contains items separated by commons and enclosed within square brackets """

names_in_list = ['Anna', 'Sammy', 'Jhon']

"""
Tuple is a collections which is ordered and unchangeable
In python tuples are written with round brackets
"""
names_in_tuple = ('Anna', 'Sammy', 'Jhon')

"""
Set is a collection witch is unordered and un-indexed and the value is unique
"""
names_in_set = {'Anna', 'Sammy', 'Jhon'}

"""
Dictionary is a collection which is unordered, changeable and indexed
While other date type have only value as an element, a dictionary has key and value
Value can be of any data type and can repeat
Keys must be of immutable type and must be unique 
"""
names_in_dictionary = {1: 'Anna', 2: 'Sammy', 3: 'Jhon'}
"""
Key can be used either inside square brackets ot with the get() method
The difference while using get() is that it returns "None" instead of key error if the key is not found
Dictionary are mutable
"""
print('Get:')
print(names_in_dictionary.get(2))
"""
We can add new items or change the value of existing items using assigment operator
If the key is already present value gets updated else a new pair is added to the dictionary
"""
names_in_dictionary[4] = 'Maria'
print(names_in_dictionary)

"""
Iterating through key
Using the key() method to get all the keys from a dictionary
"""

for key in names_in_dictionary.keys():
    names_in_dictionary[key] += ','

print(names_in_dictionary)

"""
Iterating through value
Using the values() method to get all the value
"""
for value in names_in_dictionary.values():
    print(value)

"""
Iterating using items()
Iterating using tuble (key, value) pairs
using the items() method to iterate through key and value pairs
"""
for (key, value) in names_in_dictionary.items():
    print(f'{key}: {value}')

"""We can also check if a value exists by using the value() """
if 'Anna,' in names_in_dictionary.values():
    print('Exists')

"""
Dictionary methods
- clear() : remove all the elements from the dictionary
- copy() : returns a copy of the dictionary
- pop() : removes the specific item from the dictionary 
- popitem() : remove the item that was last inserted 
"""

"""None key word is used to define a null value"""
none_value = None
