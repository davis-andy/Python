# Chapter 3 Assignments

## Ch03-01
1. Write a Python program that prompts the user to input three numbers.  The program should then output the numbers in ascending order.
\***__Do NOT use nested conditionals (nested-if).  Use one if-elif statment.__

2. Try the following combinations for testing:
1, 2, 3
1, 3, 2
2, 1, 3
2, 3, 1
3, 2, 1
3, 1, 2
3, 1, 1
1, 1, 3
1, 3, 1
3, 1, 3
3, 3, 3

\*************************************************************************************

OUTPUT:

&ndash; The bold text is the user's input.

\*************************************************************************************
<pre>
Please input three integers: 
<b>2 3 1</b>

Input three integer numbers in ascending order:
1 2 3
</pre>
\*************************************************************************************
<pre>
Please input three integers: 
<b>3 2 1</b>

Input three integer numbers in ascending order:
1 2 3
</pre>
\*************************************************************************************
<pre>
Please input three integers: 
<b>1 2 3</b>

Input three integer numbers in ascending order:
1 2 3
</pre>
\*************************************************************************************
<pre>
Please input three integers: 
<b>2 1 3</b>

Input three integer numbers in ascending order:
1 2 3
</pre>
\*************************************************************************************
<pre>
Please input three integers: 
<b>2 1 1</b>

Input three integer numbers in ascending order:
1 1 2
</pre>
\*************************************************************************************

## Ch03-02
1. Write a Python program to score the paper-rock-scissor game.
Each of the two users types in either (**P** or **p**), (**R** or **r**), or (**S** or **s**).
The program then announces the winner as well as the basis for determining the winner:
Paper covers rock,
Rock smashes scissor,
Scissors cut paper,
or Nobody wins.
\***__Use nested conditionals (nested-if).  Use the outer if for Player1, and the inner if for Player 2.__

\*************************************************************************************

OUTPUT:

&ndash; The bold text is the user's input.

\*************************************************************************************
<pre>
Enter [R]ock, [P]aper or [S]cissor
Player 1: <b>p</b>
Enter [R]ock, [P]aper or [S]cissor
Player 2: <b>s</b>

Scissor cuts paper.
Player 2 WINS!
</pre>
\*************************************************************************************
<pre>
Enter [R]ock, [P]aper or [S]cissor
Player 1: <b>p</b>
Enter [R]ock, [P]aper or [S]cissor
Player 2: <b>s</b>

Scissor cuts paper.
Player 2 WINS!
</pre>
\*************************************************************************************
<pre>
Enter [R]ock, [P]aper or [S]cissor
Player 1: <b>p</b>
Enter [R]ock, [P]aper or [S]cissor
Player 2: <b>p</b>

Nobody WINS!
</pre>
\*************************************************************************************