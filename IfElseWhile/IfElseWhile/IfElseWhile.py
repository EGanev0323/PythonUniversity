#cmd=int(input('Enter number: '))

#if cmd<50:
#    print('F')
#elif cmd>=50 and cmd<60:
#    print('E')
#elif cmd>=60 and cmd <70:
#    print('D')
#elif cmd>=70 and cmd <80:
#    print('C')
#elif cmd>=80 and cmd<90:
#    print('B')
#elif cmd>=90:
#    print('A')


#for i in range(11,1,-2): #with -2 we create descending loop with 2 steps
#    print(i)

#for i in range(11,1,2): #with 2 we create ascending loop with 2 steps
#    print(i)


#for letter in range(ord('a'),ord('z')+1):    #ord- order от усвоим за нас към бинарен за компютъра
#    print(chr(letter))                       #All symbols from a to z

#for letter in range(ord('z'),ord('a')-1,-1):    #ord- order  от усфоим за нас към бинарен за компютъра
#    print(chr(letter))                          #All symbols from z to a

#word='Python'                   #Print letter by letter whe given word
#for i in word:
#    print(i)


#for i in range(20,0,-2):        #All even numbers in descending order 
#    print(i)

#n=1
#while n<=11:
#    n+=2
#    print(n)
#    n+=1
 

#n=int(input())
#sum=0
#while True:
#    sum+=n%10
#    n=n//10
#    if not n:
#        break

#print(sum)


#for number in range(1,20):
#    if number==5:
#        continue
#    if number ==11:
#        break
#    print(number)


#програма която въвежда n цели чилса и намира най- голямото

#n=int(input('Enter n: '))
#maxim=0
#for i in range(n):
#    num=int(input('Enter number: '))
#    if num>maxim:
#        maxim=num

#print(f'Maximum number is: {maxim}.')




# Sum of the numbers

#n=int(input('Enter n: '))
#sums=0
#for i in range(n):
#    num=int(input('Enter number: '))
#    sums+=num
#print(f'Sum is: {sums}.')



# Triangle with *

n=int(input())  
for x in range(n+1):
    print('*'*x)