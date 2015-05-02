def check_banana(x):
    z=open(x,"r")
    y=0
    for i in z:
        l=i.lower()
        sub=l.find("banana")
        while sub !=(-1):
            y=y+1
            sub=l.find("banana",(sub+1))
    return(b)

check=check_banana("banana.txt")
print("Numero de bananas: ",check)
