""" This code uses for loops to print pattern which we can call a doormat pattern
    code is divided in two parts part 1 refers to portion of pattern above welcome line
    code is divided in two parts part 2 refers to portion of pattern below welcome line
    """

a=input().split(' ')
# code below will print PART-1
b=1
for i in range(1,int(a[1])):
    if(b<=int(a[0])//2):

        #loop below will print special character "-" in line

        for j in range((int(a[1])//2)-(1+3*(i-1))):
                print("-",end="")  

        # loop below will print special character ".|." in line

        for k in range(1,i+1):
            print(".|.",end="")
        for k in range(1,i):
            print(".|.",end="")

        # loop below will print special character "-" in line after ".|." this character 

        for j in range((int(a[1])//2)-(1+3*(i-1))):
                print("-",end="")
        print("")
    else:
        break
       
    b+=1
    
# code below will print welcome line
print("-"*((int(a[1])-7)//2),end='')
print("welcome",end='')
print("-"*((int(a[1])-7)//2),end='')
print('')
# code below will print PART-2
c=1
x=int(a[0])//2
for i in range(1,int(a[1])):
    if(c<=int(a[0])//2):

        #loop below will print special character "-" in line

        for j in range((int(a[1])//2)-(1+3*(x-1))):
                print("-",end="")

        # loop below will print special character ".|." in line 

        for k in range(1,x):
            print(".|.",end="")
        for k in range(x):
            print(".|.",end="")

        # loop below will print special character "-" in line after ".|." this character

        for j in range((int(a[1])//2)-(1+3*(x-1))):
                print("-",end="")
        print("")
        x-=1  
    else:
        break   
    c+=1

            
    