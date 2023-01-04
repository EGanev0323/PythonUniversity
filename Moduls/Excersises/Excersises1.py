from Rectangle import rectangle
from Romb import romb
from Square import square
from Trapezoid import trapezoid
from Triangle import triang

cmd= input()
while cmd!='End':
    if cmd=="Rectangle":
        a=float(input("Enter a: "))
        b=float(input("Enter b: "))
        rectangle(a,b)
    elif cmd=="Romb":
        a=float(input("Enter a: "))
        h=float(input("Enter h: "))
        romb(a,h)
    elif cmd=="Square":
        a=float(input("Enter a: "))
        square(a)
    elif cmd=="Trapezoid":
        a=float(input("Enter a: "))
        b=float(input("Enter b: "))
        h=float(input("Enter h: "))
        trapezoid(a,b,h)
    elif cmd=="Triangle":
        a=float(input("Enter a: "))
        h=float(input("Enter h: "))
        triang(a,h)
    else:
        print("Wrong cmd")
    cmd=input()