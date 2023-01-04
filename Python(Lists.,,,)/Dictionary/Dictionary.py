#d=dict(name='Ivan',LName='Ivanov')
d={'FirstName':'Ivan', 'LastName':'Ivanov'}
#print(d['name'])  

#c='name'in d #Проверява дали ключа се съдържа в речника
#print(c)
#d['sname']='Georgiev' #Добавяне на нов ключ със стойност
#print(d)

#for key in d.keys():
#    print(f'{key}=>{d[key]}')

keys=list(d.keys())  #Сортиране на речника
keys.sort()
for k in keys:
    print(f'{k} => {d[k]}')