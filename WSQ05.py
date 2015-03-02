#Antonio Yosefat Juárez Quintero A01228128
#In this program I will ask the user for a value in fahrenheit and then I will convert it to Celcious, finally, I determinated if it would boil or not

f = int(input("Give me the temperature in Fahrenheit: ")) #The input for the Fahrenheit
print() #A simple space
c = 5 * (f - 32)/9 #The formula of the celcious convertion
print ("The temperature in Celcious is: ", c)
print () #The same as the previous
if(c >= 100): #The condition for the if
	print("Water boil at this temperature(Under typical conditions)")#The output if the condition is true
#Note: Identation is important in order to make the if work
else: #Else... I is like taking all the values that doesn't enter in the if, like another condition.
	print("Water doesn't boil at this temperature (Under typical conditions)")#The output for this condition

#Done
