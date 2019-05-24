def name_function():
    print("Hello")

def say_hello(name = 'Name'):
    return 'Hello ' + name
result = say_hello("Jose")
print(result)

def add(n1, n2):
    return n1+n2

result = add(9,9)
print(result)

def dog_check(mystring):
    if 'dog' in mystring:
        return True
    else:
        return False
print(dog_check("dog in away"))
