# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect this spams

p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

msg = input("Enter your message: ")

if p1 in msg or p2 in msg or p3 in msg or p4 in msg:
    print("Spam Detected")
else:
    print("Spam not detected")