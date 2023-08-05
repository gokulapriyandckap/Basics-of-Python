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


#sets
"""Set is an unordered collection of datatypes that is iterable, mutable and has no duplicate elements.
The order of elements in a set is undefined though it may consist of various elements."""

#Important Points of Sets.
# 1. Lists and Tuples are unorders.
# This means sets do not record element position.
# 2. Set only have unique elements and set did not have duplicate elements.

set1= {"Pop","rock","soul","rock"}
print(set1) # It will be return unique values only.

album_list = ["gokul","ganesh","gokul",2004]
album_set = set(album_list) # To convert set.
print(album_set) # It'll also  return unique values only after converting into set.

# Set Operations.
setA = {"python","Java","R"}
setA.add("PHP") #The add() method adds an element to the set. If the element already exists, the add() method does not add the element.
print(setA)
print("PHP" in setA) #The in keyword is used to check if a value is present in a sequence (list, range, string etc.).

setA.remove("R") # The remove() method removes the first matching element (which is passed as an argument) from the li
print(setA)

C = {"Gokul","Ganesh","sandhya"}
D = {"Deepak","Gokul","Vignesh"}
e = C & D # Check the same elements in the two sets
print(e)

# The issubset() method returns True if all items in the set exists in the specified set, otherwise it returns False.
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)

#Range.
# syntax of range is range(start, stop, step).
# eg: range(3) = [0,1,2]. range(10,15) = [10,11,12,13,14].
for i in range(0,100,2):
  print(i)
for i in range(1,10):
  print(i)

# for
# The for loop in Python is an iterating function.
# If you have a sequence object like a list, you can use the for loop to iterate over the items contained within the list

square = ["red","pink","blue","black"]

for i in square:
  print(i)

# Functions
# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

def add(a):
  b = a +1
  print (b)

add(99)

def mul(a,b):
  print(a *b)

mul(1000,87)


def print_stuff(stuff):
  for i,s in enumerate(stuff):
    print('Album',i,"Rating is ",s)

album_rating = [10,8.5,9.5]
print_stuff(album_rating)

#collecting Arguments.
def artistNames(*names):
  for x in names:
    print(x)
artistNames("Anirudh","G.v","A.R.R","Sana")


# Pass
#whereas pass means, “there is no code to execute here,”
#pass tells Python to skip this line and do nothing.
# it will continue through the remainder of the  body.
def nowork():
  pass

nowork()

# Built-in Functions.
# Python Have Built-in Functions.
 #len()->function returns the number of characters in the string.
mylist = ["apple", "banana", "cherry"]
print(len(mylist))

#sum()-> function returns a number, the sum of all items in an iterable.
a = (1, 2, 3, 4, 5)
print(sum(a))


#sorted()->  function returns a sorted list of the specified iterable object.
#syntax -> sorted(iterable, key=key, reverse=reverse)
a = ("b", "g", "a", "d", "f", "c", "h", "e")
x = sorted(a)
print(x)

#reverse sorted()
a = ("h", "b", "a", "c", "f", "d", "e", "g")
x = sorted(a, reverse=True)
print(x)


#if else with Comparison Operators.
a = 10
b = 90
if(a > b):
  print("a is greater than b")
elif(a == b):
  print("a is equal to b")
else:
  print("a is smaller than b")


#exception Handling with file Handling
try:
  with open("sample.txt", "w") as getfile:
    getfile.write("""Often, programmers fall in love with Python because of the increased productivity it provides. Since there is no compilation step, the edit-test-debug cycle is incredibly fast. Debugging Python programs is easy: a bug or bad input will never cause a segmentation fault. Instead, when the interpreter discovers an error, it raises an exception. When the program doesn't catch the exception, the interpreter prints a stack trace. A source level debugger allows inspection of local and global variables, evaluation of arbitrary expressions, setting breakpoints, stepping through the code a line at a time, and so on. The debugger is written in Python itself, testifying to Python's introspective power. On the other hand, often the quickest way to debug a program is to add a few print statements to the source: the fast edit-test-debug cycle makes this simple approach very effective.""")
  with open("sample.txt", "r") as file1:
    print(file1.read())
    file1.close()
  # Readlines()-> method returns a list containing each line in the file as a list item.
  with open("sample.txt","r") as file1:
    print(file1.readlines())

except:
  print("unable to open or read the data in the file")

else:
  print("The file written succesfully")

finally:
  getfile.close()
  print("file is now closed")



