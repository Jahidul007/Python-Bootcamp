number_list = [1, 2, 3]
str_list = ['one', 'two', 'three']

# No iterables are passed
result = zip()

# Converting itertor to list
result_list = list(result)
print(result_list)

# Two iterables are passed
result = zip(number_list, str_list)

# Converting itertor to set
result_set = set(result)
print(result_set)