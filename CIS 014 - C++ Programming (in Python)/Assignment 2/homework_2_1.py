def breakCash(numPennies: int) -> str:
    cad = (numPennies / 100) * 1.33

    dollars = numPennies // 100
    cents = numPennies % 100
    quarters = cents // 25
    dimes = (cents % 25) // 10
    nickels = (cents % 25 % 10) // 5
    pennies = (cents % 25 % 10 % 5)

    sentence = f'In US currency you have: {dollars} dollars, {quarters} quarters, {dimes} dimes, {nickels} nickels, ' \
               f'and {pennies} pennies.\n'
    sentence += f'In canadian currency you have: {cad:.2f} dollars.'

    return sentence


def main():
    print("Please enter all of your pennies: ")
    numOfPennies = int(input())
    print(breakCash(numOfPennies))


main()
