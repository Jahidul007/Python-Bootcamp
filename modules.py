# counter
from collections import Counter
from collections import defaultdict

l = [1, 2, 3, 1, 2, 2, 3, 4, 5, 66, 6, 6, 4, ]

# print(Counter(l))

d = {'k1': 1}

print(d['k1'])

d = defaultdict(object)
print(d['one'])

for item in d:
    print(item)

d = defaultdict(lambda: 0)
print(d['one'])

d = {}

d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5

print(d)
'''
for k,v in d.items():
    print(k, v)
'''


from collections import OrderedDict

d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5


for k, v in d.items():
    print(k,v)
