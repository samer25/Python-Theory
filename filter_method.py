"""
Using the filter() method to filter elements that fulfill a given condition

The filter() method returns an iterator object so you have to converted to list
"""

numbers = [1, 2, 3, 4, 5]

even_number = list(filter(lambda x: x % 2 == 0, numbers))
print(even_number)

"""
Or you can looped:
"""

ages = [5, 12, 17, 18, 24, 32]


def func(x):
    if x < 18:
        return False
    else:
        return True


adults = filter(func, ages)

for x in adults:
    print(x)
