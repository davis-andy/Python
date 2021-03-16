'''
This assignment determines the number of days in a month given the year
'''

# variable for determining Leap Year
leap = False

# Function to determine Leap Year
def leap_year(year):
    global leap

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False

# Function to determine days in a month
def days_in_month(month):
    switcher = {
        1: 31, # January
        2: 28, # February
        3: 31, # March
        4: 30, # April
        5: 31, # May
        6: 30, # June
        7: 31, # July
        8: 31, # August
        9: 30, # September
        10: 31, # October
        11: 30, # November
        12: 31, # December
    }

    return switcher.get(month)

# Loop program unless user ends
while True:
    year = int(input('Please enter the 4 digit year: '))
    month = int(input('Please enter the month: '))
    days = 0

    leap_year(year)

    if leap == True and month == 2:
        days = days_in_month(month) + 1
    else:
        days = days_in_month(month)
    
    print(f'Year {year} Month {month} has {days} days in a month')
    repeat = input('Do you want to repeat? (Y/N) ').lower()
    print('')

    if repeat == 'n':
        break

print('Thank you for playing!')
