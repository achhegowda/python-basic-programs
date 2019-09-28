f=0
s=1
n=int(input("enter the lenth of fib series:"))
for k in range(n):
    print(f,end=" ")
    t=f
    f=s
    s=f+t
    
    
