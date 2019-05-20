x = 0

while x < 5:
    print(f'The current value of x is {x}')
    x = x + 1

# pass
x = [1, 2, 3]
for item in x:
    pass

# continue

x = 'Python'
for item in x:
    if item == 'y':
        continue
    print(item)

print()
# break
x = 'Python'
for item in x:
    if item == 'y':
        break
    print(item)