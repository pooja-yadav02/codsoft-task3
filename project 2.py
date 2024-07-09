print(" welcome to my new game :-")
import random
def gamewin(computer,your_choice):
    if computer == your_choice:
        return None
    elif computer=="r":
        if your_choice=="s":
            return False
        elif your_choice=="p":
            return True
    elif computer=="p":
        if your_choice=="r":
            return False
        elif your_choice=="s":
            return True
    elif computer=="s":
        if your_choice=="p":
            return False
        elif your_choice=="r":
            return True     
print("computer Turn: rock(r),paper(p),scissor(s) ?")
randNo=random.randint(1,3)

if randNo==1:
    computer="r"
elif randNo==2:
    computer="p"
elif randNo==3:
    computer="s"
        
your_choice=input("Your turn: rock(R),paper(P),scissor(s)")
a=gamewin(computer,your_choice)

print(f"computer choose {computer} ")
print (f"your_choose {your_choice} ")
if a==None:
    print(" The game is tie..! ")
elif a:
    print(" you win")
    
else:
    print(" you lose...!")

