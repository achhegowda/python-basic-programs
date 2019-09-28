def fun(n):
	f=0
	s=1
	for k in range(n):
		print(f)
		t=f
		f=s
		s=f+t
ask=input("are here for fib series(yes/no):")
if ask=="yes":
    k=int(input("enter the length of fib series:"))
    fun(k)

else:
    print("thank you")
