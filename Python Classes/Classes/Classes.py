

#class Person:
#    def __init__(self,name,age):
#        self.name=name
#        self.age=age
#        self.__w=10 #Частен атрибут

#MyPerson=Person("Ivan",35)
#print(MyPerson.name)
#print(MyPerson.age)


#__ make attribute private

#class Car:
#    #class attribute
#    car_type="sports"
#    def __init__(self,color):
#        #instance attribute
#        self.__color=color
#    def print_car(self):
#        print(self.__color,"\t",self.car_type)
#    def get_color(self):
#        return self.__color
#    def set_color(self,color):
#        self._color=color
#car2=Car("Yellow")
#car2.print_car()
##car2.color="black" #cant change private attribute value
##car2.print_car()
##print(car2.__color)
#car2.set_color("green")
#print(car2.get_color())
#car2.print_car()


#class FirstClass:
#    x=5
#    def FirstClassMethod():
#        print("This is class method")
#FirstClass.FirstClassMethod()

#class Person:
#    pass   #празен клас

#class Person:
#    def __init__ (self,fname,lname,year):
#        self.firstname=fname
#        self.lastname=lname
#    def printName(self):
#        print(self.firstname,self.lastname)

#MyPerson=Person("Ivan", "Petrov")
#MyPerson.printName()

#class Student(Person):  #Наследяване на клас
#    pass

#MyStudent=Student("Ivan","Ivanov")
#MyStudent.printName()

#class Student(Person):  
#    def __init__(self,fname,lname):
#        #super().__init__(self,fname,lname,year)
#        Person.__init__(self,fname,lname,year)  #Може и двете
#        self.graduationyear=year

#MyStudent=Student("Petur","Petrov",2019)

#class Person:
#    def __init__ (self,fname,lname,year):
#        self.firstname=fname
#        self.lastname=lname
#    def printName(self):
#        print(self.firstname,self.lastname)

#MyPerson=Person("Ivan", "Petrov",2019)
#MyPerson.printName()

#class Student(Person):  
#    def __init__(self,fname,lname,year):
#        #super().__init__(self,fname,lname,year)
#        Person.__init__(self,fname,lname,year)  #Може и двете
#        self.graduationyear=year
#    def welcome(self):
#        print("Welcome",self.firstname,self.lastname,"to the class of", self.graduationyear)

#MyStudent=Student("Petur","Petrov",2019)
#MyStudent.welcome()

#class Person:
#    def __init__(self,fname,lname):
#        self.firstname=fname
#        self.lastname=lname
#    def __str__(self):
#        return f"{self.firstname} {self.lastname}"
#person1=Person("polina","koleva")
#print(person1)