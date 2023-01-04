#num=10
#L=lambda n:2*n+1
#print('Odd nums')
#for i in range(num):
#    print(L(i),end=', ')
#print('\nKвадрати на числата')
#for i in range(num):
#    print((lambda x:x*x) (i+1), end=', ')

def f():
    global s   #Глобализира за целия код с да съществува и да се променя в зависимост от функцията
    s=10

s=5
print(s)
f()
print(s)
