# It is a built in data type that let us create immutable sequences of value
# It is a collection which is ordered and indexed

tup = (2,1,3,4)
print(type(tup)) # Output: <class 'tuple'>
print(tup[0]) # Output: 2
# We can't change the value of a tuple, it is immutable
tup[0] = 2

#how to make it tuple
tup = (5)
print(type(tup)) # Output: <class 'int'>
# To make it a tuple we need to add comma after the value
tup = (5,)
print(type(tup)) # Output: <class 'tuple'>

