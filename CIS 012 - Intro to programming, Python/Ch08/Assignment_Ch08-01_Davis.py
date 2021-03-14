def createList(listSize):
    timeList = [None] * listSize
    return timeList

def fillList(listSize, timeList):
    for i in range(listSize):
        timeList[i] = i


hoursList = createList(24)
fillList (24, hoursList)
minutesList = createList(60)
fillList (60, minutesList)
daysList = ["mo", "tu", "we", "th", "fr", "sa", "su"]
responseList = ["y", "n"]



def collectUserInputTime():
    startHour, startMinute = input("Enter the time the call starts in 24-hour rotation:\n").split(":")
    return startHour, startMinute

def validateUserInputTime(startHour, startMinute):
    try:
        startHr = int(startHour)
        startMn = int(startMinute)
    except:
        print()
        print("Invalid time input.\nPlease try again.\n")
        return False

    if startHr < 0:
        print()
        print("Invalid time input.\nPlease try again.\n")
        return False
    elif startMn < 0:
        print()
        print("Invalid time input.\nPlease try again.\n")
        return False
    elif startHr in hoursList:
        return True
    elif startMn in minutesList:
        return True
    else:
        print()
        print("Invalid time input.\nPlease try again.\n")
        return False




def collectUserInputDay():
    inp = input("Enter the first two letters of the day of the week:\n")
    firstDayCharacter = inp[0].lower()
    secondDayCharacter = inp[1].lower()
    return firstDayCharacter, secondDayCharacter

def validateUserInputDay(firstDayCharacter, secondDayCharacter):
    if (firstDayCharacter + secondDayCharacter) in daysList:
        return True
    else:
        print()
        print("Invalid day input.\nPlease try again.\n")
        return False




def collectUserInputCallLength():
    callLengthHour, callLengthMinute = input("Enter the length of the call in (hours:minutes)\n").split(":")
    return callLengthHour, callLengthMinute

def validateUserInputCallLength(callLengthHour, callLengthMinute):
    try:
        callHour = int(callLengthHour)
        callMinute = int(callLengthMinute)
    except:
        print()
        print("Invalid call length input.\nPlease try again.\n")
        return False

    if callHour < 0:
        print()
        print("Invalid time input.\nPlease try again.\n")
        return False
    elif callMinute < 0:
        print()
        print("Invalid time input.\nPlease try again.\n")
        return False
    else:
        return True




def calculateTotalCost(startHour, startMinute, firstDayCharacter, secondDayCharacter, callLengthHour, callLengthMinute):
    if (firstDayCharacter+secondDayCharacter) == daysList[0]:
        if int(startHour) < 8:
            rate = (int(callLengthMinute)*.25) + (int(callLengthHour)*15)
        elif int(startHour) >= 18:
            rate = (int(callLengthMinute)*.25) + (int(callLengthHour)*15)
        elif int(startHour) >= 8:
            rate = (int(callLengthMinute)*.40) + (int(callLengthHour)*24)
    if (firstDayCharacter+secondDayCharacter) == daysList[1]:
        if int(startHour) < 8:
            rate = (int(callLengthMinute)*.25) + (int(callLengthHour)*15)
        elif int(startHour) >= 18:
            rate = (int(callLengthMinute)*.25) + (int(callLengthHour)*15)
        elif int(startHour) >= 8:
            rate = (int(callLengthMinute)*.40) + (int(callLengthHour)*24)
    if (firstDayCharacter+secondDayCharacter) == daysList[2]:
        if int(startHour) < 8:
            rate = (int(callLengthMinute)*.25) + (int(callLengthHour)*15)
        elif int(startHour) >= 18:
            rate = (int(callLengthMinute)*.25) + (int(callLengthHour)*15)
        elif int(startHour) >= 8:
            rate = (int(callLengthMinute)*.40) + (int(callLengthHour)*24)
    if (firstDayCharacter+secondDayCharacter) == daysList[3]:
        if int(startHour) < 8:
            rate = (int(callLengthMinute)*.25) + (int(callLengthHour)*15)
        elif int(startHour) >= 18:
            rate = (int(callLengthMinute)*.25) + (int(callLengthHour)*15)
        elif int(startHour) >= 8:
            rate = (int(callLengthMinute)*.40) + (int(callLengthHour)*24)
    if (firstDayCharacter+secondDayCharacter) == daysList[4]:
        if int(startHour) < 8:
            rate = (int(callLengthMinute)*.25) + (int(callLengthHour)*15)
        elif int(startHour) >= 18:
            rate = (int(callLengthMinute)*.25) + (int(callLengthHour)*15)
        elif int(startHour) >= 8:
            rate = (int(callLengthMinute)*.40) + (int(callLengthHour)*24)
    if (firstDayCharacter+secondDayCharacter) == daysList[5]:
        rate = (int(callLengthMinute)*.15) + (int(callLengthHour)*9)
    if (firstDayCharacter+secondDayCharacter) == daysList[6]:
        rate = (int(callLengthMinute)*.15) + (int(callLengthHour)*9)
    return rate


def collectUserInputYesNo():
    YesOrNo = input("Do you want to repeat the program (y/n)?\n>>").lower()
    return YesOrNo

def validateUserInputYesNo(YesOrNo):
    if YesOrNo in responseList:
        return True
    else:
        print()
        print("Invalid response.\nPlease try again.\n")
        return False

def clearPreviousOutput(YesOrNo):
    if YesOrNo == responseList[0]:
        YesOrNo = None
        print()
        return True
    else:
        return False



while True:
    while True:
        startHour, startMinute = collectUserInputTime()
        if validateUserInputTime(startHour, startMinute) == True:
            break
    print()
    while True:
        firstDayCharacter, secondDayCharacter = collectUserInputDay()
        if validateUserInputDay(firstDayCharacter, secondDayCharacter) == True:
            break
    print()
    while True:
        callLengthHour, callLengthMinute = collectUserInputCallLength()
        if validateUserInputCallLength(callLengthHour, callLengthMinute) == True:
            break
    print()
    print("Cost of the call: $%.2f"%calculateTotalCost(startHour, startMinute, firstDayCharacter, secondDayCharacter, callLengthHour, callLengthMinute))
    print()
    while True:
        YesOrNo = collectUserInputYesNo()
        if validateUserInputYesNo(YesOrNo) == True:
            break
    if clearPreviousOutput(YesOrNo) == False:
        break
print()
print("Bye!")
