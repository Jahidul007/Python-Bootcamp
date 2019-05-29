class Sample():
    # class object attribute
    # same for any instant of a class
    species = 'mammal'

    def __init__(self, my_breed, name, spots):
        # attributes
        # we take in the argument
        # Assign it using self.attribute_name
        self.breed = my_breed
        self.name = name

        # Expect boolean True/False
        self.spots = spots

    # operation/Actions ---> Methods
    def bark(self, number):
        print("Woof! My name is {} and number is {}".format(self.name, number))


my_dog = Sample(my_breed='Lab', name='Sammy', spots=False)

print(my_dog.species)
print(my_dog.name)

my_dog = my_dog.bark(10)
print(my_dog)


class Circle():
    # CLASS OBJECT ATTRIBUTE
    pi = 3.1416

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * Circle.pi

    # METHOD
    def get_circumference(self):
        return self.radius * self.pi * 2


my_circle = Circle(30)
print(my_circle.area)
