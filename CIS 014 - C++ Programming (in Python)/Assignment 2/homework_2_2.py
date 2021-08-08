halfDollars = int(input('Enter half dollars: '))
print()
quarters = int(input('Enter quarters: '))
print()
dimes = int(input('Enter dimes: '))
print()
nickels = int(input('Enter nickels: '))
print()
pennies = int(input('Enter pennies: '))
print()

totalCoins = halfDollars + quarters + dimes + nickels + pennies
totalPennies = (halfDollars * 50) + (quarters * 25) + (dimes * 10) + (nickels * 5) + pennies
usd = totalPennies / 100

print(f'The value of your {totalCoins} coins is equivalent to {totalPennies}, or ${usd:.2f} USD')
