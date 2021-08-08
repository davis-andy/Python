print('Please enter all of your pennies:')
user = input()
intUser = int(user)

usdTotal = intUser / 100
cad = usdTotal * 1.33

dollars = intUser // 100
cents = intUser % 100
quarters = cents // 25
dimes = (cents - (quarters * 25)) // 10
nickels = (cents - (quarters * 25) - (dimes * 10)) // 5
pennies = (cents - (quarters * 25) - (dimes * 10) - (nickels * 5))

print(f'In US currency you have: {dollars} dollars, {quarters} quarters, {dimes} dimes, {nickels} nickels, and '
      f'{pennies} pennies.')
print(f'In canadian currency you have: {cad} dollars.')
