hours, minutes = input("Enter the time the call starts in 24-hour rotation: ").split(":")
print()
day = input("Enter the first two letters of the day of the week: ").lower()
print()
length = input("Enter the length of the call in minutes: ")
hrs = int(hours)
mins = int(minutes)
call = int(length)
rate = 0

def calculateTotalCost(hour, week, call_length):
    if week == "mo":
        if hour < 8:
            rate = call_length*.25
        elif hour >= 18:
            rate = call_length*.25
        elif hour >= 8:
            rate = call_length*.40
    if week == "tu":
        if hour < 8:
            rate = call_length*.25
        elif hour >= 18:
            rate = call_length*.25
        elif hour >= 8:
            rate = call_length*.40
    if week == "we":
        if hour < 8:
            rate = call_length*.25
        elif hour >= 18:
            rate = call_length*.25
        elif hour >= 8:
            rate = call_length*.40
    if week == "th":
        if hour < 8:
            rate = call_length*.25
        elif hour >= 18:
            rate = call_length*.25
        elif hour >= 8:
            rate = call_length*.40
    if week == "fr":
        if hour < 8:
            rate = call_length*.25
        elif hour >= 18:
            rate = call_length*.25
        elif hour >= 8:
            rate = call_length*.40
    if week == "sa":
        rate = call_length*.15
    if week == "su":
        rate = call_length*.15
    return rate


print()
print("Cost of the call: $%.2f"%calculateTotalCost(hrs, day, call))
