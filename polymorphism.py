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