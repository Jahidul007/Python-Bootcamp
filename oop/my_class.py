import random
class MyClass(object):
    def call_function(self):
        self.random_val = random.randint(1, 10)


this_object = MyClass()
this_object.call_function()
print(this_object.random_val);