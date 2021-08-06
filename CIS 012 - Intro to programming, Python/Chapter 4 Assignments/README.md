# Chapter 4 Assignments

## Ch04-01
1. Write a value-returning function, **isVowel**, that returns the value **True** if a given character is a vowel and otherwise returns **False**.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\***__Be sure to allow the users to use lowercase as well as uppercase letters.__

\*************************************************************************************

OUTPUT:

&ndash; The bold text is the user's input.

\*************************************************************************************
<pre>
Enter a character between a and z (or A and Z): <b>a</b>

a is a vowel: True.
</pre>
\*************************************************************************************
<pre>
Enter a character between a and z (or A and Z): <b>E</b>

E is a vowel: True.
</pre>
\*************************************************************************************
<pre>
Enter a character between a and z (or A and Z): <b>B</b>

B is a vowel: False.
</pre>
\*************************************************************************************
<pre>
Enter a character between a and z (or A and Z): <b>b</b>

b is a vowel: False.
</pre>
\*************************************************************************************

## Ch04-02
1. Write a Python program that accepts a year written as a four-digit Arabic (ordinary) numberal and outputs the year written in Roman numbers.


**Important**:

Roman numerals are V for 5, X for 10, L for 50, C for 100, D for 500, and M for 1,000.


Recall that some numbers are formed by using a kind of subtraction of one Roman "digit"; for example, IV is 4 produced as V minus I, XL is 40, CM is 900, and so on.


A few sample years: MCM is 1900, MCML is 1950, MCMLX is 1960, MCMXL is 1940, MCMLXXXIX is 1989.


(Hints: USe division and mod.)




Assume the year is between 1000 and 3000.



Define the following functions (value returning functions):

**returnRomanThousandsPlace()**: Accepts a thousands place integer number as an argument and returns the roman numerals for the thousands place.

**returnRomanHundredsPlace()**: Accepts a hundreds place integer number as an argument and returns the roman numerals for the hundreds place.

**returnRomanTensPlace()**: Accepts a tens place integer number as an argument and returns the roman numerals for the tens place.

**returnRomanOnesPlace()**: Accepts a ones place integer number as an argument and returns the roman numerals for the ones place.

\*************************************************************************************

OUTPUT:

&ndash; The bold text is the user's input.

\*************************************************************************************
<pre>
Enter a year between 1000 and 3000:
<b>1952</b>

Your number in roman numerals is: MCMLII.
</pre>
\*************************************************************************************
<pre>
Enter a year between 1000 and 3000:
<b>2048</b>

Your number in roman numerals is: MMXLVIII.
</pre>
\*************************************************************************************
<pre>
Enter a year between 1000 and 3000:
<b>2500</b>

Your number in roman numerals is: MMD.
</pre>
\*************************************************************************************

## Ch04-03
1. Write Python statements that output the example in the OUTPUT section.

\*************************************************************************************

OUTPUT:

&ndash; The bold text is the user's input.

\*************************************************************************************
<pre>
Enter your first name: <b>John</b>
Enter your pay rate per hour: <b>12.5</b>
Enter the number of hours you worked last week: <b>35.5<b>

First Name: John
Pay Rate: $12.5
Hours Worked: 35.5
Salary: $443.75
</pre>
\*************************************************************************************

## Ch04-04
1. Write a Python program prompts the user to input the elapsed time for an event in seconds.  The program then outputs the elapsed time in hours, minutes, and seconds.  Hint: use // and %

\*************************************************************************************

OUTPUT:

&ndash; The bold text is the user's input.

\*************************************************************************************
<pre>
Enter the elapsed time in seconds: <b>9630</b>

The elapsed time in seconds = 9630

The equivalent time in hours:minutes:seconds = 2:40:30
</pre>
\*************************************************************************************