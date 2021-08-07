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


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Important**:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Roman numerals are V for 5, X for 10, L for 50, C for 100, D for 500, and M for 1,000.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Recall that some numbers are formed by using a kind of subtraction of one Roman "digit"; for example, IV is 4 produced as V minus I, XL is 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;40, CM is 900, and so on.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A few sample years: MCM is 1900, MCML is 1950, MCMLX is 1960, MCMXL is 1940, MCMLXXXIX is 1989.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(Hints: Use division and mod.)

<br></br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Assume the year is between 1000 and 3000.

<br></br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Define the following functions (value returning functions):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**returnRomanThousandsPlace()**: Accepts a thousands place integer number as an argument and returns the roman numerals for the
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;thousands place.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**returnRomanHundredsPlace()**: Accepts a hundreds place integer number as an argument and returns the roman numerals for the
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hundreds place.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**returnRomanTensPlace()**: Accepts a tens place integer number as an argument and returns the roman numerals for the tens place.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**returnRomanOnesPlace()**: Accepts a ones place integer number as an argument and returns the roman numerals for the ones place.

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
1. Create a Python module called **RPSMod.py**, and define new functions (see #2) in the **RPSMod.py** (contains user-defined functions only); do NOT include an code calling the user defined functions.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\***__Do NOT include any user-defined functions in *Assignment_Ch04-03_yourLastName.py* file__

2. Write a Python program to score the paper-rock-scissor game; user vs. computer.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The user types in either (**P** or **p**), (**R** or **r**), or (**S** or **s**).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Computer randomly generates either (**P** or **p**), (**R** or **r**), or (**S** or **s**).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The program then announces the winner as well as the basis for determining the winner:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Paper covers rock,

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Rock smashes scissors,

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Scissors cut paper,

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;or Tie!.

<br></br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\***__Computer generate only integer values.  Do NOT use a list.__

<br></br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Define the following functions (value returning functions):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**collectStringInput()**: Accepts no arguments, collect a string value from the user, and returns the collected string value: (**P** or **p**), (**R** or **r**), or (**S** 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;or **s**).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**generateIntegerValue()**: Accepts no arguments, randomly generates an integer number, and returns the generated integer number.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**convertIntegerToRPS()**: Accepts the integer number generated by **generateIntegerValue()** as an argument and returns a string value: (**P** or 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**p**), (**R** or **r**), or (**S** or **s**).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**evaluateWinning()**: Accepts the value returned by **collectStringInput()** as an argument and the value returned by **convertIntegerToRPS()** 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;and returns a string calue (announces the winner).

\*************************************************************************************

OUTPUT:

&ndash; The bold text is the user's input.

\*************************************************************************************
<pre>
Enter [R]ock, [P]aper, or [S]cissor
Player: <b>p</b>

Computer's selection: s

Scissor cuts paper.
Computer WINS!
</pre>
\*************************************************************************************
<pre>
Enter [R]ock, [P]aper, or [S]cissor
Player: <b>p</b>

Computer's selection: s

Scissor cuts paper.
Computer WINS!
</pre>
\*************************************************************************************
<pre>
Enter [R]ock, [P]aper, or [S]cissor
Player: <b>p</b>

Computer's selection: p

Tie!
</pre>
\*************************************************************************************

## Ch04-04
1. Write a Python program that computes the cost of a long-distance call.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The cost of the call is determined according to the following rate schedule:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a. Any call started between 8:00 A.M. and 6:00 P.M., Monday through Friday, is billed at a rate of $0.40 per minute.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b. Any call starting before 8:00 A.M. or after 6:00 P.M., Monday through Friday, is charged at a rate of $0.25 per minute.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;c. Any call started on a Saturday or Sunday is charged at a rate of $0.15 per minute.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The input will consist of the day of the week, the time the call started, and the length of the call in minutes.  The output will be the cost of 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;the call.  The time is to be input in 24-hour notation, so the time 1:30 P.M. is input as (must be the following format, the user types in the 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;colon): \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**13:30**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The day of the week will be read as one of following pairs of character values: \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Mo Tu We Th Fr Sa Su**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Be sure to allow the user to use either uppercase or lowercase letters or a combination of the two.  The number of minutes will be input as a 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value of integer.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Format your output to two decimal places.

<br />
<br />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Define the following function (value returning function):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**calculateTotalCost()**: Accepts arguments (hour, minute, day, call length), calculate the total cost of a call, and returns the total cost (float).

<br />
<br />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\***__Be sure to allow the user to use lowercase as well as uppercase letters.__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\***__Do NOT use lists.__

\*************************************************************************************

OUTPUT:

&ndash; The bold text is the user's input.

\*************************************************************************************
<pre>
Enter the time the call starts in 24-hour rotation:
<b>13:10</b>

Enter the first two letters of the day of the week:
<b>Mo</b>

Enter the length of the call in minutes:
<b>10</b>

Cost of the call: $4.00
</pre>
\*************************************************************************************
<pre>
Enter the time the call starts in 24-hour rotation:
<b>20:10</b>

Enter the first two letters of the day of the week:
<b>fR</b>

Enter the length of the call in minutes:
<b>10</b>

Cost of the call: $2.50
</pre>
\*************************************************************************************
<pre>
Enter the time the call starts in 24-hour rotation:
<b>10:10</b>

Enter the first two letters of the day of the week:
<b>su</b>

Enter the length of the call in minutes:
<b>10</b>

Cost of the call: $1.50
</pre>
\*************************************************************************************