# Homework / Lab Assignments 2

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
* You may use sprintf, stringstream, itoa, etc., the choice is up to you, to do string concatenation inside breakCash() to form your desired output string 
* You then return the output string
* Finally you cout the output string of breakCash() in main()
* You will start with a console program with your main() function as your entry point; to invoke your breakCash(...) function the right away, your main() function should look like this:

<pre>
main():
    print("Please enter all of your pennies: ")
    numOfPennies = int(input())
    print(breakCash(numOfPennies))
</pre>

## Lab 1
* Get your IDE (Integrated Development Environment) to work on a sample program on your computer (or any public computer).
* Create your first "Hello World" program, and compile it in the IDE. Please reference Chapter 2 in your textbook for instructions

## Lab 2
Print to screen the following sentence:

<pre>
The CIS14 C++ Programming class
</pre>

(a) all on one line

(b) on five lines, and

(c) inside a box using a combination of '_' and '|' characters
