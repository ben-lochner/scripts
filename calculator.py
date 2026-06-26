while True:
    calc = input("Input a calculation! ")
    try:
        answer = eval(calc)
        print("The answer is " + str(answer) + "!")
        break
    except NameError as error:
        print("Invalid input! Please try again!")
    except SyntaxError as error:
        print("Invalid input! Please try again!")

while True:
    calc = input("Input a calculation! (Use 'ans' to use your last"
                 "calculation's answer as an integer! "
                 "Type 'done' to exit!) ")
    if calc == "done":
        print("See you later!")
        break
    else:
        try:
            if "ans" in calc:
                calc = calc.replace("ans", str(answer))
            else:
                pass

            answer = eval(calc)
            print("The answer is " + str(answer) + "!")
        except NameError as error:
            print("Invalid input! Please try again!")
        except SyntaxError as error:
            print("Invalid input! Please try again!")
