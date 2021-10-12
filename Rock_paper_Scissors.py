import random

def gameWin(comp,you):

    if comp == you:
        return None

    elif comp == 'r':
        if you == 'p':
            return True
        elif you == 's':
            return False

    elif comp == 'p':
        if you == 's':
            return True
        elif you == 'r':
            return False            

    elif comp == 's':
        if you == 'p':
            return False
        elif you == 'r':
            return True


print("Computer's turn: Rock(r), Paper(p), Scissors(s)")

randNo = random.randint(1,3)

if randNo == 1:
    comp = 'r' 
elif randNo == 2:
    comp = 'p'    
elif randNo == 3:
    comp = 's'

you = input("Your turn - Rock(r), Paper(p), Scissors(s): ") 
a = gameWin(comp,you) 

print(f"Computer chose {comp}")
print(f"You chose {you}")
 

if a == None:
    print("Its a tie")
elif a == True:
    print("You win!")
else:
    print("Computer wins!")        