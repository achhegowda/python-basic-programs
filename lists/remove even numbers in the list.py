n=int(input("enter the number of elements;"))
a=[]
for i in range(0,n):
    x=int(input("enter the number"))
    a.append(x)
    l=[]
for i in a:
    if i%2==0:
        l.append(i)
s1=set(a)
s2=set(l)
f=s1-s2
k=list(f)
print("list with out evwn numbers",f)    
