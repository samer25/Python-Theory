"""
Python file object
Built-in function to create and manipulate file
io - module is the default module for accessing file
-Don't need to import it

open() - returns a file object whose type depends on:
-The mode
-File operation such as reading and writing
-Files in a text mode(w, r, wt, rt, etc) returns a TextIOWrapper
"""

"""
Opening a file
-open() function in python opens a file object
"""
file = open('text.txt', 'r')

"""
The arguments are file name and the mode(reading and etc.)
All arguments except file are optional and have default value
If the file is not in the current directory the full path to the file can be provided
"""
file_path = open('./text.txt', 'r')

"""
If the file does not exist (FileNotFoundError) is throw
It can be caught a try finally block
"""
try:
    file = open('invalid.txt', 'r')
except FileNotFoundError:
    print("File was not found!")
finally:
    print('Exit!')

"""
File modes
The mode argument is optional and specifies the mode for manipulating the file
It's default value is 'r' open for reading in the text mode
"""

"""
File modes in Python
-'w': open for writing, truncating the file first
-'x': create a new file and open it for writing
-'a': open for writing, appending to the end of the file if it exists
-'t': text mode(default)
-'b': binary mode
-'+': open a disk file for updating (reading nad writing)
"""
"""Reading readline function"""
file = open('text.txt')
print(file.readline(5))
print(file.readline())

"""
Looping over a file object
"""
file = open('text.txt', 'r')
for line in file:
    print(line, end=' ')

"""
Creating and writing a file
"""

new_file = open('new.txt', 'w')
new_file.write("Tis is the write command")
new_file.close()
new_file = open('new.txt', 'r')
print(new_file.readline())

"""
Append to a file
"""

new_file = open('new.txt', 'a')
line = ['\nwrite ', ' in ', ' file ']
new_file.writelines(line)
new_file.close()
new_file = open('new.txt', 'r')
print(new_file.readline())

"""
With Statement
File opened with (with) statement will be closed automatically once it leaves the (with) block 
"""
with open('with_file.txt', 'w') as f:
    f.write('This is with "with" statement')

"""
Deleting a file
To delete a file you must import the os module
"""
import os

os.remove('with_file.txt')
"""Can use full path"""
"""
Keep in mind if the file does not exist and error will be raised
"""

file_path = 'invalid.txt'
if os.path.exists(file_path):
    os.remove(file_path)
