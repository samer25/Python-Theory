"""
Functions is a named piece of code can take parameters and return result
Splits large of problems into small pieces
Better organization of the program
Improves code readability
Improves code understandability

Avoiding repeating code,  improves code maintainability and code re-usability(Using existing functions several times)
"""
names_students = ['Anna', 'Sammy', 'John', 'Petter']


def order_name_by_alphabetical(name_list):
    return sorted(name_list)


print(order_name_by_alphabetical(names_students))

"""
Parameter is variable defined in functions definition
"""


def func(parameter):
    return parameter


"""
Argument is actual value passed to the function
"""
argument = []
func(argument)

"""function argument can have default value"""


def func(age=25):
    return age


"""Packing arguments (*args and **kwargs)"""


def some_functional(*args, **kwargs):
    pass


"""
This operation is called packing
We pack all the arguments into one single variable
We use packing when we need to be passed to a function
We use *args to pack arguments into tuple 
"""


def some_function(*args):
    print(args)


some_function(2, 3, 4)

"""
The **kwargs allows you to pass key worded variable length of arguments to a function 
"""


def greet_me(**kwargs):
    for (key, value) in kwargs.items():
        print(f'{key}, {value}')


greet_me(Hello='Petter')

"""
You can also use keyword argument and *args
"""


def some_function(arg1, *rest_args):
    print(arg1 + sum(rest_args))


some_function(1, 2, 3, 4, 5)

"""
Unpacking

We can use * to unpack the list so that all elements of it can be passed as different parameters
And we can use ** to unpack a dictionary so all of its elements are passed as key worded arguments 
Note that the length of the list that you unpack must be the same as the amount of parameters in the function 
"""


def print_num(a, b, c):
    print(a, b, c)


nums = [1, 2, 3]
print_num(*nums)

"""
Note that the keys of the dictionary must match the names of the parameters of the function order of the keys does not 
matter 
"""


def func_d(name, age):
    print(f'{name} is {age} old')


person = {'age': 20, 'name': 'Petter'}
func_d(**person)

"""
Recursion
The process in which a function calls itself is called recursion
The function that is calling itself is called a recursive function 
A recursive function has the following structure
-A base case
-A recursive case 
"""


def rec(n):
    if n == 1:
        return 1
    return n + rec(n - 1)


print(rec(5))
