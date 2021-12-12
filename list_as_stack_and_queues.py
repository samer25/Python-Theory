"""
Stack(LIFO):
A list structure of function calls and parameters
The process of adding data to a stack is referred to as a push
Retrieving data from a stack is called pop
Elements is a stack are added/removed from the top of LIFO order
"""
"""
In python to add an item to the top of the stack use append()
To retrieve an item from the top of the stack use pop()
"""

"""
Queue(FIFO)
A queue is a first in first out (FIFO)
We use them when we want things to happen in the order that they were called 
"""
"""
In python doing insert or pops from the beginning of a list is slow what why we use collections dequeue
We use append() to add to the queue and popleft() to remove from the queue
"""
from collections import deque

names = deque(['Anna', 'Sammy', 'John'])
