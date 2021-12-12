"""
Comprehension are constructs allow sequence to be built from other sequence

Structure:
A list comprehension consists of the following parts:
-An output expression producing elements of the output list
-A variable representing members of the input sequence
-An input sequence
-An optional predicate expression
"""
numbers = [0, 1, 2, 3, 4, 5]

comprehension = [x * 2 for x in numbers if x > 0]
print(comprehension)

"""
Comprehensions provide us with a short way to construct new sequences
Python supports the following 4 types of comprehensions
-List Comp.
-Dictionary Comp.
-Set Comp.
-Generator Comp.
"""
"""List Comprehension"""
x = [num for num in range(5)]
"""list comprehension can include if else statements"""
filtered = [True if x % 2 == 0 else False for x in x]
print(filtered)

"""Dictionary Comprehension"""
info = [("p", 22), ("a", 18)]
dict_comp = {key: value for (key, value) in info}
print(dict_comp)

"""Set comprehension are pretty similar to list comprehension difference is that set comprehension use curl brackets"""
num = {1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3}
unique = {num for num in num}
print(unique)

"""
Nested list comprehension are nothing but a list comprehension within another list comprehension
Usually we use nested comprehension when working with multidimensional list
"""
matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)
