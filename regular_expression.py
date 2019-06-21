import re
patterns = ['term1', 'term2']

text = 'This is a string with term1, but not the other term'

print(re.search('hello', 'hello world!'))

for pattern in patterns:
    print('Searching for {} in:\n{}'.format(pattern, text))

    if re.search(pattern, text):
        print("\n")
        print("Match was found")
    else:
        print("\n")
        print("No match found")

match = re.search(patterns[0], text)
print(type(match))

print(match.start())
print(match.end())
