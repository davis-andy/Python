def CanIAlwaysWin(n: int) -> bool:
    result = True

    if n % 5 == 0:
        result = False

    return result


def main():
    n = int(input('Enter a number: '))
    print(f'Can I win: {CanIAlwaysWin(n)}')


main()
