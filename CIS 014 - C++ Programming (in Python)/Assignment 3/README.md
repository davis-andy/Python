# Homework Assignments 3

## Homework 3.1
You can instantiate (create) a Python string on the stack like so:

<pre>
str = "babbaa"
</pre>

which consists of an array of 6 elements of type char:

<pre>
{'b','a','b','b','a','a'}
</pre>

You have a Python string of finite length consisting of only 'a' and 'b's in it. Write the following function to 
separate all of the 'a' and 'b' in the string so that all 'a' appear before 'b' in it:

<pre>
def separateLetters(inp: str) -> str:
</pre>

The above sorted string becomes, for example: 

<pre>
print(separateLetters("babbaa"))  # outputs "aaabbb"
</pre>

Examples:

Input: abbbbbbbbaaaaaaa

Output: aaaaaaaabbbbbbbb

<br />

Input: a

Output: a

<br />

Input: bb

Output: bb

<br />

Input: ab

Output: ab

<br />

Input: ba

Output: ab

<br />

**Constraints and Assumptions:**

* Input string is of finite size < 50.
* Input string cannot be empty or NULL.
* Input string only contains either 'a' or 'b' English lower-case alphabets, nothing else.
* Do NOT use any existing Python sorting library for this problem (doing so will receive partial credits for logic)

## Homework 3.2
What do you do with a pile of pebbles (little rocks)? You and your friend decide to play a game to remove these 
pebbles, one or several at a time, to prove that one of you is the Ultimate Strategist at PCC.

The game rules are:

* You go first when the game starts (that is, you pick your game-winning move first)
* You and your friend take turns to remove the rest
* Each of you can remove 1 to 4 pebbles at each turn
* The one who removes the last pebble will be the winner

Write the following function, CanIAlwaysWin(n: int), to see if you are always the winner given n as your starting 
quantity of pebbles.

<pre>
def CanIAlwaysWin(n: int) -> bool: 
</pre>

For example:

* n <= 4 returns true, you are the winner (since you can remove all 4 at once leaving your friend with none)
* n = 5 returns false, you lose (no matter you remove 1, 2, 3, or 4 pebbles the last pebble will always be your 
friend's to remove)
* n = 6, n = 7, etc., what do you think?

*NOTE: you WON'T need to write a game asking two users to take turns inputting numbers. Instead, you need to 
implement the CanIAlwaysWin() function by returning either a true or false value. Your main() function may look like:*

<pre>
def main():
   n = int(input("Enter a number: "))
   print(f'Can I win: {CanIAlwaysWin(n)}')
</pre>

**Constraints and Assumptions:**

* n is always positive > 0
* n is an integer less than INT_MAX.
* This problem tests your use of basic human logics and pattern matching. 
* You will implement your CanIAlwaysWin function which will be called from your console's main().
* HINT: let's say n = 9, how many pebbles do you have to remove first to ensure your winning chance is 100%? Sure, 
you can remove **1** first, but that will leave you to win or lose depending on what your opponent's move is next. So 
removing 1 is not the key. How about removing 4 first? Will that guarantee your win?