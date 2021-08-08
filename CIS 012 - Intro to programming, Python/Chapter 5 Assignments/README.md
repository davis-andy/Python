# Chapter 5 Assignments

## Ch05-01
1. Write a Python program that reads 10 integers and then finds and prints the sum of the even and off integers.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use a while loop to calculate.  Allow the user to repeat the program (use a while 
loop).

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
1. Write a Python program that creates and stores a multiplication table in a list called **MT**, and then displays 
elements.  Do NOT create additional lists.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;To create a list called **MT**, use the following:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MT = [ ]**

<br />
<br />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use three while loops (counter-controlled):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use one while loop to add elemets to the **MT** list and set initial value to be 
**0**.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use another while loop to change elements (Do NOT set values manually, except the 
first row and first column).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use the other to display elements.

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

## Ch05-03
1. Create a program that uses **while** loops to perform the following steps.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a. Prompt the user to input two positive integers (no zero or negative). \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;variables: **firstNum** and **secondNum** (**firstNum** must be less 
than **secondNum**).  Validate the user's input; prompt the user again if \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**firstNum** is not less than **secondNum** (use while loop).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b. Output all odd numbers between **firstNum** and **secondNum**. (use while loop).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;c. Output the sum of all even numbers between **firstNum** and **secondNum**. 
(use while loop).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;d. Output the sum of the square of the odd numbers between **firstNum** and 
**secondNum**. (use while loop).

<br />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Program layout for each step:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#A

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;while loop

<br />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#B

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;while loop

<br />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#C

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;while loop

<br />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#D

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;while loop

<br />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\***__Allow the user to repeat the program. (requires another while loop).__

\*************************************************************************************

OUTPUT:

&ndash; The bold text is the user's input.

\*************************************************************************************
<pre>
Enter two positive integer numbers.
First number must be less than the second number:
Enter numbers:  <b>8 a</b>

Incorrect Input.
Please try again.

Enter two positive integer numbers.
First number must be less than the second number:
Enter numbers:
</pre>
\*************************************************************************************
<pre>
Enter two positive integer numbers.
First number must be less than the second number:
Enter numbers:  <b>a 8</b>

Incorrect Input.
Please try again.

Enter two positive integer numbers.
First number must be less than the second number:
Enter numbers:
</pre>
\*************************************************************************************
<pre>
Enter two positive integer numbers.
First number must be less than the second number:
Enter numbers:  <b>8 2</b>

First number must be less than the second number!
Please try again.

Enter two positive integer numbers.
First number must be less than the second number:
Enter numbers:
</pre>
\*************************************************************************************
<pre>
Enter two positive integer numbers.
First number must be less than the second number:
Enter numbers:  <b>-2 8</b>

No negative numbers!
Please try again.

Enter two positive integer numbers.
First number must be less than the second number:
Enter numbers:
</pre>
\*************************************************************************************
<pre>
Enter two positive integer numbers.
First number must be less than the second number:
Enter numbers:  <b>2 8</b>

Odd integers between <b>2</b> and <b>8</b> are:
3 5 7

Sum of even integers between <b>2</b> and <b>8</b> = 20

Sum of the squares of odd integers between <b>2</b> and <b>8</b> = 83


Do you want to repeat the program?
y/n
> <b>y</b>
</pre>
\*************************************************************************************
<pre>
Enter two positive integer numbers.
First number must be less than the second number:
Enter numbers:  <b>1 9</b>

Odd integers between <b>1</b> and <b>9</b> are:
1 3 5 7 9

Sum of even integers between <b>1</b> and <b>9</b> = 20

Sum of the squares of odd integers between <b>1</b> and <b>9</b> = 165


Do you want to repeat the program?
y/n
> <b>y</b>
</pre>
\*************************************************************************************
<pre>
Enter two positive integer numbers.
First number must be less than the second number:
Enter numbers:  <b>11 15</b>

Odd integers between <b>11</b> and <b>15</b> are:
11 13 15

Sum of even integers between <b>11</b> and <b>15</b> = 26

Sum of the squares of odd integers between <b>11</b> and <b>15</b> = 515


Do you want to repeat the program?
y/n
> <b>n</b>

Bye!
</pre>
\*************************************************************************************

## Ch05-04
1. Create a program that uses **for** loops to perform the following steps.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a. Prompt the user to input two positive integers (no zero or negative). \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;variables: **firstNum** and **secondNum** (**firstNum** must be 
less than **secondNum**).  Validate the user's input; prompt the user again if \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**firstNum** is not less than **secondNum** (use for loop).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b. Output all odd numbers between **firstNum** and **secondNum**. (use for loop).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;c. Output the sum of all even numbers between **firstNum** and **secondNum**. 
(use for loop).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;d. Output the sum of the square of the odd numbers between **firstNum** and 
**secondNum**. (use for loop).

<br />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Program layout for each step:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#A

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for loop

<br />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#B

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for loop

<br />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#C

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for loop

<br />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#D

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for loop

<br />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\***__Allow the user to repeat the program. (requires another for loop).__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\***__Do NOT use lists.__

\*************************************************************************************

OUTPUT:

&ndash; The bold text is the user's input.

\*************************************************************************************
<pre>
Enter two positive integer numbers.
First number must be less than the second number:
Enter numbers:  <b>8 a</b>

Incorrect Input.
Please try again.

Enter two positive integer numbers.
First number must be less than the second number:
Enter numbers:
</pre>
\*************************************************************************************
<pre>
Enter two positive integer numbers.
First number must be less than the second number:
Enter numbers:  <b>a 8</b>

Incorrect Input.
Please try again.

Enter two positive integer numbers.
First number must be less than the second number:
Enter numbers:
</pre>
\*************************************************************************************
<pre>
Enter two positive integer numbers.
First number must be less than the second number:
Enter numbers:  <b>8 2</b>

First number must be less than the second number!
Please try again.

Enter two positive integer numbers.
First number must be less than the second number:
Enter numbers:
</pre>
\*************************************************************************************
<pre>
Enter two positive integer numbers.
First number must be less than the second number:
Enter numbers:  <b>-2 8</b>

No negative numbers!
Please try again.

Enter two positive integer numbers.
First number must be less than the second number:
Enter numbers:
</pre>
\*************************************************************************************
<pre>
Enter two positive integer numbers.
First number must be less than the second number:
Enter numbers:  <b>2 8</b>

Odd integers between <b>2</b> and <b>8</b> are:
3 5 7

Sum of even integers between <b>2</b> and <b>8</b> = 20

Sum of the squares of odd integers between <b>2</b> and <b>8</b> = 83


Do you want to repeat the program?
y/n
> <b>y</b>
</pre>
\*************************************************************************************
<pre>
Enter two positive integer numbers.
First number must be less than the second number:
Enter numbers:  <b>1 9</b>

Odd integers between <b>1</b> and <b>9</b> are:
1 3 5 7 9

Sum of even integers between <b>1</b> and <b>9</b> = 20

Sum of the squares of odd integers between <b>1</b> and <b>9</b> = 165


Do you want to repeat the program?
y/n
> <b>y</b>
</pre>
\*************************************************************************************
<pre>
Enter two positive integer numbers.
First number must be less than the second number:
Enter numbers:  <b>11 15</b>

Odd integers between <b>11</b> and <b>15</b> are:
11 13 15

Sum of even integers between <b>11</b> and <b>15</b> = 26

Sum of the squares of odd integers between <b>11</b> and <b>15</b> = 515


Do you want to repeat the program?
y/n
> <b>n</b>

Bye!
</pre>
\*************************************************************************************

## Ch05-05
1. Create a program that uses **while** loops to perform the following steps.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a. Create a user-defined function called **validateUserInput()** to prompt the 
user to input two positive integers and validate the user's input. \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**validateUserInput()** is a value returning function; doesn't accept 
any arguments and returns **firstNum** and **secondNum**. \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Variables: **firstNum** and **secondNum** (**firstNume** must be less 
than **secondNum**). (use while loop to calidate and repeat).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b. Create a user-defined function called **oddNumbers()** to output all odd 
numbers between **firstNum** and **secondNum** (use while loop). \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**oddNumbers()** is a void function; accepts **firstNum** and 
**secondNum** as arguments and doesn't return any values.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;c. Create a user-defined function called **sumEvenNumbers()** to output the sum 
of all even numbers between **firstNum** and **secondNum**  \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(use while loop).  **sumEvenNumbers()** is a value returning 
function; accepts **firstNum** and **secondNum** as arguments and returns the sum \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;of all even numbers.  Declare a variable called **sumEven** in the 
**main()** to store the returned value by **sumEvenNumbers()**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;d. Create a user-defined function called **sumSquareOddNumbers()** to output the 
sum of the square of the odd numbers between **firstNum** \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;and **secondNum** (use while loop).  **sumSquareOddNumbers()** is a 
value returning function; accepts **firstNum** and **secondNum** as \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;arguments and returns the sum of the square of the odd numbers.  
Declare a variable called **sumSquareOdd** in the **main()** to store the \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;returned value by **sumSquareOddNumbers()**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e. Create a user-defined function called **main()** to repeat a program (use 
while loop) and execute the user-defined functions; \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**validateUserInput()**, **oddNumbers()**, **sumEvenNumbers()**, 
and **sumSquareOddNumbers()**.  **main()** is a void function; doesn't accept any \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;arguments.

<br />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Program layout for each step:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#A

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**validateUserInput()**

<br />
<br />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#B

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**oddNumbers()**

<br />
<br />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#C

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**sumEvenNumbers()**

<br />
<br />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#D

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**sumSquareOddNumbers()**

<br />
<br />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#E

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**main()**

<br />
<br />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#Executing Program.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;main()

<br />
<br />

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\***__Allow the user to repeat the program. (requires another while loop).__

\*************************************************************************************

OUTPUT:

&ndash; The bold text is the user's input.

\*************************************************************************************
<pre>
Enter two positive integer numbers.
First number must be less than the second number:
Enter numbers:  <b>8 a</b>

Incorrect Input.
Please try again.

Enter two positive integer numbers.
First number must be less than the second number:
Enter numbers:
</pre>
\*************************************************************************************
<pre>
Enter two positive integer numbers.
First number must be less than the second number:
Enter numbers:  <b>a 8</b>

Incorrect Input.
Please try again.

Enter two positive integer numbers.
First number must be less than the second number:
Enter numbers:
</pre>
\*************************************************************************************
<pre>
Enter two positive integer numbers.
First number must be less than the second number:
Enter numbers:  <b>8 2</b>

First number must be less than the second number!
Please try again.

Enter two positive integer numbers.
First number must be less than the second number:
Enter numbers:
</pre>
\*************************************************************************************
<pre>
Enter two positive integer numbers.
First number must be less than the second number:
Enter numbers:  <b>-2 8</b>

No negative numbers!
Please try again.

Enter two positive integer numbers.
First number must be less than the second number:
Enter numbers:
</pre>
\*************************************************************************************
<pre>
Enter two positive integer numbers.
First number must be less than the second number:
Enter numbers:  <b>2 8</b>

Odd integers between <b>2</b> and <b>8</b> are:
3 5 7

Sum of even integers between <b>2</b> and <b>8</b> = 20

Sum of the squares of odd integers between <b>2</b> and <b>8</b> = 83


Do you want to repeat the program?
y/n
> <b>y</b>
</pre>
\*************************************************************************************
<pre>
Enter two positive integer numbers.
First number must be less than the second number:
Enter numbers:  <b>1 9</b>

Odd integers between <b>1</b> and <b>9</b> are:
1 3 5 7 9

Sum of even integers between <b>1</b> and <b>9</b> = 20

Sum of the squares of odd integers between <b>1</b> and <b>9</b> = 165


Do you want to repeat the program?
y/n
> <b>y</b>
</pre>
\*************************************************************************************
<pre>
Enter two positive integer numbers.
First number must be less than the second number:
Enter numbers:  <b>11 15</b>

Odd integers between <b>11</b> and <b>15</b> are:
11 13 15

Sum of even integers between <b>11</b> and <b>15</b> = 26

Sum of the squares of odd integers between <b>11</b> and <b>15</b> = 515


Do you want to repeat the program?
y/n
> <b>n</b>

Bye!
</pre>
\*************************************************************************************
