x=int(input("enter the lower bound for number of tuples in list:"))
y=int(input("enter the upper bound for number of tuples in list:"))
z=[(x,x**2) for x in range(x,y+1)]
print("the list which contain tuple(num,num**2):",z)
