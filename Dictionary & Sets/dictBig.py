# Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.

lang = {}

f1 = input("Enter 1st friend Name: ")
l1 = input("Enter 1st friend language: ")
lang[f1] = l1

f2 = input("Enter 2nd friend Name: ")
l2 = input("Enter 2nd friend language: ")
lang.update({f2: l2})

f3 = input("Enter 3rd friend Name: ")
l3 = input("Enter 3rd friend language: ")
lang[f3] = l3

f4 = input("Enter 4th friend Name: ")
l4 = input("Enter 4th friend language: ")
lang[f4] = l4

print(lang)
