import random
N = int(input('Enter a number bigger than 30 '))

number = random.randint(0,N+1)
number_of_guesses = 0
guesses = 0

while number_of_guesses < 4 and guesses != number:
    print('Guess a number between 1 and {}'.format(N))
    guess = int(input('Guess a number! '))
    number_of_guesses = number_of_guesses + 1
    if guess > 4:
        print('True number is less than your guess!')
    if guess < 4:
        print('True number is bigger than your guess!')
    elif guess == 4:
        print('Your guess is correct!!!')
        break
    else:
        print('You did not find it')
else:
    print('TRY AGAIN!')