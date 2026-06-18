import random

# oh my god this is so scuffed but it works for now so we ball
item_1 = input("What's something you have in your fridge? ")
item_2 = input("What's something you have in your fridge? ")
item_3 = input("What's something you have in your fridge? ")
item_4 = input("What's something you have in your fridge? ")
item_5 = input("What's something you have in your fridge? ")

item_list = [item_1, item_2, item_3, item_4, item_5]

random_item_1 = random.choice(item_list)
random_item_2 = random.choice(item_list)

print("I think you should make a meal out of " + random_item_1 + " and " + random_item_2 + "!")
