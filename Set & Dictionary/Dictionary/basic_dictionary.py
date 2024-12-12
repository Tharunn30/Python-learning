#Dictionaries are used to store data values in key:value pairs
#Dictionaries are mutable, meaning that they can be modified after creation
#Dictionaries are unordered, meaning that the order of the key-value pairs does not matter
#Dictionaries are dynamic, meaning that they can grow or shrink as items are added or removed
#Properties : They are unordered, mutable(changeable) and dont allow duplicate keys

info = {
    "name": "Tharunn",
    "cgpa" : "8.21", 
    "College" : "SRM",
    "age" : 21,
    "is_adult" : True,
    "is_student" : False,
    "subjects" : ["Python","DSA","OOPS"],
    "topics" : ("dict","set")
}

#How to access the dict?
#Accessing a dictionary is similar to accessing a list or a string, but you use the key
print(info["name"])
print(info["topics"])
print(info["age"])

#How to change data in dict?
#You can change the data in a dictionary by assigning a new value to a key

info["name"] = "P.V. Tharunn" #overwrite
info["surname"] = "Raj" #creating new in dict
print(info)


#We can also make empty dict

null_dict = {}
print(null_dict) #{}
#We can also make dict with some values
null_dict["name"] = "John"