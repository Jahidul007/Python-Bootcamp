class Sample():
    def __init__(self, breed):
        self.breed = breed

my_dog = Sample(breed= 'Lab')

print(type(my_dog))
print(my_dog.breed)