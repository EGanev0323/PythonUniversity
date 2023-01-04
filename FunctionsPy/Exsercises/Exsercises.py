
##-----------1zad------------
#def square(c):
#    return c*c

#def rectangle(a,b):
#    return a*b

#def triangle(a,b):
#    return (a*b)/2


#n= input()
#while(True):
#    if n=='square':
#        c=float(input())
#        print(square(c))
#        break
#    elif n=='rectangle':
#        a=float(input())
#        b=float(input())
#        print(rectangle(a,b))
#        break
#    elif n=='triangle':
#        a=float(input())
#        b=float(input())
#        print(triangle(a,b))
#        break
#    else:
#        n=input()
    



##--------------2zad---------------
#def f(n):
#    reverseNum=str(n)[::-1]
#    if n==reverseNum:
#        print('1')
#    else:
#        print('0')
#n=input()
#f(n)

##-------------3zad----------------
#def plus(a, b):
#    return(a+b)

#def minus(a, b):
#    return(a-b)

#def umj(a, b):
#    return(a*b)

#def delE(a,b):
#    return(a/b)
    
#n=input('Command type: ')
#if n=='plus':
#    a=int(input())
#    b=int(input())
#    print(plus(a,b))
#elif n=='minus':
#    a=int(input())
#    b=int(input())
#    print(minus(a,b))
#elif n=='umj':
#    a=int(input())
#    b=int(input())
#    print(umj(a,b))
#elif n=='delE':
#    a=int(input())
#    b=int(input())
#    print(delE(a,b))


#-------------------4zad---------------

def f(l, b):
    for x in range(len(l)):
        if b<x:
            l[x]=0
    return print(l)

l=[]
a=str(input())
b=int(input())

for x in range(1,len(a)+1):
    l.append(x)

f(l,b)
