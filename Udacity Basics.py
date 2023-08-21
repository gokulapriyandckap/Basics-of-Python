# Arithmetic Operators
# Arithmetic operators
#
# + Addition
# - Subtraction
# * Multiplication
# / Division
# % Mod (the remainder after dividing)
# ** Exponentiation (note that ^ does not do this operation, as you might have seen in other languages)

# Examples
#
# print(3 + 5) # 8
# print(1 + 2 + 3 * 3) # 12
# print(3 ** 2) # 9
# print(9 % 2) # 1



# Integers and Floats
# There are two Python data types that could be used for numeric values:
#
# int - for integer values
# float - for decimal or floating point values
# You can create a value that follows the data type by using the following syntax:

# x = int(4.7)   # x is now an integer 4
# y = float(4)   # y is now a float of 4.0



# Python Best Practices

# Good
# print(4 + 5)
# Bad
# print(                       4 + 5)


# Booleans , Compariosn Operators and Logical Operators
# Examples

# x = 42 > 43 # False
#
# age = 14
# is_teen = age > 12 and age < 20
# print(is_teen) # True

# Strings

# You can also include a \ in your string to be able to include one of these quotes:
#
# >>> this_string = 'Simon\'s skateboard is in the garage.'
# >>> print(this_string)
# Simon's skateboard is in the garage.



# >>> first_word = 'Hello'
# >>> second_word = 'There'
# >>> print(first_word + second_word)
#
# HelloThere
#
# >>> print(first_word + ' ' + second_word)
#
# Hello There
#
# >>> print(first_word * 5)
#
# HelloHelloHelloHelloHello
#
# >>> print(len(first_word))
#
# 5




# The len() function
# len() is a built-in Python function that returns the length of an object, like a string. The length of a string is the number of characters in the string. This will always be an integer.
#
# There is an example above, but here's another one:
#
# print(len("ababa") / len("ab"))
# 2.5





# Type and Type Conversion
#
# int
# float
# bool
# string
# type()
#  print(type(633))
# int
#  print(type(633.0))
# float
#  print(type('633'))
# str
#  print(type(True))
# bool

# string methdods
# len("this")
# type(12)
# my_string = "Hello world"

# my_string.islower()
# True
#  my_string.count('o')
# 2
#  my_string.find('a')
# 3


# Examples
# verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
# print(verse, "\n")
#
# print("Verse has a length of {} characters.".format(len(verse)))
# print("The first occurence of the word 'and' occurs at the {}th index.".format(verse.find('and')))
# print("The last occurence of the word 'you' occurs at the {}th index.".format(verse.rfind('you')))
# print("The word 'you' occurs {} times in the verse.".format(verse.count('you')))


# Data strucrtures
# Lists and Membership Operators

"""Lists : Data structures are containers that organize and group data types together in different ways.
A list is one of the most common and basic data structures in Python.
You saw here that you can create a list with square brackets.
 Lists can contain any mix and match of the data types you have seen so far."""

# Examples
#
# months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
#
# print(months[0]) # January
# print(months[1]) # February
# print(months[7]) # August
# print(months[-1]) # December
# print(months[25]) # IndexError: list index out of range


# list_of_random_things = [1, 3.4, 'a string', True]
 # list_of_random_things[0] #output 1

# months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
#
# q3 = months[6:9]
# print(q3) # [ 'July', 'August', 'September']
#
# first_half = months[:6]
# print(first_half) # ['January', 'February', 'March', 'April', 'May', 'June']
#
# second_half = months[6:]
# print(second_half) # ['July', 'August', 'September', 'October', 'November', 'December']
#
# print(len(months)) # 12
#
# greeting = "Hello there"
# print(len(greeting)) # 11


# Slice and Dice with Lists

# list_of_random_things = [1, 3.4, 'a string', True]
# list_of_random_things[1:2] #output [3.4]

# list_of_random_things[:2]  #output [1, 3.4]


# List Methods.
# new_str = "\n".join(["fore", "aft", "starboard", "port"])
# print(new_str)

# Output:
# fore
# aft
# starboard
# port

# .join()
# name = "-".join(["García", "O'Kelly"])
# print(name)
# Output: García-O'Kelly


# .append()
# letters = ['a', 'b', 'c', 'd']
# letters.append('z')
# print(letters)
# Output: ['a', 'b', 'c', 'd', 'z']


# Tuples
"""A tuple is another useful container. It's a data type for immutable ordered sequences of elements.
They are often used to store related pieces of information."""
# Examples
#
# AngkorWat = (13.4125, 103.866667)
#
# print(type(AngkorWat))
# # <class 'tuple'="">
#
# print("AngkorWat is at latitude: {}".format(AngkorWat[0]))
# # AngkorWat is at latitude: 13.4125
#
# print("AngkorWat is at longitude: {}".format(AngkorWat[1]))
# AngkorWat is at longitude: 103.866667


# location = (13.4125, 103.866667)
# print("Latitude:", location[0])
# print("Longitude:", location[1])

# dimensions = 52, 40, 100
# length, width, height = dimensions
# print("The dimensions are {} x {} x {}".format(length, width, height))


# Sets
"""A set is a data type for mutable unordered collections of unique elements.
 One application of a set is to quickly remove duplicates from a list."""

# numbers = [1, 2, 6, 3, 1, 1, 6]
# unique_nums = set(numbers)
# print(unique_nums)
# output: {1, 2, 3, 6}


# fruit = {"apple", "banana", "orange", "grapefruit"}  # define a set
#
# print("watermelon" in fruit)  # check for element
#
# fruit.add("watermelon")  # add an element
# print(fruit)
#
# print(fruit.pop())  # remove a random element
# print(fruit)


# This outputs:
# False
# {'grapefruit', 'orange', 'watermelon', 'banana', 'apple'}
# grapefruit
# {'orange', 'watermelon', 'banana', 'apple'}

# Dictionaries.
"""A dictionary is a mutable data type that stores mappings of unique keys to values. Here's a dictionary that stores elements and their atomic numbers."""
# elements = {"hydrogen": 1, "helium": 2, "carbon": 6}

# print(elements["helium"])  # print the value mapped to "helium"
# elements["lithium"] = 3  # insert "lithium" with a value of 3 into the dictionary


# print("carbon" in elements)
# print(elements.get("dilithium"))
# This would output: # True ,None


# Compound Data Structures
# We can include containers in other containers to create compound data structures.
# For example, this dictionary maps keys to values that are also dictionaries!
# elements = {"hydrogen": {"number": 1,
#                          "weight": 1.00794,
#                          "symbol": "H"},
#               "helium": {"number": 2,
#                          "weight": 4.002602,
#                          "symbol": "He"}}


# We can access elements in this nested dictionary like this.
# helium = elements["helium"]  # get the helium dictionary
# hydrogen_weight = elements["hydrogen"]["weight"]  # get hydrogen's weight


# You can also add a new key to the element dictionary.
# oxygen = {"number":8,"weight":15.999,"symbol":"O"}  # create a new oxygen dictionary
# elements["oxygen"] = oxygen  # assign 'oxygen' as a key to the elements dictionary
# print('elements = ', elements)


# Output is:
# elements =  {"hydrogen": {"number": 1,
#                           "weight": 1.00794,
#                           "symbol": 'H'},
#                "helium": {"number": 2,
#                           "weight": 4.002602,
#                           "symbol": "He"},
#                "oxygen": {"number": 8,
#                           "weight": 15.999,
#                           "symbol": "O"}}```


# verse_dict =  {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
# print(verse_dict, '\n')

# find number of unique keys in the dictionary
# num_keys = len(set(verse_dict))
# print(num_keys)

# find whether 'breathe' is a key in the dictionary
# contains_breathe = 'breathe' in verse_dict
# print(contains_breathe)

# create and sort a list of the dictionary's keys
# sorted_keys = sorted(verse_dict.keys())
# print(sorted_keys)

# get the first element in the sorted list of keys
# print(sorted_keys[0])

# find the element with the highest value in the list of keys
# print(max(sorted_keys))

# Output:
# if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise
#
# ['if', 'you', 'can', 'keep', 'your', 'head', 'when', 'all', 'about', 'you', 'are', 'losing', 'theirs', 'and', 'blaming', 'it', 'on', 'you', 'if', 'you', 'can', 'trust', 'yourself', 'when', 'all', 'men', 'doubt', 'you', 'but', 'make', 'allowance', 'for', 'their', 'doubting', 'too', 'if', 'you', 'can', 'wait', 'and', 'not', 'be', 'tired', 'by', 'waiting', 'or', 'being', 'lied', 'about', 'don’t', 'deal', 'in', 'lies', 'or', 'being', 'hated', 'don’t', 'give', 'way', 'to', 'hating', 'and', 'yet', 'don’t', 'look', 'too', 'good', 'nor', 'talk', 'too', 'wise']
#
# {'or', 'when', 'hating', 'make', 'all', 'head', 'waiting', 'losing', 'don’t', 'to', 'look', 'about', 'yourself', 'by', 'wise', 'doubting', 'trust', 'deal', 'allowance', 'being', 'too', 'wait', 'in', 'nor', 'for', 'theirs', 'and', 'if', 'on', 'lied', 'are', 'your', 'but', 'give', 'yet', 'lies', 'good', 'men', 'tired', 'doubt', 'hated', 'blaming', 'can', 'be', 'keep', 'their', 'not', 'it', 'talk', 'way', 'you'}
#
# 51

# If Statement
# An if statement is a conditional statement that runs or skips code based on whether a condition is true or false.
# Here's a simple example.
# if phone_balance < 5:
#     phone_balance += 10
#     bank_balance -= 10

# If, Elif, Else
# In addition to the if clause, there are two other optional clauses often used with an if statement.
# For example:
# if season == 'spring':
#     print('plant the garden!')
# elif season == 'summer':
#     print('water the garden!')
# elif season == 'fall':
#     print('harvest the garden!')
# elif season == 'winter':
#     print('stay indoors!')
# else:
#     print('unrecognized season')



# For Loops
"""Python has two kinds of loops - for loops and while loops. A for loop is used to "iterate", or do something repeatedly, over an iterable.
An iterable is an object that can return one of its elements at a time. This can include sequence types, 
such as strings, lists, and tuples, as well as non-sequence types, such as dictionaries and files."""


# Example
# Let's break down the components of a for loop, using this example with the list cities:
# cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
# for city in cities:
#     print(city)
# print("Done!")


# for i in range(3):
#     print("Hello!")
# Output:
# Hello!
# Hello!
# Hello!


# Creating and Modifying Lists

## Creating a new list
# cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
# capitalized_cities = []
#
# for city in cities:
#     capitalized_cities.append(city.title())


cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

# for index in range(len(cities)):
#     cities[index] = cities[index].title()
#
# print(cities)



# names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
# usernames = []
#
# for name in names:
#     usernames.append(name.lower().replace(" ", "_"))
#
# print(usernames)
# Output: ['joey_tribbiani', 'monica_geller', 'chandler_bing', 'phoebe_buffay']



# Modify Usernames with Range
# usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
#
# for i in range(len(usernames)):
#     usernames[i] = usernames[i].lower().replace(" ", "_")
# Output:
# ['joey_tribbiani', 'monica_geller', 'chandler_bing', 'phoebe_buffay']



# Tag Counter
# You can use string indexing to find out if each token begins and ends with angle brackets.
#
# tokens = ['<greeting>', 'Hello World!', '</greeting>']
#
# count = 0
# for token in tokens:
#     if token[0] == '<' and token[-1] == '>':
#         count += 1
# print(count)
# Output:
# 2

#
# Create an HTML List
# items = ['first string', 'second string']
# html_str = "<ul>\n"          # The "\n" here is the end-of-line char, causing
#                              # chars after this in html_str to be on next line
#
# for item in items:
#     html_str += "<li>{}</li>\n".format(item)
# html_str += "</ul>"
#
# print(html_str)
# Output:
# <ul>
# <li>first string</li>
# <li>second string</li>
# </ul>



# While Loops
"""For loops are an example of "definite iteration" meaning that the loop's body is run a predefined number of times.
 This differs from "indefinite iteration" which is when a loop repeats an unknown number of times and ends when some condition is met, which is what happens in a while loop."""

#Here's an example of a while loop.
# card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
# hand = []
#
# ## adds the last element of the card_deck list to the hand list
# ## until the values in hand add up to 17 or more
# while sum(hand)  < 17:
#     hand.append(card_deck.pop())

# Factorials with While Loops
# Here is our solution for this one:
## number to find the factorial of
# number = 6
# ## start with our product equal to one
# product = 1
# ## track the current number being multiplied
# current = 1

# while  current <= number:
#     # multiply the product so far by the current number
#     product *= current
#     # increment current with each iteration until it reaches number
#     current += 1
#
#
# ## print the factorial of number
# print(product)


#
# Nearest Square
# limit = 40
#
# num = 0
# while (num+1)**2 < limit:
#     num += 1
# nearest_square = num**2
#
# print(nearest_square)
# Output:36



# Zip
"""zip returns an iterator that combines multiple iterables into one sequence of tuples.
 Each tuple contains the elements in that position from all the iterables. For example, printing"""

#
# Zip Coordinates
# x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
# y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
# z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
# labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]
#
# points = []
# for point in zip(labels, x_coord, y_coord, z_coord):
#     points.append("{}: {}, {}, {}".format(*point))
#
# for point in points:
#     print(point)




# Zip Lists to a Dictionary
# cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
# cast_heights = [72, 68, 72, 66, 76]
#
# cast = dict(zip(cast_names, cast_heights))
# print(cast)
# Output:{'Lily': 66, 'Barney': 72, 'Marshall': 76, 'Ted': 72, 'Robin': 68}
# The order of elements in this output may vary since dictionaries are unordered.


# Unzip Tuples
# cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))
#
# names, heights = zip(*cast)
# print(names)
# print(heights)
# Output:('Barney', 'Robin', 'Ted', 'Lily', 'Marshall')(72, 68, 72, 66, 76)


# Transpose with Zip
# data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
#
# data_transpose = tuple(zip(*data))
# print(data_transpose)
# Output: ((0, 3, 6, 9), (1, 4, 7, 10), (2, 5, 8, 11))


#
# Enumerate
# cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
# heights = [72, 68, 72, 66, 76]
#
# for i, character in enumerate(cast):
#     cast[i] = character + " " + str(heights[i])
#
# print(cast)
# Output:  ['Barney Stinson 72', 'Robin Scherbatsky 68', 'Ted Mosby 72', 'Lily Aldrin 66', 'Marshall Eriksen 76']


# List Comprehensions

# capitalized_cities = []
# for city in cities:
#     capitalized_cities.append(city.title())
# can be reduced to:  capitalized_cities = [city.title() for city in cities]


# conditional in list Comprehensions
# squares = [x**2 for x in range(9) if x % 2 == 0] # if

# squares = [x**2 for x in range(9) if x % 2 == 0 else x + 3] # if else


# squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]



# Extract First Names
# names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
#
# first_names = [name.split()[0].lower() for name in names]
# print(first_names)
# Output: ['rick', 'morty', 'summer', 'jerry', 'beth']


# Multiples of Three
# multiples_3 = [x * 3 for x in range(1, 21)]
# print(multiples_3)
# Output:[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]


# Filter Names by Scores
# scores = {
#              "Rick Sanchez": 70,
#              "Morty Smith": 35,
#              "Summer Smith": 82,
#              "Jerry Smith": 23,
#              "Beth Smith": 98
#           }
#
# passed = [name for name, score in scores.items() if score >= 65]
# print(passed)
# Output: ['Beth Smith', 'Summer Smith', 'Rick Sanchez']
# The order of elements in this output may vary since dictionaries are unordered.


# Functions.

# Defining Functions
# Example of a function definition:
#
# def cylinder_volume(height, radius):
#     pi = 3.14159
#     return height  *pi*  radius ** 2
# After defining the cylinder_volume function, we can call the function like this.
#
# cylinder_volume(10, 3)
# This is called a function call statement.


# Default Arguments
# We can add default arguments in a function to have default values for parameters that are unspecified in a function call.

# def cylinder_volume(height, radius=5):
#     pi = 3.14159
#     return height  *pi*  radius ** 2

# cylinder_volume(10, 7)  # pass in arguments by position
    # cylinder_volume(height=10, radius=7)  # pass in arguments by name





"""Write a function named readable_timedelta.
 The function should take one argument, an integer days, and return a string that says how many weeks and days that is. 
 For example, calling the function and printing the result like this:"""
# readable_timedelta
# def readable_timedelta(days):
#     # use integer division to get the number of weeks
#     weeks = days // 7
#     # use % to get the number of days that remain
#     remainder = days % 7
#     return "{} week(s) and {} day(s).".format(weeks, remainder)
#
# # test your function
# print(readable_timedelta(10))
# Output:
# 1 week(s) and 3 day(s).


# Documentation.
"""Documentation is used to make your code easier to understand and use.
Functions are especially readable because they often use documentation strings, or docstrings. 
Docstrings are a type of comment used to explain the purpose of a function, and how it should be used.
Here's a function for population density with a docstring."""
# def population_density(population, land_area):
#     """Calculate the population density of an area. """
#     return population / land_area


# Lambda Expressions
"""You can use lambda expressions to create anonymous functions. 
That is, functions that don’t have a name. They are helpful for creating quick functions that aren’t needed later in your code.
This can be especially useful for higher order functions, or functions that take in other functions as arguments."""

# With a lambda expression, this function:

# def multiply(x, y):
#     return x * y
# can be reduced to:
#
# multiply = lambda x, y: x * y


# Scripting the raw Input
# name = input("Enter a Name:")
# print("Hello ;) " +  name.title())

# For calculator
# input  = eval(input("Enter your Number"))
# print(input)

# Specifying Exceptions
# We can actually specify which error we want to handle in an except block like this:
#
# try:
#     # some code
# except ValueError:
#     # some code
# Now, it catches the ValueError exception, but not other exceptions. If we want this handler to address more than one type of exception, we can include a parenthesized tuple after the except with the exceptions.
#
# try:
#     # some code
# except (ValueError, KeyboardInterrupt):
#     # some code
# Or, if we want to execute different blocks of code depending on the exception, you can have multiple except blocks.
#
# try:
#     # some code
# except ValueError:
#     # some code
# except KeyboardInterrupt:
#     # some code

# Handling Input Errors  Here is our solution  for what the revised party_planner function on the previous page could look like, using a try-except block:

# def party_planner(cookies, people):
#     leftovers = None
#     num_each = None
#
#     try:
#         num_each = cookies // people
#         leftovers = cookies % people
#     except ZeroDivisionError:
#         print("Oops, you entered 0 people will be attending.")
#         print("Please enter a good number of people for a party.")
#
#     return (num_each, leftovers)
    # ```


    # Reading and Writing Files
# Reading a File
# with open("sample.txt", "r") as file1:
#     print(file1.read())
#     file1.close()


## demo.py

# import useful_functions as uf

# scores = [88, 92, 79, 93, 85]

# mean = uf.mean(scores)
# curved = uf.add_five(scores)

# mean_c = uf.mean(curved)

# print("Scores:", scores)
# print("Original Mean:", mean, " New Mean:", mean_c)

# print(__name__)
# print(uf.__name__)


# ## useful_functions.py

# def mean(num_list):
#     return sum(num_list) / len(num_list)

# def add_five(num_list):
#     return [n + 5 for n in num_list]

# def main():
#     print("Testing mean function")
#     n_list = [34, 44, 23, 46, 12, 24]
#     correct_mean = 30.5
#     assert(mean(n_list) == correct_mean)

#     print("Testing add_five function")
#     correct_list = [39, 49, 28, 51, 17, 29]
#     assert(add_five(n_list) == correct_list)

#     print("All tests passed!")

# if __name__ == '__main__':
#     main()

# Techniques for Improting module
# Techniques for Importing Modules
# There are other variants of import statements that are useful in different situations.

# To import an individual function or class from a module:
# from module_name import object_name
# To import multiple individual objects from a module:
# from module_name import first_object, second_object
# To rename a module:
# import module_name as new_name
# To import an object from a module and rename it:
# from module_name import object_name as new_name
# To import every object individually from a module (DO NOT DO THIS):
# from module_name import *
#     ```
#     6. If you really want to use all of the objects from a module, use the standard import module_name statement instead and access each of the objects with the dot notation.
#     ```python
# import module_name

# Third-Party Libraries
# There are tens of thousands of third-party libraries written by independent developers! You can install them using pip, a package manager that is included with Python 3. pip is the standard package manager for Python, but it isn't the only one. One popular alternative is Anaconda which is designed specifically for data science.

# To install a package using pip, just enter "pip install" followed by the name of the package in your command line like this: pip install package_name. This downloads and installs the package so that it's available to import in your programs. Once installed, you can import third-party packages using the same syntax used to import from the standard library.

# Using a requirements.txt File
# Larger Python programs might depend on dozens of third party packages. To make it easier to share these programs, programmers often list a project's dependencies in a file called requirements.txt. This is an example of a requirements.txt file.

# beautifulsoup4==4.5.1
# bs4==0.0.1
# pytz==2016.7
# requests==2.11.1
# Each line of the file includes the name of a package and its version number. The version number is optional, but it usually should be included. Libraries can change subtly, or dramatically, between versions, so it's important to use the same library versions that the program's author used when they wrote the program.

# You can use pip to install all of a project's dependencies at once by typing pip install -r requirements.txt in your command line.



# def create_cast_list(filename):
#     cast_list = []
#     with open(filename) as f:
#         for line in f:
#             name = line.split(",")[0]
#             cast_list.append(name)
#
#     return cast_list
#
#
# cast_list = create_cast_list('flying_circus_cast.txt')
# for actor in cast_list:
#     print(apoctor)