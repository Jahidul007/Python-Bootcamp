my_list = [1, 2, 3, 4, 5, 6, 7, 8]
for i in my_list:
    print(i)

for i in my_list:
    # check for even
    if i % 2 == 0:
        print('Even number: ',i)
    else:
        print(f'Odd number: {i}')
sum = 0;
for i in my_list:
    sum = sum+i
print(sum)


mystring = 'Hello Python'
for letter in mystring:
    print(letter)

# tuple
tup = (1,2,3)
for item in tup:
    print(item)

mylist = [(1,2),(3,4),(5,6),(7,8)]
print('List length: ',len(mylist))

for item in mylist:
    print(item)
# tuple in packing
for (a, b) in mylist:
    print(a)
    print(b)

# dictionary
d = {'k1': 1, 'k2': 2, 'k3': 3}

for key, value in d.items():
    print(value)



