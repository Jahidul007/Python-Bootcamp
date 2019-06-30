# THIS IS a guess the number game.
import random
print("HELLO. What is your name")
name = input()
print("well, "+ name +' I am thinking a number between 1 and 10')
secret_number = random.randint(1, 20)

for guessTaken in range(1, 7):
    print('Take a guess....')
    guess = int(input())

    if guess <secret_number:
        print('Your guess is too low')
    elif guess> secret_number:
        print('Guess is too high')
    else:
        break;
if guess == secret_number:
    print('Good job, ' + name + '! you guessed my number in ' + str(guessTaken) + ' guesses!')







print('You took ' + str(guessTaken) + ' guessses')


