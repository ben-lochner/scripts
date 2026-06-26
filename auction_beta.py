user_list = []
bid_list = []
budget = 10000

while True:
    user = input("Please input your name! (if no user, type 'none') ")
    if user == "none":
        break
    else:
        user_list.append(user)
        # look at me i know how to append things now

if user_list == []:
    print("Feel free to come back later!")
else:
    print("Welcome to the auction!")

    list_select = -1
    for user in user_list:
        list_select = list_select + 1

        while True:
            bid = int(input(user_list[list_select] + ", Place your bid here! "
                                                    "Your budget is $" + str(budget) + "! $"))
            if bid > budget:
                print("Your bid is over the budget! Please try a different number!")
            elif bid < 0:
                print("Invalid integer! Please try a different number!")
            else:
                break
        bid_list.append(bid)
    print(str(user_list[bid_list.index(max(bid_list))]) + " wins with a bid of "
                                                    + str(max(bid_list)) + "!")

# this is very unfinished
# but i realistically am going to have to finish this over multiple days
# so ill leave it at this for now :3
