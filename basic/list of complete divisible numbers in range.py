a=int(input("enter the lower bound:"))
b=int(input("enter the upper bound:"))
n=int(input("enter the number to be divide:"))
c=0
for i in range(a,b+1):
    if(i%n)==0:
        print (i)
        c+=1
print (c)        
