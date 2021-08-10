def convertString2Integer(s: str) -> int:
    output = 0

    for i in s:
        if i == '-':
            continue
        currentNum = ord(i) - 48
        output = output * 10 + currentNum

    if s[0] == '-':
        output *= -1

    return output


def main():
    print(convertString2Integer('123'))
    print(convertString2Integer('-123'))
    print(convertString2Integer('0000012'))
    print(convertString2Integer('1200'))


main()
