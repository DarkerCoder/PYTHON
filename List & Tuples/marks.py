# Write a program to accept marks of 6 students and display them in a sorted manner.

marks = []

m1 = int(input('Enter 1st student marks: '))
marks.append(m1)
m2 = int(input('Enter 2nd student marks: '))
marks.append(m2)
m3 = int(input('Enter 3rd student marks: '))
marks.append(m3)
m4 = int(input('Enter 4th student marks: '))
marks.append(m4)
m5 = int(input('Enter 5th student marks: '))
marks.append(m5)
m6 = int(input('Enter 6th student marks: '))
marks.append(m6)

marks.sort()
print(marks)