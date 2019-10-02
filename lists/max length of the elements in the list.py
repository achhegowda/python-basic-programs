n=int(input("enter the number of elements:"))
q=[]
for i in range(0,n):
    x=(input("enter number " +  str(i+1) + ":"))
    q.append(x)
max1=q[0]
for i in q:
    if i>q[0]:
        t=i
        max1=t
print("max length string is:",len(max1))
        
    
