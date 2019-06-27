def div42by(dividedby):
    try:
        return 42 / dividedby
    except:
        return "You tried to divide by zero"


print(div42by(2))
print(div42by(3))
print(div42by(0))

print("How many cats do you have?")
numcats = input()

try:
    if (numcats > 4):
        print("That is a lot of cats")
    else:
        print("That is not many cats")
except:
    print("There is an invalid input")
