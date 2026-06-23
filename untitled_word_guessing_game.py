import english_words
from english_words import get_english_words_set
import random

word_gen = get_english_words_set(['web2'], lower=True)
word_pull = list(word_gen)
word_pool = [word for word in word_gen if len(word) == 6]
word_pick = random.choice(word_pool)

print(word_pick)

guess_list = []

# i read all of these quotes in baldi's voice while actively typing them
# im actually so chopped LMAOOO
while True:
    guess = input("Take a guess! ")
    guess_list.append(guess)

    if guess == word_pick:
        print("Wow! Congratulations!")
        break
    elif len(guess) != 6:
        print("Oops! Try guessing a 6-letter word next time!")
    elif guess not in word_pull:
        print("Oops! Try guessing a real word next time!")
    else:
        letters = [letter for letter in word_pick if letter in guess]
        print("You got " + str(len(letters)) + " letters in the correct word in that guess!")
        print("Now, try again!")

score = len(guess_list)
if len(guess_list) == 1:
    print("INCREDIBLE! You guessed the word on your first try!")
else:
    print("You guessed the word in " + str(score) + " guesses!")
