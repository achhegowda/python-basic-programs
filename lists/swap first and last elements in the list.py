n=int(input("enter the number of elements in the list"))
l=[]
for i in range(0,n):
    x=int(input("enter the number"+str(i+1)+":"))
    l.append(x)
print("original list:",l)
t=l[0]
l[0]=l[n-1]
l[n-1]=t

print("the swaped list is:",l)
    

