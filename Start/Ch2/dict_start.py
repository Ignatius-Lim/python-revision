# LinkedIn Learning Python course by Joe Marini
# Example file for complex types


# Dictionary: a key-value data structure
mydict = {
  "one" : 1,
  "two" : 2,
  3 : "three",
  4.5 : ["four", "point", "five"]
}

# print(mydict)

# dictionaries are accessed via keys
# print(mydict["one"])
# print(mydict[3])


# you can also set dictionary data by creating a new key
mydict["seven"] = 7
# print(mydict)

# Trying to access a nonexistent key will produce an error
# print(mydict["nick"])


# To avoid this, you can use the "in" operator to see if a key exists
# print("two" in mydict)
# print("nick" in mydict)


# You can retrieve all of the keys and values from a dictionary
# print(mydict.keys())
# print(mydict.values())
# Although they are of the dictionary type, but the above two behaves like a List
# When print is used, they look like a List. You can also index them.


# You can also iterate over all the items in a dictionary
for key, val in mydict.items(): #The output values are tuples, each tuple containing two items.
  print(key, val)
