# Chapter 5 Assignments

## Ch05-01
1. Write a Python program that reads 10 integers and then finds and prints the sum of the even and off integers.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use a while loop to calculate.  Allow the user to repeat the program (use a while loop).

\*************************************************************************************

OUTPUT:

&ndash; The bold text is the user's input.

\*************************************************************************************
<pre>
Please enter 10 integers: 
><b>1</b>
><b>2</b>
><b>3</b>
><b>4</b>
><b>5</b>
><b>6</b>
><b>7</b>
><b>8</b>
><b>9</b>
><b>10</b>

Even sum: 30
Odd sum: 25

Do you wish to repeat this program? (y/n)
><b>y</b>

Please enter 10 integers: 
><b>11</b>
><b>12</b>
><b>13</b>
><b>14</b>
><b>15</b>
><b>16</b>
><b>17</b>
><b>18</b>
><b>19</b>
><b>20</b>

Even sum: 80
Odd sum: 75

Do you wish to repeat this program? (y/n)
><b>n</b>

Done!
</pre>
\*************************************************************************************

## Ch05-02
1. Write a Python program that creates and stores a multiplication table in a list called **MT**, and then displays elements.  Do NOT create additional lists.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;To create a list called **MT**, use the following:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MT = [ ]**

<br />
<br />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use three while loops (counter-controlled):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use one while loop to add elemets to the **MT** list and set initial value to be **0**.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use another while loop to change elements (Do NOT set values manually, except the first row and first column).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use the other to display elements.

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