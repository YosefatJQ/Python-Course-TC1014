def divisor(x,y):
    if (x==y):
        return x
    elif(x>y):
        z=divisor((x-y),y)
    else:
        z=divisor(x,(y-x))
    return z
print("Greatest common Divisor.")
x=int(input("Give me the first number: "))
y=int(input("Give me the second one: "))
print("The Greatest common divisor of", x, "and", y, "is: ", divisor(x,y))
