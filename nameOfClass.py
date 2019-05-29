class Sample():
    def __init__(self, my_breed, name , spots):
        #attributes
        # we take in the argument
        # Assign it using self.attribute_name
        self.breed = my_breed
        self.name = name

        # Expect boolean True/False
        self.spots = spots

my_dog = Sample(my_breed= 'Lab', name= 'Sammy', spots=False)

print(type(my_dog))
print(my_dog.name)