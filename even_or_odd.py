value_1 = float(input("Type a number! "))
value_2 = float(value_1 / 2)

if value_2.is_integer() == False:
    print("This number is odd!")
elif value_2.is_integer() == True:
    print("This number is even!")
