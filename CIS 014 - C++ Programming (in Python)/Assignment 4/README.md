# Homework / Lab Assignments 4

## Homework 4.1
Take any arbitrary number, n, and append zero (0) or more numeric digits at the end of it to obtain a palindrome. The 
numeric palindrome should be the shortest, namely having the least number of digits, possible. Return the integral 
length of your shortest possible palindrome (NOT your new palindrome) per given input, n. For any non-palindrome n, 
the function returns 0.  You **MUST** make use of the following function signature:

<pre>
def getShortestLength(n: int) -> int:
</pre>

Note: you may reuse the function from your lab as the helper utility to solve for the above:

<pre>
def isPalindrome(inp: int) -> bool:
</pre>

Or, you may use any other subroutines, functions, methods, etc., you need to help you solve the getShortestLength() 
problem. 

**Examples:**

input: 121

output: 3  # (because 121 is already a palindrome)

<br />

input: 12393

output: 7  # (because 12393 -> 1239321; note you may also have 123939321 but that is not the shortest palindrome 
after the input)

<br />

input: 123

output: 5  # (because 123 -> 12321) 

<br />

input: -234

output: 0 # (because -234 is not a palindrome) 

**Constraints/Assumptions:**

* Your integral input is assumed to have been within the acceptable `sys.maxsize` range
* The function returns 0 for all non-palindrome input
* Your input can be either positive or negative
* Negative number is not palindromic
* 0 is a palindrome, so is any single positive digit (2, 3, ... , 9)

## Homework 4.2
Write a de-duplication function that iteratively sanitizes (removes) all consecutive duplicates in a Python 
string. Consecutive duplicates are a pair of duplicate English alphabets sitting next to each other in the input 
string. Example: "AA", "KK", etc., are all consecutive duplicates. This function will internally run as many 
iterations as needed to remove all consecutive duplicates until there is either no consecutive duplicates left, or 
the string becomes empty (in which the function returns "Empty" back to the user):

<pre>
def deduplicate(inp: str) -> str:
</pre>

Your main() may look like the following, or anything you prefer to put in it:

<pre>
def main():
  print(deduplicate("AABB"))  # should output "Empty"
  print(deduplicate("A"))  # "A"
  print(deduplicate("ABBA"))  # should output "Empty"
  print(deduplicate("AAA"))  # "A"
  print(deduplicate("AKA"))  # "AKA" because there is no consecutive pair.
</pre>

**Examples:**

* "KCCK" -> first iteration results in "KK" by removing "CC" as consecutive duplicates -> second iteration starts 
with "KK" as consecutive duplicates hence removed. Function returns "Empty".
* "ZZZ" -> first iteration results in "Z" by removing the first "ZZ". There is nothing to be removed after 
that. Function returns "Z".
* "KKCCD" -> first iteration removes "KK" resulting in "CCD" -> second iteration removes "CC" resulting in "D". There 
is nothing left to be removed. Function return "D".

**Constraints/Assumptions:**

* Input string consists of only uppercase English alphabets, "A" - "Z".
* Input string consists of at least 1 English alphabet.
* Input string consists of at most 100 alphabets.
* Function returns the non-reducible string. 
* If the reduced string is empty, function returns the string "Empty".

## Lab 4.1
For the following Python String print their individual characters one at a time to screen. Note for a 
Python string you may use len() to get the length of string.

<pre>
str_test = "pasadena city college"
</pre>

## Lab 4.2
You are given a Python string consisting of any lowercase alphanumeric characters ('a'-'z', '0'-'9') of length L > 2 
(where L is even). One of the characters occurs L/2 number of times. The other characters are all different. For 
this problem, do not use any existing find or search string functions, otherwise you receive no extra point. Write a 
function that find this one character that occurs L/2 number of times in the input string:

<pre>
def findHalfDuplicate(s: str) -> str:
</pre>

For example: 

<pre>
"1a2a3a4a"  # L = 8; 'a' occurs 4 times; the other characters are all different
"a2a3a1"  # L = 6; 'a' occurs 3 times; the other characters are all different
"2aa3"  # L = 4; 'a' occurs 2 times; the other characters are all different
</pre>

Not valid input:

<pre>
"1a"  # L has to be > 2
"z"  # L has to be even
</pre>