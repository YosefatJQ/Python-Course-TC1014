#Antonio Yosefat Juárez Quintero A01228128
print ("Give me a list.")
x=int(input("Give me the lenght of the list."))
lista = []
for i in range(x):
	lista.append(0)
n=0
suma=0
while (n<x):
	print ("\nGive me the ",n+1," number.")
	lista[n] = int(input())
	n=n+1
n=0
while(n<x):
	if(lista[n]%3==0):
		suma=suma+lista[n]
	n=n+1
print("\nThe sum of the values are: ",suma)
