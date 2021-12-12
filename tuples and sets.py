"""
Tuple is a collections which is ordered and unchangeable
In python tuples are written with round brackets
Tuples are sequence of immutable objects
Tuples cannot be changed unlike lists
"""
names_in_tuple = ('Anna', 'Sammy', 'Jhon')

"""
There are only two available tuple methods
-count - returns the length of the tuple 
-index - returns the index of a particular element
"""
print(names_in_tuple.count('Sammy'))
print(names_in_tuple.index('Anna'))

"""
Tuple unpacking allows to extract tuple elements automatically from a list of variables
"""
first, second, third = names_in_tuple
print(first, second, third)
"""
Set is a collection witch is unordered and un-indexed and the value is unique
Set is an unordered collection of items 
Every element of a set is unique
Sets are mutable
Sets can be used to perform mathematical set operations:
-union()
-update()
-intersection()
-intersection_update()
-difference()
-difference_update()
-symmetric_difference()
-symmetric_difference_update()
-isdisjoint()
-issubset()
-issuperset()
"""

names_in_set = {'Anna', 'Sammy', 'Jhon'}
