#Nested Dictionary : It means making a dictionary inside a dictionary.

student = {
    "name" : " Tharunn Raj",
    "subjects" : { #new dictionary
        "Maths" : 90,
        "Science" : 85,
        "social " : 99,
    }
}

print(student)
print(student["subjects"["Maths"]]) #for printing nested dictionary


