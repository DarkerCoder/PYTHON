import random

'''
1 - Snake
2 - Water
3 - Gun
'''
comp = random.choice(range(1,4))
my = int(input("1 - Snake\n2 - Water\n3 - Gun\nEnter your choice: "))
dict = {1: "Snake", 2: "Water", 3: "Gun"}

print(f'You chose {dict[my]}\nComputer Chose {dict[comp]}')

if(comp == my):
    print("Draw")
else:
    if((comp == 1 and my == 3) or (comp == 3 and my == 2) or (comp == 2 and my == 1)):
        print("You Win!!!!")
    else:
        print("Computer Win!!!!")        
