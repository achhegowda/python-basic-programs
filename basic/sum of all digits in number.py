n=int(input("enter the number:"))
res=0
while(n!=0):
    d=n%10
    res=res+d
    n=n//10
print ("sum of the digits is:",res)    
