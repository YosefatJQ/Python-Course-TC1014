#Antonio Yosefat Juárez Quintero A01228128
ans = 'y'
while(ans=='y' or ans == 'Y'):
	print("This program is to display the factorial value from the number given.\n")
	fac = int(input("Please give me the number you want to know the factorial."))
	if (fac > 0):
		x = fac 
		while (x > 1):
			x = x-1
			fac = fac * x
		print (fac)
	else:
		print("The factorial of a negative number doesn't exist.")
	ans = input("Do you want to repeat?(Press anything else if you want to exit)\n")
