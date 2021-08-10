class CIS14:
    def getNumPossibleSigns(self, letterInventory: str, addresses: list, length: int) -> int:
        result = length
        test = {}
        inventory = {}

        for i in range(len(letterInventory)):
            if letterInventory[i] not in inventory:
                inventory[letterInventory[i]] = 1
            else:
                inventory[letterInventory[i]] += 1

        for x in range(length):
            for y in range(len(addresses[x])):
                if addresses[x][y] == ' ':
                    continue
                else:
                    if addresses[x][y] not in test:
                        test[addresses[x][y]] = 1
                    else:
                        test[addresses[x][y]] += 1

            for z in range(len(addresses[x])):
                if test[addresses[x][z]] > inventory[addresses[x][z]]:
                    result -= 1
                    break
                else:
                    continue

            test.clear()

        return result


def main():
    cis14 = CIS14()

    a = 'AAAABCCC123456789'
    aa = ["123C", "123A", "123 ADA"]

    b = "ABCDEFGHIJKLMNORSTUVWXYZ1234567890"
    bb = ["2 FIRST ST", " 13 PUN ST", "101 AKER"]

    c = "ABCDAAST"
    cc = ["999 S ST", "A BAD ST", "B BAD ST"]

    lengthA = len(aa)
    lengthB = len(bb)
    lengthC = len(cc)

    print(cis14.getNumPossibleSigns(a, aa, lengthA))  # 2
    print(cis14.getNumPossibleSigns(b, bb, lengthB))  # 0
    print(cis14.getNumPossibleSigns(c, cc, lengthC))  # 1


main()
