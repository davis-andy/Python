# CIS 112 Assignments

## Assignment 1
Write a Python program to find out number of days in a month.  Your program will ask user to enter month and year and display number of days of that month.

1.  Need to figure out whether the years is a leap year or not.

2.  Depends on the result of the step 1, number of days for Feb. will be different.

 

Use functions (finding leap year, finding days in a month).

After producing the output, ask users whether to repeat it or not.  If user wants to repeat, ask year and month again and produce the output.  Repeat it until user wants to stop.

Make sure you have comments in your program.


\======================================

Sample output

\======================================

Please enter the 4 digit year: 1969
Please enter the month: 2
Year 1969 Month 2 has 28 days in a month
Do you want to repeat? (Y/N)y


Please enter the 4 digit year: 2020
Please enter the month: 2
Year 2020 Month 2 has 29 days in a month
Do you want to repeat? (Y/N)n


Thank you for playing!
>>>

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
Alpha after initialization:
0    0    0    0    0    0    0    0    0    0    
0    0    0    0    0    0    0    0    0    0


Enter 20 integers:
<b>1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20</b>


Alpha after reading 20 numbers:
1    2    3    4    5    6    7    8    9    10
11   12   13   14   15   16   17   18   19   20


Beta after a call to doubleArray:
2    4    6    8    10   12   14   16   18   20 
22   24   26   28   30   32   34   36   38   40


inStock after a call to copyGamma:
11      13      15      17
33      39      45      51
99      117     135     153
297     351     405     459
891     1053    1215    1377
2673    3159    3645    4131
8019    9477    10935   12393
24057   28431   32805   37179
72171   85293   98415   111537
216513  255879  295245  334611


inStock after a call to copyAlphaBeta:
1    2    3    4
5    6    7    8
9    10   11   12
13   14   15   16
17   18   19   20
2    4    6    8
10   12   14   16
18   20   22   24
26   28   30   32
34   36   38   40


Enter 10 integers:
<b>21
22
23
24
25
26
27
28
29
30</b>


inStock after a call to setInStock:
21   39   75   147
22   39   73   141
23   44   86   170
24   42   78   150
25   40   70   130
26   43   77   145
27   47   87   167
28   45   79   147
29   57   113  225
30   52   96   184
</pre>
\*************************************************************************************