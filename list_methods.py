"""
List method are:
append() - add single element at the end
extend() - add multiple elements at the end
insert() - add single elements at a specific index
pop() - removes last element and returns it
remove() - removes by value
count() - finds all occurrence in a list
index() - finds the index of the first occurrence
reverse() - reverse the elements
clear() - removes all elements
"""
names_students = ['Anna', 'Sammy', 'John', 'Petter']
names_students.append('Lissa')
print(names_students)
names_students.extend(['Maria', 'Georgy'])
print(names_students)
names_students.insert(0, 'Ira')
print(names_students)
names_students.pop()
print(names_students)
names_students.remove('Anna')
print(names_students)
print(names_students.count('Sammy'))
print(names_students.index('John'))
names_students.reverse()
print(names_students)
names_students.clear()
print(names_students)
