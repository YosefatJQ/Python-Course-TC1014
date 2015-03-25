#Antonio Yosefat Juárez Quintero A01228128
def triangle(size,n):
	
	while (n<size):
		n=n+1
		print("T"*n)
	n=size
	while (n>0):
		n=n-1
		print("T"*n)
n=0
size=int(input("Give me the size of the triangle: "))
triangle(size,n)
