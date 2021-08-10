class CIS14:
    def isInputInDictionary(self, s: str, dic: list) -> bool:
        result = [0] * (len(s) + 1)
        result[0] = 1

        for i in range(1, len(s) + 1):
            j = i - 1
            while j >= 0:
                if s[j: i] in dic:
                    result[i] = 1
                    break
                j -= 1

        return bool(result[len(s)])


def main():
    cis = CIS14()

    a = "joe"
    aa = ["joe1", "joe"]

    b = "joey"
    bb = ["joe1", "joe"]

    c = "applepie"
    cc = ["apple", "pie"]

    d = "hellonow"
    dd = ["hello", "on", "hell", "now"]

    e = "hellonowl"
    ee = ["hell", "on", "owl"]

    print(cis.isInputInDictionary(a, aa))  # true
    print(cis.isInputInDictionary(b, bb))  # false
    print(cis.isInputInDictionary(c, cc))  # true
    print(cis.isInputInDictionary(d, dd))  # true
    print(cis.isInputInDictionary(e, ee))  # true


main()
