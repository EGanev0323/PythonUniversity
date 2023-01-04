
from Delene import delene
from Minus import minus
from Plus import plus
from Umnoje import umnoje




cmd= input()
while cmd!='End':
    if cmd=="Delene":
        a=float(input("Enter a: "))
        b=float(input("Enter b: "))
        delene(a,b)
    elif cmd=="Minus":
        a=float(input("Enter a: "))
        b=float(input("Enter b: "))
        minus(a,b)
    elif cmd=="Plus":
        a=float(input("Enter a: "))
        b=float(input("Enter b: "))
        plus(a,b)
    elif cmd=="Umnj":
        a=float(input("Enter a: "))
        b=float(input("Enter b: "))
        umnoje(a,b)
    else:
        print("Wrong cmd")
    cmd=input()
