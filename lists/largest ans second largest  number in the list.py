n=int(input("enter the number of elements;"))
a=[]
for i in range(0,n):
    x=int(input("enter the number"))
    a.append(x)
a.sort()
print("the largest number is:",a[-1])
print("the second largest number is:",a[-2])
