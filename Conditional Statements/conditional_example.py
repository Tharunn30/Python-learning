# Grade students based on marks.

# Marks >= 90, Grade= A
# 90 > marks >= 80, Grade= B
# 80 > marks >= 70, Grade= c
# 70 > marks, Grade = D

marks = int(input("Enter the marks: "))
if marks >= 90:
    grade = "A"
elif(marks >= 80 and marks< 90):
    grade = "B"
elif(marks >= 70 and marks< 80):
    grade = "C"
else:
    grade = "D"

print("Grade of the student is: ",grade)
