# LinkedIn Learning Python course by Joe Marini
# Example file for complex types

# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values
mylist = [0, 1, "two", 3.2, False]
# print(len(mylist))
print(mylist)

# to access a member of a sequence type, use []
# print(mylist[2])
# print(mylist[-1])
# mylist[0] = 10
# print(mylist[0])

# add a list to another list
# another_list = [6, 7, 8]
# mylist = mylist + another_list
# print(mylist)

mystr = "This is a string"
print(mystr)
# String is also a sequence, but it is immutable.

# use slices to get parts of a sequence
# print(mylist[1:4:2]) # First value is start, second is end but not inclusive, last is step amt
# print(mylist[-3::2]) # Slice values are optional. You can leave out up to 2 of them
# The use of negative number means it starts from behind

# you can use slices to reverse a sequence
# print(mylist[::-1]) # Using a negative step amount causes a reverse (applies to string too)

# str_temp = "car"
# print(str_temp[::-1])


# Tuples are like lists, but they are immutable (similar to string)
mytuple = (0 ,1, 2, "three")
print(mytuple)


# Sets are also sequences, but they only contain unique values (non repeating)
myset = {1, 2, 3, 2, 4, "hey"}
print(myset)

# Set, however, can not be indexed like lists or tuples
# print(myset[0]) # this will cause an error

# Test for membership - To check if a value exists in a sequence
print(1 in mylist)
print(3 in mytuple)
print(5 in myset)
