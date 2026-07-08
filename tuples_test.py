import random

while True:
    x_pos = input("Please put in your X position: ")
    try:
        x_pos2 = int(x_pos)
        break
    except ValueError:
        print("Invalid input! Please try again!")
while True:
    y_pos = input("Please put in your Y position: ")
    try:
        y_pos2 = int(y_pos)
        break
    except ValueError:
        print("Invalid input! Please try again!")
while True:
    z_pos = input("Please put in your Z position: ")
    try:
        z_pos2 = int(z_pos)
        break
    except ValueError:
        print("Invalid input! Please try again!")

player_pos = (x_pos2, y_pos2, z_pos2)
goal_pos = (random.randint(0, 300),
            random.randint(0, 300),
            random.randint(0, 300))
print("Your current coordinates are: " + str(player_pos) + "!")
print("The goal's coordinates are " + str(goal_pos) + "!")

math_or_something = abs(sum(tuple(a - b for a, b in zip(player_pos, goal_pos))))
# oh so thats how you subtract tuples
# also this line looks so blursed LMAO

if player_pos != goal_pos:
    print("You are " + str(math_or_something) + " units away from the goal!")
else:
    print("You hit the goal right on the bullseye!")
