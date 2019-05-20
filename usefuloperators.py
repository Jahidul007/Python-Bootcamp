for num in range(10):
    print(num)

index = 0;
for letter in 'abcde':
    print('Index at {} the letter is {}'.format(index, letter))
    index +=1

# enumerate
word = "abcde"
for letter in enumerate(word):
    print(letter)

# zip

res = input("what is your name: ")

print(res)