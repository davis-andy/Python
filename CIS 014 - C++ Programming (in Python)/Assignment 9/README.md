# Homework Assignments 9

## Homework 9.1 (in progress)
**You are the owner of this "PCC Sign" store that sells signs including individual letters made of plastic that 
customers would buy to put on their mailboxes such as the "5793 Dowling" street address**

Your shop is so popular everyone in town comes to your store to buy sign letters. But your inventory of plastic 
letters is limited. Sometimes you have them in stock. Sometimes you don't.

You will write a class to automatically determine whether a set of mailbox signs (or street addresses) is possible 
given your available plastic letter inventory in the store. Your console program **MUST** include this class 
declaration with the member function: 

<pre>
class CIS14:
    def getNumPossibleSigns(letterInventory: str, addresses: list, length: int) -> int:
</pre>

In addition the member function documentation is as follows: 

<pre>
/**
 * MEMBER FUNCTION NAME: 
 *    getNumPossibleSigns
 * PURPOSE: 
 *    The function takes in a series of addresses in a string array and compares each of them with the available 
 *    letterInventory, returning the number of addresses that are POSSIBLE to form from the given letterInventory
 * PARAMETER:
 *    letterInventory: str
 *    addresses: list
 *    length: length of the list, addresses
 * RETURN VALUE:
 *    int: the number of possible addresses that can be formed from your inventory of letters
 */
</pre>
 
Note the length parameter in the function. Assuming your addresses[] is as follows:

<pre>
addresses = ["S1","S2","S3"] 
</pre>

Then you may obtain the length of your Python string array using the len():

<pre>
length = len(addresses)
</pre>

<br />

**Example #1:**

"AAAABCCC123456789"

["123C","123A","123 ADA"]

Returns: 2

Only two of these can be formed. The space in "123 ADA" can never be a problem, and collection contains two 'A's. We 
only consider one address at a time so it doesn't matter that we cannot form both "123C" and "123A" at the same time 
from this collection. The two possible signs that can be formed from this collection are "123C", "123A"

<br /> 

**Example #2:** 

"ABCDEFGHIJKLMNORSTUVWXYZ1234567890"

["2 FIRST ST"," 13 PUN ST", "101 AKER"]

Returns: 0

We cannot form any of these. The first address requires two 'S's, the second address requires a 'P', and the third 
address requires two '1's.

<br /> 

**Example #3:**

"ABCDAAST"

["999 S ST", "A BAD ST", "B BAD ST"]

Returns: 1

"999 S ST" cannot be formed since collection does not contain any digits. "B BAD ST" cannot be formed because it 
requires 2 'B's.

<br />

**Constraints and Assumptions:**

* __letterInventory__ contains between 1 and 50 characters inclusive
* __letterInventory__ doesn't contain space character, '&nbsp;&nbsp;&nbsp;'
* Each character in the __letterInventory__ will be an uppercase letter 'A'-'Z' or a digit '0'-'9'
* Comparison doesn't include space '&nbsp;&nbsp;&nbsp;'
* __addresses__ contains between 1 and 50 elements inclusive
* Each address contains between 1 and 50 characters inclusive
* Each character in each address will be an uppercase letter 'A'-'Z' or a digit '0'-'9'or a space '&nbsp;&nbsp;&nbsp;'

## Homework 9.2 (in progress)
You are given an input string and a dictionary of English words. You are asked to see if the input is consisted 
of words only in the dictionary. For example:

<br />

**Example #1**
Input string ="joe";
Input dictionary =["joe1", "joe" ];
Output: true
Explanation: "joe" is in the dictionary.
 
<br />

**Example #2**
Input string ="joey";
Input dictionary =["joe1", "joe" ];
Output: false
Explanation: even though "joe" is in the dictionary, "y" is not.

<br /> 

**Example #3**
Input string ="applepie";
Input dictionary =["pie", "apple" ];
Output: true
Explanation: "apple" and "pie" are both in the dictionary. 

<br /> 

**Example #4**
Input string ="hellonow";
Input dictionary =["hello", "on", "hell", "now" ];
Output: true
Explanation: "hello" and "now" are both in the dictionary. 
 
<br />

**Example #5**
Input string ="hellonowl";
Input dictionary =["hell", "on", "owl" ];
Output: true
Explanation: "hell", "on", and "owl" are all in the dictionary. 
 

Implement the following class method that takes the input string and a dictionary of English words, and checks to see 
if the given input is composed of only the words from the input dictionary:

```
class CIS14:
   def isInputInDictionary(s: str, dic: dict) -> bool:
```
<br />

**Constraints / Assumptions:**

* The input string cannot be NULL.
* The input dictionary cannot be NULL; it has at least one English words.
* The method takes a pointer to the input string.
* The method takes a reference of the input dictionary.
* HINT: this solution calls for recursion.