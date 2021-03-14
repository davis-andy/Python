sum_even = 0
sum_square = 0
number1 = None
number2 = None
loops = [1]
validate = [1]

for loop in loops:
    for i in validate:
        print("Enter two positive integer numbers.\nFirst number must be less than the second number:")
        number1, number2 = input("Enter numbers: ").split()
        try:
            firstNum = int(number1)
            secondNum = int(number2)
        except ValueError:
            print()
            print("Incorrect input.\nPlease try again.")
            print()
            validate.append(i+1)
            continue
        if firstNum < 0:
            print()
            print("No negative numbers!\nPlease try again.")
            print()
            validate.append(i+1)
        elif secondNum < 0:
            print()
            print("No negative numbers!\nPlease try again.")
            print()
            validate.append(i+1)
        elif firstNum > secondNum:
            print()
            print("First number must be less than second number!\nPlease try again.")
            print()
            validate.append(i+1)
        elif firstNum < secondNum:
            break


    print()
    print("Odd integers between", number1, "and", number2, "are:")
    for odd in range(firstNum,(secondNum+1)):
        if odd %2 != 0:
            print (odd, end=" ")
    print()
    print()


    for evens in range(firstNum, (secondNum+1)):
        if evens %2 == 0:
            sum_even = sum_even + evens
    print("Sum of even integers between", number1, "and", number2, "=", str(sum_even))
    print()


    for square in range(firstNum, (secondNum+1)):
        if square %2 != 0:
            sum_square = sum_square + (square**2)
    print("Sum of the squares of odd integers between", number1, "and", number2, "=", str(sum_square))

    sum_even = 0
    sum_square = 0
    number1 = None
    number2 = None
    print()
    print("Do you wish to repeat this program?\ny/n")
    end = input("> ")
    if end == "y":
        print()
        loops.append(loop+1)
    elif end == "n":
        break
print()
print("Bye!")
