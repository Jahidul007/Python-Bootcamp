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


#Methods that are available in dictionaries

sample_dict = {1:'a', 2:'b', 3:'c', 4:'d'}
sample_dict.clear()                       #Clears the dictionary without deleting it
sample_dict.copy()                        #Copies the dictionary to a new memory location
sample_dict.fromkeys()                    #Returns a dictionary with the specified keys and value
sample_dict.keys()                        #Returns a list containing the dictionary's keys
sample_dict.values()                      #Returns a list of all the values in the dictionary
sample_dict.get()                         #Returns the value of the specified key
sample_dict.items()                       #Returns a list containing a tuple for each key value pair 
sample_dict.pop()                         #Removes the element with the specified key
sample_dict.popitem()                     #Removes the last inserted key-value pair
sample_dict.update()                      #Updates the dictionary with the specified key-value pairs
sample_dict.setdefault()                  #Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
