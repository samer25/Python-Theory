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
