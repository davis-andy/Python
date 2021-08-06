year = input("Enter a year between 1000 to 3000: ")
iYear = int(year)
thousands = iYear//1000
hundreds = (iYear-(thousands*1000))//100
tens = (iYear-(thousands*1000)-(hundreds*100))//10
ones = (iYear-(thousands*1000)-(hundreds*100)-(tens*10))

def returnRomanOnesPlace(ones):
    if ones == 1:
        return "I"
    elif ones == 2:
        return "II"
    elif ones == 3:
        return "III"
    elif ones == 4:
        return "IV"
    elif ones == 5:
        return "V"
    elif ones == 6:
        return "VI"
    elif ones == 7:
        return "VII"
    elif ones == 8:
        return "VIII"
    elif ones == 9:
        return "IX"
    elif ones == 0:
        return ""
def returnRomanTensPlace(tens):
    if tens == 1:
        return "X"
    elif tens == 2:
        return "XX"
    elif tens == 3:
        return "XXX"
    elif tens == 4:
        return "XL"
    elif tens == 5:
        return "L"
    elif tens == 6:
        return "LX"
    elif tens == 7:
        return "LXX"
    elif tens == 8:
        return "LXXX"
    elif tens == 9:
        return "XC"
    elif tens == 0:
        return ""
def returnRomanHundredsPlace(hundreds):
    if hundreds == 1:
        return "C"
    elif hundreds == 2:
        return "CC"
    elif hundreds == 3:
        return "CCC"
    elif hundreds == 4:
        return "CD"
    elif hundreds == 5:
        return "D"
    elif hundreds == 6:
        return "DC"
    elif hundreds == 7:
        return "DCC"
    elif hundreds == 8:
        return "DCCC"
    elif hundreds == 9:
        return "CM"
    elif hundreds == 0:
        return ""
def returnRomanThousandsPlace(thousands):
    if thousands == 1:
        return "M"
    elif thousands == 2:
        return "MM"
    elif thousands == 3:
        return "MMM"

roman = str(returnRomanThousandsPlace(thousands)) + str(returnRomanHundredsPlace(hundreds)) + str(returnRomanTensPlace(tens)) + str(returnRomanOnesPlace(ones))


print()
print("Your number in roman numerals is:",roman)
