# Homework Assignments 8

## Homework 8.1
**Reverse an integer:**

You will write a class CIS14 and implement its public member function, int reverseInt(int), to reverse an integer. Your 
program **MUST** include this CIS14 class declaration with its public member function **BEFORE** the placement of your 
main() function. Remember, no header file (.h files) is necessary:

<pre>
class CIS14 {
public:
   int reverseInt(int input);
};
</pre>

Member function to implement:

<pre>
int reverseInt(int input)
</pre>

<br />

Example #1: 

input: 14

returns: 41

<br />

Example #2: 

input: -14

returns:  -41

<br />

Example #3:

input: 10

returns:  1 

<br />

Example #4:

input: 1000

returns:  1 

<br />

**Constraints/Assumptions:**

* __int__ is equivalent to __signed int__ and there's a range of values; on most of your machines it's a 32-bit integer 
which means your __sizeof(int)__ should return 4
* Your input to reverseInt is always assumed to be in-range. It is the responsibility of the user of your reverseInt() 
function to make sure that the input doesn't overflow. This responsibility is out of scope for this problem. __So, input 
is assumed to be in-range.__
* Your function __returns 0 when the reversed integer overflows.__
* Your function input is an __int__, so inputs such as 01, 001, 002, etc., are not possible
* Your function output is also an __int__, so outputs such as 001, 01, 021, are not possible. You have to convert those 
into 1, 1, 21, etc respectively. See __Hints__ below.

<br />

**Hints:**

* Did you notice that the reversed integer might overflow, namely go outside of the 32-bit integer range? For example 
if your input is 1000000119  its reverse will not be acceptable
* Overflow is NOT the same as overload. See http://www.cplusplus.com/reference/climits/ on INT_MAX
* If the integer's last digit is 0, what should the output be? For example cases such as 10, 100, etc. For this 
problem, 01 is equivalent to 1, 001 is 1, and so on.
 
<pre>
/*
 * EXAMPLE (you may choose to have your own implementation style in main())
 */
int main() {
   // instantiate an instance of CIS14 class
   CIS14 cis14;

   // invoke this instance's member function one  by one
   cout << cis14.reverseInt(1) << endl;
   cout << cis14.reverseInt(123) << endl;
   ...
   return 0;
}
</pre>

## Homework 8.2
**Converts a string to an integer.**

Write the following function:

<pre>
int convertString2Integer(string str)
</pre>

Example #1:

str: "123"

return: 123

<br />

Example #2:

str: "-123"

return: -123

<br />

Example #3:

str: "0000012"

return: 12

<br />

**Constraints/Assumptions:** 

* This problem **WON'T** require you to check for integer overflow. Your output is always assumed in-range (<= INT_MAX).
* Your string input **CANNOT** be empty or NULL.
* Your string input should **ONLY** contain '0' - '9' digit(s), and/or a negative sign ('-'); there are no other ASCII 
characters.
* Your string input **CAN** have leading zeros, namely "01", "0000000000000124", etc; in which case your function 
should return 1, 124, etc.
* You **CANNOT** use any string-to-integer library functions (namely atoi(), stoi(), stringstream(), etc.) for this 
problem.

<pre>
/*
 * EXAMPLE (you may choose to have your own implementation style in main())
 */
int main() {
  cout << convertString2Integer("123");
  cout << convertString2Integer("-999");
  ...
  return 0;
}
</pre>

## Homework 8.3
Lego inspires and develops the builders of tomorrow. An example of a 2-by-4 lego brick looks like the following:

You have a set of them, each with a varying height denominations (in red): 2x4x1, 2x4x4, 2x4x8, etc. You are asked to 
build a wall of a certain target height using an unlimited supply of these bricks. Write a function to output the 
number of possible ways (namely, total combination) you can use these bricks to build up a wall of target_height. For 
the sake of illustration, these heights are unit-less; they are relative to the size of 2x4):

```
int getLegoCombinations(vector<int> &lego_heights, int target_height)
```

**Examples:**

input: {1,2,5}, 3

output: 2

Explanation: you have 3 lego bricks of height 1, 2, and 5, respectively. You are asked to build a wall of height 3. 
There are 2 ways (output) to accomplish this by stacking up your bricks like this: {1,1,1}, {1,2}. Note the piece with 
height 5 is never used because its use is not possible.

<br />

input: {1,2,5}, 0

output: 0

Explanation: there is nothing to build (target height of 0), hence returning 0.

<br />

input: {1,2,5}, 7

output: 6

Explanation: there are 6 possible ways as follows:

{1,1,1,1,1,1,1}

{1,1,1,1,1,2}

{1,1,1,2,2}

{1,2,2,2}

{1,1,5}

{2,5}

<br />

input: {5}, 9

output: 0

Explanation: height denomination provided can never reach 9, hence returning 0.

<br />

**Constraints / Assumptions:**

* Input vector with integral denominations of lego_heights is never empty.
* 0 <= target_height <= INT_MAX.
* lego_height is always integral and >= 1.
* Your lego supply (of indicated denominations) is unlimited.
* HINT: this solution calls for Dynamic Programming. Given an integer array, solutions,  where solutions[target_height] 
* is the total combination at the target height, your answer should be obtained via solutions[target_height - height#1] 
+ solutions[target_height - height#2] + solutions[target_height - height#3] + ....