n=int(input("enter the number of elements in list 1;"))
a=[]
for i in range(0,n):
    x=int(input("enter the number"))
    a.append(x)
m=int(input("enter the number of elements in list 2:"))
b=[]
for k in range(0,m):
    y=int(input("enter the number"))
    b.append(y)
z=a+b

print("new merged list:",z)
z.sort()
print ("sorted new list:",z)
