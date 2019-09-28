n=int(input("enter the number"))

for i in range(1,n+1):
    l=[]
    for j in range(1,i+1):
        print(j,sep=" ",end=" ")
        if i>j:
            print("+",sep=" ",end=" ")
        l.append(j)
    print("= ",sum(l))            
print()
