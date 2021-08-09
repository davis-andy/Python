def getSecretMessage(s: str) -> str:
    message = ''
    delim = ' '
    delimHit = True

    for i in s:
        if i == delim:
            delimHit = True
        elif i != delim and delimHit:
            message += i
            delimHit = False

    return message


def main():
    print(getSecretMessage("professor can code"))  # prints "pcc"
    print(getSecretMessage("                "))  # prints nothing
    print(getSecretMessage("pasadena"))  # prints "p"


main()
