def validateUserInput():
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
    return firstNum, secondNum

def oddNumbers(num1, num2):
    start = int(num1)
    finish = int(num2) + 1
    while start < finish:
        if start %2 != 0:
            print(start, end = " ")
        start = start + 1

def sumEvenNumbers(endPoint1, endPoint2):
    sum_even = 0
    start_even = endPoint1
    finish_even = endPoint2 + 1
    while start_even < finish_even:
        if start_even %2 == 0:
            sum_even = sum_even + start_even
        start_even = start_even + 1
    return sum_even


def sumSquareOddNumbers(squareOdd1, squareOdd2):
    sum_square = 0
    start_square = squareOdd1
    finish_square = squareOdd2 + 1
    while start_square < finish_square:
        if start_square %2 != 0:
            sum_square = sum_square + (start_square**2)
        start_square = start_square + 1
    return sum_square

def main():
    while True:
        firstNum, secondNum = validateUserInput()
        print()
        print("Odd integers between", str(firstNum), "and", str(secondNum), "are:")
        oddNumbers(firstNum, secondNum)
        sumEven = sumEvenNumbers(firstNum, secondNum)
        print()
        print()
        print("Sum of even integers between", str(firstNum), "and", str(secondNum), "=", str(sumEven))
        sumSquareOdd = sumSquareOddNumbers(firstNum, secondNum)
        print()
        print("Sum of the squares of odd integers between", str(firstNum), "and", str(secondNum), "=", str(sumSquareOdd))
        sumEven = 0
        sumSquareOdd = 0
        number1 = None
        number2 = None
        print()
        print("Do you wish to repeat this program?\ny/n")
        end = input("> ")
        if end == "n":
            break
        else:
            print()
    print()
    print("Bye!")

main()
