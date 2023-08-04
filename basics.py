#Changing Data Type
print(float(2))
print(int(1.1))
print(int("99"))
print(str(90))

#to check the Data Type
print(type("gokul"))

#string : stride
name = "Gokulapriyan"
print(name[::2]) # slicing by two indeces
print(name[0:8:2]) #start value, end value and step value

# string: Slicing
print(name[0:6])

# Multiplying the Variable
print(3 * name)


# String Concatentation
print(name + " is a Python Developer")


#Escape Sequences

print("gokul \n is the best student") # new line
print("gokul \t is the best student") # tab where the backslash
print("gokul \\ is the best student ")# The Result is Backslash after escape sequence.

# string Methods
a = "gokul"
print(a.upper()) #Python String upper() method converts all lowercase characters in a string into uppercase characters and returns it.

b = "Gokul is the best"
print(b.replace("Gokul","gokulapriyan")) # The replace() method returns a copy of the string where the old substring is replaced with the new string. The original string remains unchanged. If the old substring is not found, it returns a copy of the original string.

#find() function is a part of python library. find() takes a string as input. It is used to find the index of the first occurrence of the substring inside a given string.
print(name.find("k")) # Note If the character is not in string output will be -1


#Tuples()
"""A tuple is an immutable object, which means it cannot be changed, 
and we use it to represent fixed collections of items."""

# Adding The Two Tuples.
tuple1 = ("disco",10,1.2)
tuple2 = tuple1 + ("hardRock",10)
print(tuple2)

#Tuple Slicing
print(tuple2[0:3])

#Tuples Nesting

nestedTuples = (1,2,("pop"),(3,4))
print(nestedTuples[2],nestedTuples[0],nestedTuples[-1])

#lists
""" A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements.
 Each element or value that is inside of a list is called an item. Just as strings are defined as characters between quotes,
 lists are defined by having values between square brackets [ ]."""

# To clone or make a copy of List using[:]  List[:].
A = ["gokul",10,1.2]
B = A[:]
print(B)

#Convert string to List
print("hardrock".split())
print("gokul peace".split())


#Dictionary
#Note: The keys Have to be Immutable and Unique.
"""Dictionaries are Python's implementation of a data structure that is more generally known as an associative array.
 A dictionary consists of a collection of key-value pairs. Each key-value pair maps the key to its associated value."""

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict.values()) # To get all the Values in Dictionaries.

#The del keyword is used to delete objects.
# In Python everything is an object, so the del keyword can also be used to delete variables,
# lists, or parts of a list
del(thisdict['brand'])
print(thisdict)

print(thisdict.keys()) # To get all the Keys in Dictionaries.
