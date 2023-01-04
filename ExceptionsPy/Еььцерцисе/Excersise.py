#число от 1000 до 2000. число което го делим на пи трянва да има цифрата 6 до макс 3тия символ



def f():
    u=float(input("Enter number in range 1000-2000"))
    if n<1000 or u>2000:
        print("Number is not in range")
        return f()
    else:
        x=round(u/math.pi,3)
        if '6' in str(x):
            x=str(x)
            try:
            print('6 is not included in x:'+x)
            except:
            print('6 in included in x')
            f()
            
f()