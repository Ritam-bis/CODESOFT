import random
'''
rock=r 
paper=p
scissors=s
'''
choices = ['r', 'p', 's']
computer = random.choice(choices)

yourint = input("ENTER YOUR CHOICE (r for Rock, p for Paper, s for Scissors): ").lower()

mydic = {'r': 'ROCK', 'p': 'PAPER', 's': 'SCISSORS'}

if yourint in mydic:   # check valid input
    you = mydic[yourint]
    comp = mydic[computer]
    print(f"YOUR CHOICE: {you}\nCOMPUTER'S CHOICE: {comp}")
else:
    print("❌ Invalid input! Please enter r, p, or s.")

if(computer==yourint):
    print("ITS A DRAW !!")
else:
    if(computer=="r" and yourint=="p"):
        print("YOU WIN!!")
    elif(computer=="r" and yourint=="s"):
        print("YOU LOSE")
    elif(computer=="p" and yourint=="s"):
        print("YOU WIN !!")
    elif(computer=="p" and yourint=="r"):
        print("YOU LOSE !!")
    elif(computer=="s" and yourint=="p"):
        print("YOU LOSE !!")
    elif(computer=="s" and yourint=="r"):
        print("YOU WIN !!")
    else:
        print("SOMETHING WENT WRONG")    