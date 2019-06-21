# decimal to hexadecimal
print(hex(512))

# decimal to binary
print(bin(10))

# 2 power of 3
print(2 ** 3)

# 2 power of 9 and mod by 3
print(pow(2, 9, 3))

print(round(2.6))

print(round(3.1416592,2))

print(abs(-4))


from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets

def func(x):
    return x**2
interact(func, x =True)