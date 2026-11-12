# LinkedIn Learning Python course by Joe Marini
# Example file for complex types

# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values
mylist = [0, 1, "two", 3.14, True]
#print(len(mylist))  # Lists can contain values of different types

# to access a member of a sequence type, use []
# print(mylist[2])  # this will print "two"
# print(mylist[-1])  # this will print True, the last element in the list
# mylist[0] = 10  # this will change the first element to 10
# print(mylist)

# add a list to another list
# another_list = [4, 5, 6]
# mylist = mylist + another_list
# print(mylist)

# mystr = "This is a string"
# print(mystr[6])  # this will print "s"


# use slices to get parts of a sequence
#print(mylist[1:4:2])  # this will print [1, "two", 3.14]

# you can use slices to reverse a sequence
#print(mylist[::-1])  # this will print [True, 3.14, "two", 1, 0]


# Tuples are like lists, but they are immutable
mytuple = (0, 1, "two", 3.14, True)
# print(mytuple[2])  # this will print "two"
# print(mytuple[-1])  # this will print True, the last element in the tuple



# Sets are also sequences, but they contain unique values
myset = {0, 1, "two", 3.14, True, 2,3.14}
#print(myset)  # this will print the set, but the order of the elements may be different each time you run the program

# Set, however, can not be indexed like lists or tuples
#print(myset[0]) # this will cause an error

# Test for membership
print(1 in myset)  # this will print True
print(2 in mytuple)  # this will print False, because 2 is not in the tuple
print(3 in mylist)  # this will print False, because 3 is not in the list  
