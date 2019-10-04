class date(object):
    value = 10
    def get_date(self):
        return "04-10-2019"
class time(date):
    def get_time(self):
        return "11:23:45"

dt = date()
print(dt.get_date())
print(dt.value)

tm = time()
print(tm.get_time())
print(tm.get_date())


class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print('%s is a eating %s.' %(self.name, food))
class Dog(Animal):
    def fetch(self, thing):
        print('%s goes after the %s!' %(self.name, thing))

class Cat(Animal):
    def swatstring(self):
        print('%s shreds the string!' %self.name)


d = Dog('river')
c = Cat('Fluffy')

d.fetch('paper')
c.swatstring()
d.eat("dog food")
c.eat("cat food")
# d.swatstring()

















