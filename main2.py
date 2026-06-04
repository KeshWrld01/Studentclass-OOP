class student:
    name = "Feel"
    print("Hello, my name is ",name)
ob =  student()

class student1:
    grade = 10
    name  = "Feel"

    def introduction(self):
        print("Hi I am a student")
    def details(self):
        print("My name is ",self.name)
        print("I am in grade ",self.grade)

object1  = student1()
object1.introduction()
object1.details()

class parrot:
    species = "Bird"

    def __init__(self,name,age):
        self.name = name
        self.age = age

blu  = parrot("Blu",10)
woo  = parrot("Woo",15)

#accessing the class attributes
print("Blu is a ",blu.species)
print("Woo is a ",woo.species)

#access the instance attributes
print("{} is {} years old".format(blu.name,blu.age))
print("{} is {} years old".format(woo.name,woo.age))