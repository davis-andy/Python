'''
This assignment determines if a number is prime or not
'''

# Function to determine a prime number
def isPrime(number):

    if number > 1:
        for i in range(2, int(number/2)+1):
            if number % i == 0:
                print(f'{number} is not a prime number.')
                break
        else:
            print(f'{number} is a prime number.')
    else:
        print(f'{number} is not a prime number.')

# Loop program unless user ends
while True:
    prime = int(input('Please enter a number: '))

    isPrime(prime)

    repeat = input('Do you want to repeat? (Y/N) ').lower()
    print('')

    if repeat == 'n':
        break

print('Thank you for playing!')