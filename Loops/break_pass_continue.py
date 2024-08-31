for i in range(0, 40, 2):
    if i == 16:
        break  # exit the loop
    print(i)

j = 0
print("While loop")
while j < 16:
    if j == 8:
        j += 1  # Increment j after continue
        continue  # Skip the number 8
    print(j)
    j += 1

for i in range(4):
    pass # skip this loop for now

k = 24
print("Pass while")
while k < 100:
    if k == 99:
        break
    print(k+4)
    k = k + 4
