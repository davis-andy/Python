a,b,c = input("Please input three integers: ").split()

try:
    if int(a)<=int(b)<=int(c):
        print()
        print("Input three integers in ascending order:",a,b,c)
    elif int(a)<=int(c)<=int(b):
        print()
        print("Input three integers in ascending order:",a,c,b)
    elif int(b)<=int(a)<=int(c):
        print()
        print("Input three integers in ascending order:",b,a,c)
    elif int(b)<=int(c)<=int(a):
        print()
        print("Input three integers in ascending order:",b,c,a)
    elif int(c)<=int(b)<=int(a):
        print()
        print("Input three integers in ascending order:",c,b,a)
    else:
        print()
        print("Input three integers in ascending order:",c,a,b)

except:
    print()
    print("Error, enter a numerical value")
    exit()
