import random

number = random.randint(1, 300)
guess_count = []
print("I've picked a random number from 1 to 300, take a guess!")
while True:
    guess = int(input("Take a swing at it! (Input an integer!) "))
    guess_count.append(guess)
    difference = abs(guess - number)
    if difference == 0:
        score = len(guess_count)
        print("Great! You guessed the number after " + str(score) + " guesses!")
        break
    elif difference <= 2:
        print("You're blazing hot!")
    elif difference <= 5:
        print("Getting real hot!")
    elif difference <= 20:
        print("Getting warmer!")
    elif difference <= 50:
        print("Getting cooler!")
    elif difference <= 100:
        print("Freezing cold!")
    else:
        print("You're in Antarctica!")
