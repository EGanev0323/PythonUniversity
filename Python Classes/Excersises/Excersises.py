class Person:
    def __init__(self,fName,lName,nationality):
        self.firstName=fName
        self.lastName=lName
        self.nationality=nationality
    #def prints(self):
    #   print(f"{self.firstName} {self.lastName} {self.nationality}")
    def __str__(self):
        return f"{self.firstName} {self.lastName} {self.nationality}"



class Student(Person):
    def __init__(self, fName, lName, nationality,university,yearofstudy):
        super().__init__(fName, lName, nationality)
        self.university=university
        self.yearofstudy=yearofstudy
    #def prints(self):
    #    print(f"{self.firstName} {self.lastName} {self.nationality} {self.university} {self.yearofstudy}")
    def __str__(self):
        return f"{self.firstName} {self.lastName} {self.nationality} {self.university} {self.yearofstudy}"



class Lecture(Person):
    def __init__(self, fName, lName, nationality,university,experience):
        super().__init__(fName, lName, nationality)
        self.university=university
        self.experience=experience
    #def prints(self):
    #    print(f"{self.firstName} {self.lastName} {self.nationality} {self.university} {self.experience}")
    def __str__(self):
        return f"{self.firstName} {self.lastName} {self.nationality} {self.university} {self.experience}"


p=Person("Petur","Petrov","Bulgaria")
#p.prints()
print(p)

s=Student("Georgi","Georgiev","Bulgaria","TU",2022)
#s.prints()
print(s)

l=Lecture("Ivan", "Ivanov", "Bulgaria","TU", 20)
#l.prints()
print(l)