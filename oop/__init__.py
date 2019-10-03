class my_num(object):
    def __init__(self, value):
        try:
            value = int(value)
        except ValueError:
            value = 0
        self.val = value

    def increament(self):
        self.val = self.val+1

string  = my_num('hello')
number = my_num(40)


string.increament()
string.increament()
number.increament()

print(number.val)