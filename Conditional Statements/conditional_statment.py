age = int(input("Enter your age: "))

#if 
if(age >= 18):
    print("You are eligbile for license")
else:
    print("You are child")

#elif (else if)
light = "green"

if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("Go slowly")

#Difference between if and elif is, if statement checks the conditon. Elif checks when the if statement is false
num = 5
if(num > 2):
    print("greater than 2")
elif(num < 2):
    print("number is lesser than 2")


#else has no condition
light = "White"

if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("Go slowly")
else:
    print("Light is broken")




