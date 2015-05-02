import statistics

def readNumbersFromFile(x):
	y = open(x, "r")
	l = []
	a = 0
	b = 0
	c = 0
	sum = 0
	for line in y:
		sum=sum+(int(line))
		l.append(int(line))
		val = len(l)
		prom = sum/val
		while(z<value):
			a = ((l[b])- prom) ** 2
			b = b+1
			c = c+a
			sd = math.squirt(c/value)
	print("Numero de valores: ",val)
	print("Total de valores: ", sum)
	print("Promedio: ", prom)
	print("Deviasion estandard: ", sd)

readNumbersFromFile("random.txt")
