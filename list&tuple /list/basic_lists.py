# List: It is a built in data type that stores set of values.
# It can store elements of different types (integers, float, strings etc)

# marks1 = 95.2
# marks2 = 91.1
# marks3 = 96.9
# marks4 = 64.5
# marks5 = 49.9

# the above method is traditional but not useful for huge data, its great for very limited data

#the list method is very good and less time consuming

marks = [95.2, 91.1, 96.9, 64.5, 49.9]
print(marks) # output: [95.2, 91.1, 96.9, 64
print(type(marks)) # output: <class 'list'>

print(len(marks))
print(marks[0])
print(marks[1])

#We can add multiple type of data in single list.

student = ["Tharunn", 91, 21, "SRM"]
print(student) # output: ['Tharunn', 91, 21, 'SRM

#Note: Strings are immutatble and lists are mutable. 

string = "Hello"
# string[0] = "J" # this will throw an error

student[0]= "Raj"
print(student[0]) # output: Raj

#Slicing
#Slicing is a way to extract a subset of data from a list.

# format: list_name[starting_index : ending index]

marks = [95.2, 91.1, 96.9, 64.5, 49.9]
print(marks[1:4]) # output: [91.1, 96.9, 64.5]
print(marks[:5])# output: [95.2, 91.1, 96.9, 64]
print(marks[-4]) # output: [95.2, 91.1, 96.9, 64]
