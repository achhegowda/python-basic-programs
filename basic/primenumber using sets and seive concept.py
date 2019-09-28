n=int(input("enter the upper bound of the number:"))
s=set(range(2,n+1))
while s:
    prime=min(s)
    print(prime,end=" ")
    s-=set(range(prime,n+1,prime))
    
