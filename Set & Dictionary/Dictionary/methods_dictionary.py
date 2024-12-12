student = {
    "name" : "Tharunn Raj",
    "subjects" : { #new dictionary
        "Maths" : 90,
        "Science" : 85,
        "social " : 99,
    }
}

# #1 mydict.keys() : It returns all keys
print(student.keys())

# #2 mydict.values() : It returns all values
print(student.values())

#3 mydict.items() : It returns all (key,val) paris as tuple
# print(student.items())
pairs = list(student.items())
print(pairs[0])

#4. mydict.get("key") : It returns the key according to value
#Its better to use .get always so that it avoids the error. The error wont even let you get past the error even if the code is right
print(student["name2"]) #error
print(student.get["name2"]) #no error -> None

#5. mydict.update(newDict) : It inserts the specified items to the dictionary
#It updates and creates new key. It over writes the value. 
new_dict = ({"city" : "Chennai"})
student.update(new_dict)
print(student)

