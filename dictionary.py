my_dict = {'key1': 'value1', 'key2': 'value2'}
print(my_dict)
print(my_dict['key1'])
prices_lookup = {'apple': 2.99, 'oranges': 1.99, 'milk': 5.80}
print(prices_lookup)
print(prices_lookup['milk'])
print(prices_lookup['oranges'])

d = {'k1': 123, 'k2': [0, 1, 2], 'k3': {'insidekey': 100}}
print(d['k2'][1])
print(d['k3'])
print(d['k3']['insidekey'])
my_list = d['k2']
print(my_list)

d['k4'] = 300

print(d.items())
print(d.keys())
print(d.values())

num1 = 100
num2 = 100
print("Sum", num1+num2)
