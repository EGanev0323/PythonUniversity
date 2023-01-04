#1-5 free
#5-10 50% disc
#>10 10lv

n=int(input('Enter n: '))
ticketPrice=10


if n>1 and n<=5:
    print('Ticket is free')
elif n>5 and n<=10:
    print(f'Ticket is {ticketPrice/2}lv')
elif n>10:
    print(f'Ticket is {ticketPrice} lv')

