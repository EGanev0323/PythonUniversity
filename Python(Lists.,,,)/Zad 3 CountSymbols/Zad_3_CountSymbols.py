#3. Напишете програма , в която потребителя въвежда текст и на негова база 
#се създава речник. За ключове на речника служат символите от текста, а 
#стойността на елементите се определя от броя на съответните символи в 
#текста. 
#Примерен вход : SSWTWWTAAA 
# Речникът ще се състои от 4 елемента : 
# А:3 S:2 T:2 W:3 



#lists=input("Enter elemnts: ")
#thisdic={}
#count=0
#for x in range(len(lists)-1):
#    if x>=1:
#        if lists[x]==lists[x-1]:
#            continue
#        for i in lists:
#            if lists[x]==i:
#                count+=1

#        thisdic[lists[x]]=count
#        count=0
#    else:
#        for i in lists:
#            if lists[x]==i:
#                count+=1

#        thisdic[lists[x]]=count
#        count=0
    
#print(thisdic)




lists=input("Enter elemnts: ")
thisdic={}
count=0
for x in lists:
    for i in lists:
        if x==i:
            count+=1
    
    thisdic[x]=count
    count=0
    
print(thisdic)
