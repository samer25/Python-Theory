"""
There can be more than one additional dimension to list
Multidimensional lists are the lists within lists
-grid is a basic example of two-dimensional list
-cube is a basic example of three dimensional list

When dealing with graphics( pixels on the screen are in grid formation)

Creating MD list with zeros
-Using loops
"""

x = []

for i in range(3):
    x.append([])
    for j in range(2):
        x[i].append(0)

print(x)

"""
-Using comprehension
"""

x = [[0 for i in range(2)] for j in range(3)]

print(x)

"""
Accessing Elements
To access an element in a two dimensional list for example you should give the row and the column of the element 
"""
print(x[1][0])

"""
With e dimensional list 
"""

x = [[[1, 2], [3, 4], [5, 6], [7, 8]]]
print(x[0][1][1])

"""
Traversing Elements 
"""
x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(x)):
    for j in range(len(x[i])):
        print(x[i][j], end=" ")
    print()
