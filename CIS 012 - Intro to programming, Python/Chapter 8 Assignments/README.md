# Chapter 8 Assignments

## Ch08-01
1. Write a Python program that computes the cost of a long-distance call.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The cost of the call is determined according to the following rate schedule:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a. Any call started between 8:00 A.M. and 6:00 P.M., Monday through Friday, is billed at a rate of $0.40 per minute.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b. Any call starting before 8:00 A.M. or after 6:00 P.M., Monday through Friday, is charged at a rate of $0.25 per minute.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;c. Any call started on a Saturday or Sunday is charged at a rate of $0.15 per minute.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The input will consist of the day of the week, the time the call started, and the length of the call in minutes.  The output will be the cost of 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;the call.  The time is to be input in 24-hour notation, so the time 1:30 P.M. is input as (must be the following format, the user types in the 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;colon): \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**13:30**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The day of the week will be read as one of following pairs of character values, which are stored in two variables of type string (ex. a, b = \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"Mo"): \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Mo Tu We Th Fr Sa Su**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Be sure to allow the user to use either uppercase or lowercase letters or a combination of the two.  The number of minutes will be input as a 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value of integer.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Format your output to two decimal places.

<br />
<br />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Define the following lists and fill the lists using the two functions (**createList()** and **fillList()**):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calling the functions (copy the following statements into your program):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**hoursList = createList(24)**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**fillList(24, hoursList)**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**minutesList = createList(60)**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**fillList(60, minutesList)**

<br />

```
hoursList  = [0, 1, 2, .........., 22, 23]

minutesList = [0, 1, 2, .........., 58, 59]
```

<br />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Define the following lists and fill the lists manually (copy the following code and paste into your program):

<br />

```
daysList = ['mo', 'tu', 'we', 'th', 'fr', 'sa', 'su']

responseList = ['y', 'n']
```

<br />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Define the following functions:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**createList(listSize)**: accepts a **listSize** as an argument, create a 1-D list called **timeList** with the **listSize** (initial values: zeros), and returns the \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**timeList** list.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**fillList(listSize, timeList)**: accepts a **listSize** and the list returned by **createList()** as arfuments, and fill the passed list.  This is a void function.

<br />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**collectUserInputTime()**: accepts no arguments, collects call starting time in 24-hour notation, and returns **startHour** and **startMinute** as \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string data type.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**validateUserInputTime(startHour, startMinute)**: accepts the **startHour** and **startMinute** returned by **collectUserInputTime()** as arguments, \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;validates the user's time input by comparing to the lists called **hoursList** and **minutesList**, and returns **True**, **startHour** (integer), **startMinute** \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(integer) if the input is valid, or **False** if the input is invalid.

<br />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**collectUserInputDay()**: accepts no arguments, collects a day (two characters) save as **firstDayCharacter** and **secondDayCharacter**, and \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;returns **firstDayCharacter** and **secondDayCharacter** as string data type.  Allow uppercase and lowercase input (ex. MO, Mo, mo, and mO).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**validateUserInputDay(firstDayCharacter, secondDayCharacter)**: accepts the **firstDayCharacter** and **secondDayCharacter** returned by \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**collectUserInputDay()**, validates the user's day input by comparing to the input to the **dayList** list, and returns **True** if the input is valid, or \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**False** if the input is invalid.

<br />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**collectUserInputCallLength()**: accepts no arguments, collects call length in 24-hour notation, and returns **callLengthHour** and \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**callLengthMinute** as string data type.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**validateUserInputCallLength(callLengthHour, callLengthMinute)**: accepts the **callLengthHour** and **callLengthMinute** as arguments \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;returned by **collectUserInputCallLength()**, validates the user's call length input (**callLengthHour** and **callLengthMinute** should be greater \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;than or equal to zero), and returns **True**, **callLengthHour** (integer), **callLengthMinute** (integer) if the input is valid, or **False** if the input is \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;invalid.

<br />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**calculateTotalCost(startHour, startMinute, firstDayCharacter, secondDayCharacter, callLengthHour, callLengthMinute)**: accepts \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;arguments (startHour, startMinute, firstDayCharacter, secondDayCharacter, callLengthHour, callLengthMinute), calculate the total cost of a \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;call, and returns the total cost (float).

<br />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**collectUserInputYesNo()**: accepts no arguments, collects 'y' or 'n' save as **YesOrNo**, and returns **YesOrNo** as string data type.  Allow \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uppercase and lowercase input (ex. Y, y, N, n).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**validateUserInputYesNo(YesOrNo)**: accepts **YesOrNo** as an argument returned by **collectUserInputYesNo()**, validates the user's input by \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comparing the input to the **responseList** list, and returns **True** if the input is valid, or **False** if the input is invalid.

<br />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**clearPreviousOutput(YesOrNo)**: accepts **YesOrNo**.  If the response is 'y' or 'Y', then clear the previous output, otherwise doesn't clear the \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pervious output.

<br />
<br />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\***__Be sure to allow the user to type lowercase as well as uppercase letters.__

\*************************************************************************************

OUTPUT:

&ndash; The bold text is the user's input.

\*************************************************************************************
<pre>
Enter the time the call starts in 24-hour rotation:
<b>-13:10</b>

Invalid time input.
Please try again.

Enter the time the call starts in 24-hour rotation:
</pre>
\*************************************************************************************
<pre>
Enter the time the call starts in 24-hour rotation:
<b>a:77</b>

Invalid time input.
Please try again.

Enter the time the call starts in 24-hour rotation:
</pre>
\*************************************************************************************
<pre>
Enter the time the call starts in 24-hour rotation:
<b>13:10</b>

Enter the first two letters of the day of the week:
<b>ss</b>

Invalid day input.
Please try again.

Enter the first two letters of the day of the week:
</pre>
\*************************************************************************************
<pre>
Enter the time the call starts in 24-hour rotation:
<b>13:10</b>

Enter the first two letters of the day of the week:
<b>1s</b>

Invalid day input.
Please try again.

Enter the first two letters of the day of the week:
</pre>
\*************************************************************************************
<pre>
Enter the time the call starts in 24-hour rotation:
<b>13:10</b>

Enter the first two letters of the day of the week:
<b>Mo</b>

Enter the length of the call in (hours:minutes):
<b>-10:10</b>

Invalid call length input.
Please try again.

Enter the length of the call in (hours:minutes):
</pre>
\*************************************************************************************
<pre>
Enter the time the call starts in 24-hour rotation:
<b>13:10</b>

Enter the first two letters of the day of the week:
<b>Mo</b>

Enter the length of the call in (hours:minutes):
<b>a1:10</b>

Invalid call length input.
Please try again.

Enter the length of the call in (hours:minutes):
</pre>
\*************************************************************************************
<pre>
Enter the time the call starts in 24-hour rotation:
<b>13:10</b>

Enter the first two letters of the day of the week:
<b>Mo</b>

Enter the length of the call in (hours:minutes):
<b>0:10</b>

Cost of the call: $4.00


Do you want to repeat the program (y/n)?
>><b>y</b>
</pre>
\*************************************************************************************
<pre>
Enter the time the call starts in 24-hour rotation:
<b>20:10</b>

Enter the first two letters of the day of the week:
<b>Fr</b>

Enter the length of the call in (hours:minutes):
<b>0:10</b>

Cost of the call: $2.50


Do you want to repeat the program (y/n)?
>><b>yes</b>

Invalid response.
PLease try again.

Do you want to repeat the program (y/n)?
>><b>y</b>
</pre>
\*************************************************************************************
<pre>
Enter the time the call starts in 24-hour rotation:
<b>10:10</b>

Enter the first two letters of the day of the week:
<b>Su</b>

Enter the length of the call in (hours:minutes):
<b>1:40</b>

Cost of the call: $150.00


Do you want to repeat the program (y/n)?
>><b>n</b>
</pre>
\*************************************************************************************

## Ch08-02
1. Write a Python program that creates and stores a multiplication table in a 2D list called **MT**, and then displays elements.  Do NOT create additional lists.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;To create a empty list (2Dlist) called **MT**, use the following:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MT = [ ]**

<br />
<br />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use three while loops (counter-controlled) - no for loop:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use one while loop to add elemets to the **MT** list and set initial value to be **0**.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use another nested-while loop to change elements (Do NOT set values manually, except the first row and first column).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use the other (nested-while loop) to display elements.

\*************************************************************************************

OUTPUT:

&ndash; Use tab after displaying each number.

\*************************************************************************************
<pre>
Multiplication Table:
X      1      2      3      4      5      6      7      8      9      10
1      1      2      3      4      5      6      7      8      9      10
2      2      4      6      8      10     12     14     16     18     20
3      3      6      9      12     15     18     21     24     27     30
4      4      8      12     16     20     24     28     32     36     40
5      5      10     15     20     25     30     35     40     45     50
6      6      12     18     24     30     36     42     48     54     60
7      7      14     21     28     35     42     49     56     63     70
8      8      16     24     32     40     48     56     64     72     80
9      9      18     27     36     45     54     63     72     81     90
10     10     20     30     40     50     60     70     80     90     100
</pre>
\*************************************************************************************

## Ch08-03
1. Write a Python program that test the function mand the functions discussed in parts a through g.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Create the following lists:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**inStock** - 2D (row size: 10, column size: 4).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**alpha** - 1D list with 20 elements.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**beta** - 1D list with 20 elements.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**gamma** = [11, 13, 15, 17]

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**delta** = [3, 5, 2, 6, 10, 9, 7, 11, 1, 8]

<br />
<br />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a. Write the definition of the function **setZero** that initializes any one-dimensional list to 0 (**aplha** and **beta**).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b. Write the definition of the function **inputArray** that prompts the user to input 20 numbers and stores the numbers into **alpha**.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;c. Write the definition of the funciton **doubleArray** that initializes the elemets of **beta** to two times the corresponding elements in **alpha**.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;d. Write the definition of the function **copyGamma** that sets the elements of the first row of **inStock** from **gamma** and the remaining rows \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;of **inStock** to three times the previous row of **inStock**.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e. Write the definition of the function **copyAlphaBeta** that stores **alpha** into the first five rows of **inStock** and **beta** into the last five rows of \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**inStock**.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;f. Write the definition of the function **printArray** that prints any one-dimentionsl list.  The funciton must contain only one loop to print any \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;one-dimensional list.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;g. Write the definition of the function **inStock** that prompts the user to input the elements for the first column of **inStock**.  The function \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;should then set the elements in the remaingin columns to two times the corresponding element in the previous column, minues the \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;corresponding element in **delta**.

\*************************************************************************************

OUTPUT:

&ndash; The bold text is the user's input.

&ndash; Use tab after displaying each number.

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