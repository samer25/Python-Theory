"""
Using the map() method to convert list of string to list of integers
The map() method returns an iterator map object so you need to convert it into a list
"""

string_list = ['1', '2', '3']

number_list = list(map(lambda x: int(x), string_list))
print(number_list)

"""
Or:
"""


def addition(n):
    return n + n


numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))
