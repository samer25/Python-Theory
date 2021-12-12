"""
A regular expression ot regex is a sequence of characters that define a search pattern
Regular expressions are used in search engines
"""
"""
RegEx Module
Python has a built-in package called re
"""
import re

text = "The rain in Spain"
x = re.search("^The.*Spain$", text)
print(x)

"""
Methods
-findall() function returns a list containing all matches
"""
x = re.findall("ai", text)
print(x)
"""
Matches in the order they are found if ni matches are found an empty list is returned
"""

"""
-search() function searches the string for a match and returns a match object if there a match
if there is more than one match only the first occurrence of the match will returned
if there no matches are found the value None is returned
You can use split() function to return a list where the string has been split at each match 
"""

x = re.split("\s", text)
print(x)
