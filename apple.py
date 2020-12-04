class Apple:
    def __init__(self):
        print("Apple Created")
    pass

    _name = "jahid"

    def __detail(self, name, amount):
        print(name, amount + amount)
    def det(self):
        self.__detail('Nepali', 12)


class Banana:
    pass

    def _Det(self):
        ne = Apple.__detail(self, 'banana', 23)
        return ne


ne = Apple()
ne.det()
bn = Banana()
bn._Det()
