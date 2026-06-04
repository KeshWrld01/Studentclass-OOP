class student:
    grade = 4
    print("Hi I'm Lailah and I am in grade ",grade)

ob = student()

class vehicle:

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    
Mercedes = vehicle(360, 1200)

print("The max speed is", Mercedes.max_speed)
print("The mileage is", Mercedes.mileage)


class parrot:
    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

parrot1 = parrot("polly", 5)
parrot2 = parrot("kiki", 3)

print("parrot1 is {}".format(parrot1.species))
print("parrot2 is {}".format(parrot2.species))

print("{} is a {} years old".format(parrot1.name, parrot1.age))
print("{} is a {} years old".format(parrot2.name, parrot2.age))