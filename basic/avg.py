n=int(input("enter the number of elements to be inserted:"))
#it is based on list
#this program under version control
a=[]
for i in range(n):
    ele=int(input("enter the element:"))
    a.append(ele)
avg=sum(a)/n
print("avg of numbers is:",round(avg,3))
    
