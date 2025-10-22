import random

number = random.randint(1, 100) # random number wow
guess = input("Guess a number between 1 and 100: ")
guessnumber = 10 # number of guesses
try:
    guess = int(guess)
except ValueError:
    print("that is no number.")
    exit()
while True:
    guess = int(guess)
    if guess < number:
        print("Too low")
        guessnumber -= 1
        print("number of guesses left:", guessnumber)
        guess = input("Guess again: ")
        try:
            guess = int(guess)
        except ValueError:
            print("that is no number.")
            exit()
    elif guess > number:
        print("Too high")
        guessnumber -= 1
        print("number of guesses left:", guessnumber)
        guess = input("Guess again: ")
        try:
            guess = int(guess)
        except ValueError:
            print("that is no number.")
            exit()
    if guessnumber == 1:
        print("You ran out of guesses. The number was", number)
        exit()
    elif guess == number:
        print("You guessed it!")
        exit()
