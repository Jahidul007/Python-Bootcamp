def square(num):
    return num**2

my_nums = [1,2,3,4]

for item in map(square, my_nums):
    print(item)
def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'Even'
    else:
        return mystring[0]
names = ['Andy','jack','Rober']

for item in map(splicer, names):
    print(item)

def check_even(num):
    return num%2 == 0
my_nums = [1,2,3,4]

print(list(filter(check_even, my_nums)))

def square(num):
    result = num **2
    return  result
#print(square(5))

square = lambda num : num**3
print(square(10))
print(list(map(square, my_nums)))

print(list(filter(lambda num : num%2 == 0, my_nums)))
