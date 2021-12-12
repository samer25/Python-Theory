""" for loop is used to iterate over sequence of iterable type like
    - tuple
    - List
    - other iterable types

    for loop does not require an indexing variable to set before hand
"""
students_name = ['John', 'Anna', 'Sammy', 'Clark']
print('For loop:')
for name in students_name:
    print(name)
"""The break statement stops the loop before it has looped through all the items """
print('For loop with break:')
for name in students_name:
    if name == 'Sammy':
        print('found Sammy')
        break

"""The continue statement skips the current iteration of the loop and continue with the next"""
print('For loop with continue:')
for name in students_name:
    if name == "Anna":
        print('skipped Anna')
        continue
    print(name)

"""While loop we can execute a set of statements as long as a condition is true"""
print('While loop:')
while students_name:
    students_name.pop()
    print(students_name)
