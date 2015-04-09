#Antonio Yosefat Juárez Quintero A01228128
def calculate_e(prescision):
	sum = 1
	x=0
	y=0
	z=1
	while (x<precision):
		x=x+1
		y=1/(x*z)
		sum = sum+y
		z=x*z
	return sum

precision = int(input("How many decimal points do you want? "))
print ("The value of e with",precision,"decimal points is:",calculate_e(precision))
