class Apple:
    pass

    _name = "jahid"

    def _detail(self, name, amount):
        print(name, amount + amount)


class Banana:
    pass

    def _Det(self):
        ne = Apple._detail(self, 'banana', 23)
        print(ne)


ne = Apple()
ne._detail('Nepali', 12)
print(ne._name)
bn = Banana()
bn._Det();
