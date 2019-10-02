n=int(input("enter the number of elements in the list:"))
l=[]
for i in range(0,n):
    x=str(input("enter the element:" + str(i+1) +":"))
    l.append(x)
l.sort(key=len)
print("the sorted list is:",l)
