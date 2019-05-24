def myfunc(a,b,c=0,d=10):
    # return 5% of the sum of a and b
    return sum((a,b,c,d)) * 0.05

print(myfunc(40,60))

def myfun(*args):
    for item in args:
        print(item)
print(myfun(40,34,34,3,4))


def myfunc1(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit')
result = myfunc1(fruit='apple', veggie = 'lettuce')
print(result)


def myfunc2(*args, **kwargs):
    print('I would like {} {}'.format(args[0], kwargs['food']))

result = myfunc2(10,22,33, fruit = 'orange', food ='eggs', animal = 'dog')
print(result)
