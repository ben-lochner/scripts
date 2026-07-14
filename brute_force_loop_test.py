while True:
    try:
        xc = int(input("Please input your x coordinate! (0-500): "))
        if xc < 0 or xc > 500:
            print("Out of range! Please try again!")
            continue
            # ^^^ wait what what do you mean theres a continue button
        break
    except ValueError as error:
        print("Invalid input! Please try again!")
while True:
    try:
        yc = int(input("Please input your y coordinate! (0-500): "))
        if yc < 0 or yc > 500:
            print("Out of range! Please try again!")
            continue
            # ^^^ well this is mighty convenient isnt it :3
        break
    except ValueError as error:
        print("Invalid input! Please try again!")
cc = (xc, yc)

xg = 0
yg = 0

while True:
    xg = xg + 1
    if xg == xc:
        print("X coordinate found!")
        break
    else:
        pass
while True:
    yg = yg + 1
    if yg == yc:
        print("Y coordinate found!")
        break
    else:
        pass
ccg = (xg, yg)
print("Your coordinates are " + str(ccg) + "!")
