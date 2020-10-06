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


#Methods available for lists

sample_list = [1,2,3,4,5,6,7,8]

sample_list.append()                  #Adds an element at the end of the list
sample_list.clear()                   #Removes all the elements from the list
sample_list.copy()                    #Returns a copy of the list
sample_list.count()                   #Returns the number of elements with the specified value
sample_list.extend()                  #Add the elements of a list (or any iterable), to the end of the current list
sample_list.index()                   #Returns the index of the first element with the specified value
sample_list.insert()                  #Adds an element at the specified position
sample_list.pop()                     #Removes the element at the specified position
sample_list.remove()                  #Removes the first item with the specified value
sample_list.reverse()                 #Reverses the order of the list
sample_list.pop()                     #Sorts the list
