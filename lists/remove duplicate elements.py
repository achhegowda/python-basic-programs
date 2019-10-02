n=int(input("enter the number of elements in the list:"))
q=[]
for i in range(0,n):
    x=int(input("enter number" + str(i+1) + ":"))
    q.append(x)
s=set()
for i in q:
    s.add(i)
print(list(s))    
