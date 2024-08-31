# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

m = int(input("Enter math marks(out of 100) : "))
p = int(input("Enter physics marks(out of 100) : "))
c = int(input("Enter chemistry marks(out of 100) : "))

total = ((m + p + c) / 300) * 100

if m >= 33 and c >= 33 and p >= 33 and total >= 40:
    print("student passed")
else:
    print("Student failed")
