num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0
num6 = 0
num7 = 0
num8 = 0
num9 = 0
num10 = 0
sum_even = 0
sum_odd = 0
end = None

while True:
    print("Please enter 10 integers:")
    num1 = input("> ")
    num2 = input("> ")
    num3 = input("> ")
    num4 = input("> ")
    num5 = input("> ")
    num6 = input("> ")
    num7 = input("> ")
    num8 = input("> ")
    num9 = input("> ")
    num10 = input("> ")
    print()
    for number in [int(num1),int(num2),int(num3),int(num4),int(num5),int(num6),int(num7),int(num8),int(num9),int(num10)]:
        if number%2 == 0:
            sum_even += number
        elif number%2 != 0:
            sum_odd += number

    print ("Even sum:",sum_even)
    print ("Odd sum:",sum_odd)
    sum_odd = 0
    sum_even = 0
    print()
    print("Do you wish to repeat this program? (y/n)")
    end = input("> ")
    if end == "n":
        break
    print()
print()
print("Done!")
