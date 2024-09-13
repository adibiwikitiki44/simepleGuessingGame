import random

correctAnswer = random.randint(1, 10)

guess = int(input("Guess a number within 1 to 10 [Press 0 if you would like to exit]: "))

if guess == correctAnswer:
    print("Nice!! You got it the first time!")

guesses = 1

while guess != correctAnswer:

    if guess < 0 or guess > 10:
        print("invalid guess!")

    if guess == 0:
        print("Program has been terminated")
        break

    if guess > correctAnswer:
        guess = int(input("Guess lower: "))
        if guess == correctAnswer:
            print("You have guessed successfully! Took {} guesses" .format(guesses))
            break
    elif guess < correctAnswer:
        guess = int(input("Guess higher: "))
        if guess == correctAnswer:
            print("You have guessed successfully! Took {} guesses" .format(guesses))
            break

    guesses += 1
