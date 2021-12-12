"""
The sorted() method
The sorted() method sorts the element of a given iterable to Ascending or descending order
"""
names_students = ['Anna', 'Sammy', 'John', 'Petter']
"""
iterable sequence of collection or any iterator
"""
print(sorted(names_students))

"""reverse (optional) if true the sorted list is reversed(or sorted in Descending order)"""
print(sorted(names_students, reverse=True))
"""key (optional) function that serves as a key for the sort comparison"""

print(sorted(names_students, key=len))
