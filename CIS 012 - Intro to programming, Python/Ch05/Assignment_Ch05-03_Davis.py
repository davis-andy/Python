sum_even = 0
sum_square = 0
number1 = None
number2 = None

while True:
    while True:
        print("Enter two positive integer numbers.\nFirst number must be less than the second number:")
        number1, number2 = input("Enter numbers: ").split()
        try:
            firstNum = int(number1)
            secondNum = int(number2)
        except ValueError:
            print()
            print("Incorrect input.\nPlease try again.")
            print()
            continue
        if firstNum < 0:
            print()
            print("No negative numbers!\nPlease try again.")
            print()
        elif secondNum < 0:
            print()
            print("No negative numbers!\nPlease try again.")
            print()
        elif firstNum > secondNum:
            print()
            print("First number must be less than second number!\nPlease try again.")
            print()
        elif firstNum < secondNum:
            break


    start = firstNum
    finish = secondNum + 1
    print()
    print("Odd integers between", number1, "and", number2, "are:")
    while start < finish:
        if start %2 != 0:
            print(start, end = " ")
        start = start + 1


    start_even = firstNum
    finish_even = secondNum + 1
    while start_even < finish_even:
        if start_even %2 == 0:
            sum_even = sum_even + start_even
        start_even = start_even + 1
    print()
    print()
    print("Sum of even integers between", number1, "and", number2, "=", str(sum_even))


    start_square = firstNum
    finish_square = secondNum + 1
    while start_square < finish_square:
        if start_square %2 != 0:
            sum_square = sum_square + (start_square**2)
        start_square = start_square + 1
    print()
    print("Sum of the squares of odd integers between", number1, "and", number2, "=", str(sum_square))


    sum_even = 0
    sum_square = 0
    number1 = None
    number2 = None
    print()
    print("Do you wish to repeat this program?\ny/n")
    end = input("> ")
    if end == "n":
        print()
        break
    print()
print("Bye!")
