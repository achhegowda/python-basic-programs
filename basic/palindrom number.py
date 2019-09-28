n=int(input("enter the number:"))
rev=0
t=n
while(n!=0):
    d=n%10
    rev=rev*10+d
    n=n//10
if t==rev:
    print ("number is palindrom")
else:
    print("number is not palindrome")
