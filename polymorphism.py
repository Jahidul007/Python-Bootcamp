class Dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof!"

class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meow!"

niko = Dog('Niko')
felix = Cat('Felix')

#print(niko.speak())
#print(felix.speak())

for pet in [niko, felix]:
    print(type(pet))
   # print(type(pet.speak()))

def pet_speak(pet):
    return pet.speak()
print(pet_speak(niko))
print(pet_speak(felix))

class Animal ():

    def __init__(self, name):
        self.name  = name

    def speak(self):
        raise NotImplementedError("SubClass must implemented this abstract method")
class Dog(Animal):

    def speak(self):
        return self.name + " says woof!"

class Cat(Animal):

    def speak(self):
        return self.name + " says meow!"

myanimal = Dog("Fred")
print(myanimal.speak())

myanimal = Cat("ISSO")
print(myanimal.speak())


class Parrot:

    def fly(self):
        print("Parrot can fly")

    def swim(self):
        print("Parrot can't swim")


class Penguin:

    def fly(self):
        print("Penguin can't fly")

    def swim(self):
        print("Penguin can swim")


# common interface
def flying_test(bird):
    bird.fly()
    bird.swim()


# instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)