
# Enter your code here. Read input from STDIN. Print output to STDOUT

a=input().split(' ')
b=1
for i in range(1,int(a[1])):
    if(b<=int(a[0])//2):
    
        for j in range((int(a[1])//2)-(1+3*(i-1))):
            
                
                print("-",end="")
                
        
        for k in range(1,i+1):
            print(".|.",end="")
        for k in range(1,i):
            print(".|.",end="")
                
        

        for j in range((int(a[1])//2)-(1+3*(i-1))):
            
                
                print("-",end="")
        print("")
    else:
        break
       
    b+=1
print("-"*((int(a[1])-7)//2),end='')
print("welcome",end='')
print("-"*((int(a[1])-7)//2),end='')
print('')
c=1
x=int(a[0])//2
for i in range(1,int(a[1])):
    if(c<=int(a[0])//2):
    
        for j in range((int(a[1])//2)-(1+3*(x-1))):
            
                
                print("-",end="")
        for k in range(1,x):
            print(".|.",end="")
       
        for k in range(x):
            print(".|.",end="")
        for j in range((int(a[1])//2)-(1+3*(x-1))):
            
                
                print("-",end="")
        print("")

        x-=1  
    else:
        break
       
    c+=1

            
    