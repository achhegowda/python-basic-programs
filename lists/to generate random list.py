import random
l=[]
x=int(input("enter the count of random number to be displayed:"))
for i in range(0,x):
    r=random.randint(0,100)
    l.append(r)
print("the random numbers are:",l)    
    
