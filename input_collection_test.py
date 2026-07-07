op_list = []

while True:
    guh = input("Type a sentence with no commas! (type 'stop' to stop!) ")
    if guh == "stop":
        print("Stopping!")
        break
    elif "," in guh:
        print("Invalid input!")
    else:
        op_list.append(guh)
        print("Sentence added!")

print(str(op_list))
print("Exactly " + str(len(op_list)) + " sentences are in this mega-sentence!")
