def total(l):
	x=0
	sum = 0
	while(x<10):
		sum = sum + l[x]
		x=x+1
	return sum
def promedio(t):
	promedio = t/10
	return promedio 
def standarddeviation(l, p):
	x=0
	sum = 0
	while(x<10):
		s = (l[x]-p)**(2.0)
		sum = sum+s
		x=x+1
	s = (sum/9)**(.5)
	return s
x=0
l=[]
print("This is a list of 10 numbers.")
while (x<10):
	num = int(input("Give me the a number: "))
	l.append(num)
	x=x+1
t=total(l)
p=promedio(t)
print("\nList: ",l)
print("\nTotal: ",total(l))
print("\nPromedio: ",promedio(t))
print("\nStandard Deviation: ",standarddeviation(l, p))
