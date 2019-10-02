n=int(input("enter the number of elements;"))
a=[]
for i in range(0,n):
    x=int(input("enter the number"))
    a.append(x)
k=[i for i in a if i%2!=0]
print("the list with out even number:",k)
