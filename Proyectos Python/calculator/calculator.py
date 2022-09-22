def play():
    number = int(input("What's the first number?: "))
    secondNumber = int(input("What's the second number?: "))
    symbol = input("And now, what's the symbol? \n + \n - \n * \n / \n Your choose is: ")

    if symbol == "+":
        result = number + secondNumber
    elif symbol == "-":
        result = number - secondNumber
    elif symbol == "*":
        result = number * secondNumber
    elif symbol == "/":
        result = number / secondNumber


    print(f"The result is: {result}")


playA = True
while playA:
    playAgain = input("Do you want to play again? Type 'yes' or 'no': ")

    if playAgain == "yes":
        play()
    elif playAgain == "no":
        print("Bay bay")
        playA = False
    else:
        print("Thats not what I want")



