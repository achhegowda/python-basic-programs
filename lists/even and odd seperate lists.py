n=int(input("enter the number of elements;"))
a=[]
for i in range(0,n):
    x=int(input("enter the number"))
    a.append(x)
e=[]
o=[]
for i in a:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
print("even list:",e)
print("odd list:",o)
