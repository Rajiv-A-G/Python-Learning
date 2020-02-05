import pytest
import random

"""
# Variable Declaration
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)
"""

"""
# Random Number
print(random.randint(1,100))
"""

'''
# Format in print
a = "My {2} {0} {1}"
b = a. format("is", "Rajiv", "name")
print(b)
'''


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
        self.graduation = 12


a = [1, [1, 2, 3], '4']
try:
    print(a)
except:
    pass


