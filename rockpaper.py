import random
n=0
score=0
total=0
while(n!=1):
    # print("rock as 1 ,paper as 2 ,scissor as 3")
    a=random.randint(1,3)
    b=input("enter your choice = ")
    total+=1
    if(a==1):
        if(b=="rock" or b=="Rock"):
            print("you win :)")
            score+=1
            print("your current score is ",score)
        else:
            print("you lose :(")
            print("your current score is ",score)
    elif(a==2):
        if(b=="paper" or b=="Paper"):
            print("you win :)")
            score+=1
            print("your current score is ",score)
        else:
            print("you lose :(")
            print("your current score is ",score)
    elif(a==3):
        if(b=="scissor" or b=="Scissor"):
            print("you win :)")
            score+=1
            print("your current score is ",score)
        else:
            print("you lose :(")
            print("your current score is ",score)
    
    else:
        print(" Please enter valid values only")
    print("Press any key for continue otherwise press '1' for exit ")
    n=int(input())
print("your total score is ",score)
if(score>(total//2)):
    print("Well played")
elif(score<(total//2)):
    print("better luck next time :)")
else:
    print("your are a pro player in this game but this game will not earn money for you but you can earn through creating this type of game . :))")

