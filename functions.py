def name_function():
    print("Hello")

def say_hello(name = 'Name'):
    return 'Hello ' + name
result = say_hello("Jose")
print(result)

def add(n1, n2):
    return n1+n2

result = add(9,9)
print(result)

def dog_check(mystring):
    if 'dog' in mystring:
        return True
    else:
        return False
print(dog_check("dog in away"))

def pig_lattin(word):
    first_letter = word[0]

    #check if vowel

    if first_letter in 'aeiou':
        pig_word = word  + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    return pig_word
print(pig_lattin('apple'))
