x=int(input("enter the upper bound of the elements:"))
y=int(input("enter the lower bound of the elements:"))
z=[i for i in range(x,y+1) if(int((i)**.5))**2==i]
print ("the perfect sq number in the mentioned range is:",z)
