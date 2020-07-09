# How to merge two dictionaries
# in Python 3.5+

x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

z = {**x, **y}
z = x | y
print(z)

# In Python 2.x you could
# use this:
z = dict(x, **y)
print(z)
{'a': 1, 'c': 4, 'b': 3}

# In these examples, Python merges dictionary keys
# in the order listed in the expression, overwriting 
# duplicates from left to right.
#
# See: https://www.youtube.com/watch?v=Duexw08KaC8



# Different ways to test multiple
# flags at once in Python
x, y, z = 0, 1, 0

if x == 1 or y == 1 or z == 1:
    print('passed')

if 1 in (x, y, z):
    print('passed')

# These only test for truthiness:
if x or y or z:
    print('passed')

if any((x, y, z)):
    print('passed')


# How to sort a Python dict by value
# (== get a representation sorted by value)

xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

print(sorted(xs.items(), key=lambda x: x[1]))
#[('d', 1), ('c', 2), ('b', 3), ('a', 4)]

# Or:
import operator
print(sorted(xs.items(), key=operator.itemgetter(1)))
#[('d', 1), ('c', 2), ('b', 3), ('a', 4)]




# The get() method on dicts
# and its "default" argument

name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
}

def greeting(userid):
    return "Hi %s!" % name_for_userid.get(userid, "there")

print(greeting(382))
#"Hi Alice!"

print(greeting(333333))
#"Hi there!"


"""
name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
}

def greeting(userID): 
    return "Hi {}!".format(name_for_userid.get(userID, "there \nSorry we don't have your Username in our database"))

print(greeting(1))
"""




# https://towardsdatascience.com/8-advanced-python-tricks-used-by-seasoned-programmers-757804975802

#Sorting Objects by Multiple Keys

people = [
{ 'name': 'John', "age": 64 },
{ 'name': 'Janet', "age": 34 },
{ 'name': 'Ed', "age": 24 },
{ 'name': 'Sara', "age": 64 },
{ 'name': 'John', "age": 32 },
{ 'name': 'Jane', "age": 34 },
{ 'name': 'John', "age": 99 },
]

"""
But we don’t just want to sort it by name or age, we want to sort it by both fields. 
In SQL, this would be a query like:
SELECT * FROM people ORDER by name, age
"""

#To achieve sorting by name and age, we can do this:

import operator
people.sort(key=operator.itemgetter('age'))
people.sort(key=operator.itemgetter('name'))

#This gives us the result we're looking for
"""
[
 {'name': 'Ed',   'age': 24},
 {'name': 'Jane', 'age': 34},
 {'name': 'Janet','age': 34},
 {'name': 'John', 'age': 32},
 {'name': 'John', 'age': 64},
 {'name': 'John', 'age': 99},
 {'name': 'Sara', 'age': 64}
]
"""

#List Comprehensions

#[ expression for item in list if conditional ]

mylist = [i for i in range(10)]
print(mylist)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Or even this one
squares = [x**2 for x in range(10)]
print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#We can even use a function
def some_function(a):
    return (a + 5) / 2
    
my_formula = [some_function(i) for i in range(10)]
print(my_formula)
# [2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0]

#We can use an if statement to filter the list
filtered = [i for i in range(20) if i%2==0]
print(filtered)
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


#Check memory usage of your objects

import sys

mylist = range(0, 10000)
print(sys.getsizeof(mylist))
# 48
# A range is a lot more memory efficient than using an actual list of numbers.

import sys

myreallist = [x for x in range(0, 10000)]
print(sys.getsizeof(myreallist))
# 87632
# Try to avoid calling out full lists of Objects like this.

#Using Data Classes
"""Since version 3.7, Python offers data classes. There are several advantages over regular classes or other alternatives like returning multiple values or dictionaries:

    a data class requires a minimal amount of code
    you can compare data classes because __eq__ is implemented for you
    you can easily print a data class for debugging because __repr__ is implemented as well
    data classes require type hints, reduced the chances of bugs

Here’s an example of a data class at work:"""

from dataclasses import dataclass

@dataclass
class Card:
    rank: str
    suit: str
    
card = Card("Q", "hearts")

print(card == card)
# True

print(card.rank)
# 'Q'

print(card)
Card(rank='Q', suit='hearts')

#In Depth here: https://realpython.com/python-data-classes/

#The attrs Package

#Instead of data classes, you can use attrs. There are two reasons to choose attrs:
#
#    You are using a Python version older than 3.7
#    You want more features
#
#The attrs package supports all mainstream Python versions, including CPython 2.7 and PyPy. 
# Some of the extras attrs offers over regular data classes are validators, and converters. 
# Let’s look at some example code:

import attr
@attrs
class Person(object):
    name = attr.ib(default='John')
    surname = attr.ib(default='Doe')
    age = attr.ib(init=False)
    
p = Person()
print(p)
p = Person('Bill', 'Gates')
p.age = 60
print(p)

# Output: 
#   Person(name='John', surname='Doe', age=NOTHING)
#   Person(name='Bill', surname='Gates', age=60)

def funcname(parameter_list):
    pass


"""Find the Most Frequently Occurring Value

To find the most frequently occurring value in a list or string:"""

test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
print(max(set(test), key = test.count))
# 4

"""max() will return the highest value in a list. The key argument takes a single argument function to customize the sort order, in this case, it’s test.count. The function is applied to each item on the iterable.
test.count is a built-in function of list. It takes an argument and will count the number of occurrences for that argument. So test.count(1) will return 2 and test.count(4) returns 4.
set(test) returns all the unique values from test, so {1, 2, 3, 4}"""
test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
from collections import Counter
print(Counter(test).most_common(1))
# [4: 4]


def get_user(id):
    # fetch user from database
    # ....
    return name, birthdate

name, birthdate = get_user(4)