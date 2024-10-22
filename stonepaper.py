#STONE  PAPER SCISSOR
import random
computer =  random.choice([-1,1,0])
youstr  = input("Enter your choice :")
youDict = {"stone":1,"paper":-1,"scissor":0}
reverseDict = {1:"stone",-1:"paper",0:"scissor"}
you = youDict[youstr]

print(f"you choose {reverseDict[you]}\n Computer choose {reverseDict[computer]}")

if(computer == you):
    print("It's a tie!")
    
else: 

    if(computer == -1 and you== 1):
        print("You Win")
        
    elif(computer == -1 and you == 0):
        print("you lose")
        
    elif(computer == 1 and you== -1):
        print("You lose")
        
    elif(computer == 1 and you == 0):
        print("you win")
        
    elif(computer == 0 and you== -1):
        print("You lose")
        
    elif(computer == 0 and you == 1):
        print("you win")
    else:
        print("Something went wrong")