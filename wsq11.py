def palindromo(i):
	i=str(i)
	i=i[::-1]
	i=int(i)
	return i
lower = int(input("Give me the Lower Bound: "))
upper = int(input("Give me the Upper Bound: "))
x=[]
p=0
n=0
c=0
l=0
for h in range(upper-lower+1):
	x.append(l)
	l=l+1
if(upper<lower):
	print("The values are incorect.")
else:
	for i in x:
		i=i+1
		x=palindromo(i)
		if (x==i):
			p=p+1
		else:
			non1=x+i
			non2=palindromo(non1)
			for z in range(30):
				if non1 == non2:
					n=n+1
					break
				else:
					non1=non1+non2
					non2=palindromo(non1)
				if(z==29):
					c=c+1
	print("The range is from",lower,"to",upper,".")
	print("The number of Palindromes are: ",p)
	print("The number of Non-Lychrel numbers are: ",n)
	print("The number of Lychrel candidates are: ",c)
