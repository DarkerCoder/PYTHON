# Write a program to calculate the grade of a student from his marks from the
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

marks = int(input("Enter your marks: "))

if 100 >= marks >= 90:
    grade = "ex"
elif 90 >= marks >= 80:
    grade = "A"
elif 80 >= marks >= 70:
    grade = "B"
elif 70 >= marks >= 60:
    grade = "C"
elif 60 >= marks >= 50:
    grade = "D"
else:
    grade = "F"

print(f"Grade : {grade}")
