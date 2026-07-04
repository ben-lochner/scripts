import random
from collections import Counter
# mfw i am using a module ive not once ever seen
# UNTIL NOOOWWW :3
found = False
# yep im using this funny loop break trick
# for like every project involving multiple loop layers
# youre gonna be seeing a lot of this LOL

print("Welcome! The the game is simple!")
print("You wager an amount of (not real, of course) money."
      "Depending on how many of the target nunbers the random number generator hits,"
      "you will either make or lose money according to your wager.")
targets = [random.randint(1, 10),
           random.randint(1, 10),
           random.randint(1, 10),
           random.randint(1, 10),
           random.randint(1, 10)]
print("Here are the targets: " + str(targets))
while True:
    choice = input("Well? Take a swing at it? (y or n): ")
    if choice == "n":
        print("Come back another time!")
        break
    elif choice == "y":
        print("Great!")
        while True:
            try:
                wager = int(input("How much would you like to wager? $"))
                print("Great! Let's see if you hit!")
                shoot_your_shot = [random.randint(1, 10),
                                   random.randint(1, 10),
                                   random.randint(1, 10),
                                   random.randint(1, 10),
                                   random.randint(1, 10)]
                cross = sum((Counter(targets) & Counter(shoot_your_shot)).values())
                print("The RNG has spoken: " + str(shoot_your_shot))
                print("The RNG has hit " + str(cross) + " targets!")
                stonks = wager*(int(cross)*10/25)
                print("You return with $" + str(stonks) + "!")
                print("Come again sometime!")
                found = True
                break
            except ValueError as error:
                print("Invalid input! Please try again!")
    if found:
        break
    else:
        print("Invalid input! Please try again!")
