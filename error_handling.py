"""
Error handling (Syntax, Index, Key, Type, Value, Name Error)

Encountering errors and exceptions can be very frustrating at times
Once you know why you get certain types of errors they become much easier to fix
They are at lease two distinguishable kinds of errors:
-Syntax errors
-Exceptions

Syntax error also known as parsing errors are perhaps the most common kind of complain you get while you are still
learning python
"""
# while True print('hello world')
"""while True print('hello world')
               ^
SyntaxError: invalid syntax"""

"""
Exception
Even if a statement or expression is syntactically correct it may cause an error when an attempt is made to 
execute it
Errors detected during executing are called exceptions
When an exception is not handle it results in error mass
Example:
>>>10*(1/0)
error: ZeroDivisionError: division by zero
>>> 4 + spam * 3
error:NameError: name 'spam' is not defined
>>>'2' + 2 
error: TypeError:Can't convert 'int' object to srt implicitly
"""

"""
Common Errors Types 
-SyntaxError
-IndexError - is thrown when trying to access an item at an invalid index
-KeyError - is thrown when a key is not found
-TypeError - is thrown when an operation of function is applied to an object of an inappropriate type like:
TypeError: must be 'str' not 'int'
-ValueError - is thrown when a functions argument is of an inappropriate like:
ValueError: invalid literal for int()  with base10: 'xyz'
-NameError - is thrown when an object could not be found like:
NameError: name 'age' is not defined
"""

"""
Custom Exception

Sometimes you may need to create custom exceptions that serves you purpose
In python users can define such exceptions by creating a new class
Example:
"""

# class Error(Exception):
#     """Base class for other exceptions"""
#     pass
#
#
# class ValueTooSmallError(Error):
#     """Raised when the input value is to small"""
#
#
# num = int(5)
# if num < 10:
#     raise ValueTooSmallError

"""
Catching Exceptions

It possible to write programs that handle selected exceptions
"""

# while True:
#     try:
#         x = int(input('Please enter a number'))
#     except ValueError:
#         print('Ops! That was no valid number. Try again')

"""
We handle only value so if other error occurs the error massage will show up anyway
"""

"""
Try statement

The try statement works as follows:
-The try clause is executed
-If no exceptions occurs the except clause is skipped 
-If the type of the exception matches the except clause is executed
-If the exception is unhandled and execution stops with a message  
"""

"""
Except statement

An except clause may name multiple exceptions as parenthesized tuple
"""
# except(RuntimeError, TypeError, NameError)

"""
Finally statement
If  a 'finally' clause is present the finally clause will execute as the last task before the 'try' statement completes
The 'finally' clause runs whether ot not the 'try' statement produces an exception
"""

try:
    x = int('Petter')
except ValueError:
    print('Cannot convert str to int')
finally:
    print('finally block')

"""
Catching the exception object

If you wanted to examine the exception you can do it using the following syntax
"""

try:
    x = int(input())
except ValueError:
    print('Must be int')

"""
In most cases you want to be as specific as possible
"""

try:
    pass
except ValueError:
    pass
except TypeError:
    pass
