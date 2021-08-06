vowel = input("Enter a character between a and z (or A and Z): ")

def isVowel():
    for x in vowel:
        if x == "A":
            return True
        elif x == "a":
            return True
        elif x == "E":
            return True
        elif x == "e":
            return True
        elif x == "I":
            return True
        elif x == "i":
            return True
        elif x == "O":
            return True
        elif x == "o":
            return True
        elif x == "U":
            return True
        elif x == "u":
            return True
        else:
            return False

print()
print(vowel,"is a vowel:",isVowel())
