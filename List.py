my_list = ['jahid', 'cse', 'Comilla university']
print(len(my_list))
for i in my_list:
    print(i)

another_list = ['fahim', 'comilla university']

new_list = my_list + another_list
print(new_list)
new_list[0] = 'One all caps'

print(new_list)

# append allows to add new item in list
new_list.append('saifur')
print(new_list)

#pop remove item from the list at last node
new_list.pop()
print(new_list)

# sort list
new_list.sort()
print(new_list)
