import random

card_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
card_values = {
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11,
}
# infinite deck for now
# because making a full deck
# and writing code for removing them is hard
hand = []
dealer_hand = []


def calculate_score(current_hand):
    total = 0
    aces = 0
    for card in current_hand:
        if card in card_values:
            total += card_values[card]
            if card == "Ace":
                aces += 1
        else:
            total += card
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total

def pick_a_card_any_card():
    card_random = random.choice(card_list)
    hand.append(card_random)
    print("You received a " + str(card_random) + "!")
    print("Your current total is: " + str(calculate_score(hand)))


def dealer_pick():
    dealer_card = random.choice(card_list)
    dealer_hand.append(dealer_card)
    return dealer_card


def dealer_turn():
    print("Dealer's Turn!")
    print("Dealer reveals their hidden card. Their hand is: " + str(dealer_hand))

    dealer_score = calculate_score(dealer_hand)
    print("Dealer's current total: " + str(dealer_score))

    while dealer_score < 17:
        print("Dealer hits...")
        new_card = dealer_pick()
        print("Dealer drew a " + str(new_card) + "!")
        dealer_score = calculate_score(dealer_hand)
        print("Dealer's new total: " + str(dealer_score))

    if dealer_score > 21:
        print("Dealer busts!")

    return dealer_score

def check_winner(player_score, dealer_score):
    print("Final Results")
    print("Your score: " + str(player_score))
    print("Dealer's score: " + str(dealer_score))

    if player_score > 21:
        print("You busted! Dealer wins.")
    elif dealer_score > 21:
        print("Dealer busted! You win!")
    elif player_score > dealer_score:
        print("You beat the dealer! You win!")
    elif dealer_score > player_score:
        print("Dealer wins! Better luck next time.")
    else:
        print("It's a tie (Push)!")

def hit_or_stand():
    while True:
        choice = input("Would you like to (h)it or (s)tand? ").lower().strip()
        if choice == "h":
            pick_a_card_any_card()
            if calculate_score(hand) > 21:
                print("Bust! You went over 21.")
                break
        elif choice == "s":
            print("You keep your hand at a total of " + str(calculate_score(hand)) + "!")
            break
        else:
            print("Invalid input! Please try again!")

print("Welcome to Blackjack!")
pick_a_card_any_card()
pick_a_card_any_card()

visible_card = dealer_pick()
print("The dealer shows a " + str(visible_card) + "!")
dealer_pick()

hit_or_stand()
player_final = calculate_score(hand)
if player_final <= 21:
    dealer_final = dealer_turn()
else:
    dealer_final = calculate_score(dealer_hand)
check_winner(player_final, dealer_final)

# i had google's help for like half this code
# its like 7 pm dude i can remake this later LMAO
# :3
