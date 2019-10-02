n=int(input("enter the number of elements:"))
q=[]
for i in range(0,n):
    x=int(input("enter number " +  str(i+1) + ":"))
    q.append(x)
z=[sum (q[0:k+1])for k in range(0,len(q))]
print (q,"is original list")
print (z,"is cumulatively added lists")


