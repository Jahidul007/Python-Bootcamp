class my_class(object):
    def set_val(self, value):
        self.value = value

    def get_value(self):
        return self.value

a = my_class()
b = my_class()

a.set_val(10)
a.value = 10000
b.set_val(100)

print(a.get_value())
print(b.get_value())

