import string
import random

character_pool = string.ascii_letters + string.digits + string.punctuation

# as unprofessional as it is, i am a fan of how unbelievably scuffed this looks
def password_generation():
    password_gen_char_1 = random.choice(character_pool)
    password_gen_char_2 = random.choice(character_pool)
    password_gen_char_3 = random.choice(character_pool)
    password_gen_char_4 = random.choice(character_pool)
    password_gen_char_5 = random.choice(character_pool)
    password_gen_char_6 = random.choice(character_pool)
    password_gen_char_7 = random.choice(character_pool)
    password_gen_char_8 = random.choice(character_pool)
    password_gen_char_9 = random.choice(character_pool)
    password_gen_char_10 = random.choice(character_pool)
    password_gen_char_11 = random.choice(character_pool)
    return (password_gen_char_1, password_gen_char_2, password_gen_char_3,
    password_gen_char_4, password_gen_char_5, password_gen_char_6,
    password_gen_char_7, password_gen_char_8, password_gen_char_9,
    password_gen_char_10, password_gen_char_11)

while True:
    (password_gen_char_1, password_gen_char_2, password_gen_char_3,
     password_gen_char_4, password_gen_char_5, password_gen_char_6,
     password_gen_char_7, password_gen_char_8, password_gen_char_9,
     password_gen_char_10, password_gen_char_11) = password_generation()

    password_generation()
    random_password = str(password_gen_char_1 + password_gen_char_2 + password_gen_char_3 +
                      password_gen_char_4 + password_gen_char_5 + password_gen_char_6 +
                      password_gen_char_7 + password_gen_char_8 + password_gen_char_9 +
                      password_gen_char_10 + password_gen_char_11)
    print("Your password is " + random_password + ".")
    reroll = input("Would you like a new password? (yes/no): ")
    if reroll == "yes":
        print("Okay! Here is your new password:")
    elif reroll == "no":
        print("Okay! Enjoy your password!")
        break
    else:
        print("Invalid input, but let's give you a password anyway!")
