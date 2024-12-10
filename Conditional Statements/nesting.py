#Writing another if statement inside if statement

age = 34

if(age >= 18):
    #lets imagine that max age for driving is 80
    if(age >= 80):
        print("cant drive")
    else:    
        print("Can drive")
else:
    print("Cant drive")
