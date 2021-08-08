# Homework Assignments 2

## Homework 2.1
This problem is the SAME as your Homework Assignment #1 but **WITH** the use of breakCash() function and other twists. See the following **Constraints/Assumptions**. You will take your console program, and extract much of its computation logic into a separate breakCash() function with the following specification:

<pre>
/**
 * FUNCTION NAME: breakCash
 * PURPOSE: the function takes in the total of pennies from the user as input, computes its equivalent in
 * dollars, quarters, dimes, nickels, and pennies, and outputs the result in string to the console
 * PARAMETER:
 *     numPennies: int
 * RETURN VALUE:
 *     string: result in dollars, quarters, dimes, nickels, and pennies
 * FUNCTION SINGATURE:
 * breakCash(numPennies: int)
 */
</pre>

PLEASE MAKE SURE THAT YOU HAVE THE EXACT breakCash FUNCTION SIGNATURE namely

<pre>
breakCash(numPennies: int)
</pre>

DO NOT modify, add, or delete any parameters, return type, or name of the function in your assignment. 

HINTS:

* You need to formulate, and build your output string in the breakCash() function
* You do NOT print your string in breakCash()
* You may use any string formatting to do string concatenation inside breakCash() to form your desired output string 
* You then return the output string
* Finally you print the output string of breakCash() in main()
* You will start with a console program with your main() function as your entry point; to invoke your breakCash(...) function the right away, your main() function should look like this:

<pre>
def main():
    print("Please enter all of your pennies: ")
    numOfPennies = int(input())
    print(breakCash(numOfPennies))
</pre>

_**CONSTRAINTS/ASSUMPTIONS**_:

* All input are assumed to be positive, integral numbers, within the computer acceptable integral limit
* Your output for Canadian currency should be correct to exactly TWO (2) decimal places, e.g., not $1.170400 but $1.17
* You will use the same USD-Canadian Dollar exchange rate (1 to 1.33) from your Assignment #1
* For simplicity you may use the plural nouns for the currency units even if the unit is singular. Example: '1 pennies' is acceptable in your output.

## Homework 2.2
This problem is the reverse of (1) above with a small twist. Write a console application that takes the user's numeric input values for the following. You may write all of your code inside main(); no additional function is needed:

* number of half dollars (NOT DOLLARS)
* number of quarters
* number of dimes
* number of nickels
* number of pennies

And outputs the following:

<pre>
Enter half dollars: <b>23</b>

Enter quarters: <b>4</b>

Enter dimes: <b>26</b>

Enter nickels: <b>2</b>

Enter pennies: <b>6</b>

The value of your 61 coins is equivalent to 1526 pennies, or $15.26 USD
</pre>

_**CONSTRAINTS/ASSUMPTIONS**_:

* All input are assumed to be positive, integral numbers, within the computer acceptable integral limit
* Your output for USD should be correct to exactly TWO (2) decimal places, e.g., not $15 but $15.26 in the above example output
* Your available US currency units are: half dollars, quarters, dimes, nickels, and pennies.
* For simplicity you may use the plural nouns for the currency units even if the unit is singular. Example: '1 pennies' is acceptable in your output.