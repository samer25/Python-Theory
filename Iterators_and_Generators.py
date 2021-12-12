"""
Iterators

Iterators is simply an object that can be iterated upon
An object which well return data one element at a time
Iterator object must implement two methods __iter__() and __next__() (iterator protocol)
An object is called iterable if we can get an iterator from it
Such are list tuple string, etc.

Example:
The iter() function (which calls the __iter__() method returns an iterator from an iterable)
"""
my_list = [4, 5, 6, 7, 8, 9]
my_iter = iter(my_list)  # get on iterator using iter()
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
next(my_iter)
print(next(my_iter))

"""
For loops and Iterators

The for loop can iterate automatically through the list
The for loop can iterate over any iterable 
A for loop is implemented as :
iter_obj = iter(iterable)
While True:
    try:
        element = next(iter_obj)  # get the next item
        #  do something with elements 
    except StopIteration:
        #  if StopIteration is raised break
        #  for loop
        #  break
        
Explanation:

The for loop creates an iterator object (iter_obj) by calling iter() on the iterable
Inside the loop it calls next() to get the next element and executes the body of for loop with this value
After all the items exhaust StopIteration is raised which is internally caught and the loop ends
"""

"""
Generators

Generators are simply way of creating iterators
A generator is a function that returns an object(iterator)
This iterator can later be iterated over(one value at a time)  "YIELD"

Example:
"""


def first_n(n):
    num = 0
    while num < n:
        yield num
        num += 1


sum_firs_n = sum(first_n(5))
print(sum_firs_n)

"""
The yield statement

If a function contains at least one yield statement it becomes a generator function
Both yield and return will return a value from a function 
THE DIFFERENCE BETWEEN YIELD AND RETURN IS THAT THE RETURN STATEMENT TERMINATE A FUNCTION ENTIRELY
Yield however pauses the function saving all its states and later continues from there on successive calls
"""

"""
Generators vs normal functions 

Generator function contain one or more yield statements 
It returns an iterator but does not start execution immediately
Methods like  __iter__() and __next__() are implemented automatically 
Once the function terminates StopIteration is raised automatically on further calls

Example: Generator function
"""


def my_gen():
    n = 1
    print('This is printed first')
    yield n
    n += 1
    print('This is printed second')
    yield n
    n += 1
    print('This is printed at last')
    yield n


"""
Generator Expression

Generator can be easily created using generator expressions
Same as lambda function creates an anonymous function generator expression creates an anonymous generator function 
The syntax for generator expression is similar to that of list comprehension
The difference between them is that generator expression produces one item at a time

Example: Generator Expression
"""

my_list = [1, 3, 6, 10]  # Initialize the list
# square each term using list comprehension
print([x ** 2 for x in my_list])

# same thing can be done using generator expression
print((x ** 2 for x in my_list))


