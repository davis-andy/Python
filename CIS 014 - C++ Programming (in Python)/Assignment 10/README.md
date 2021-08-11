# Homework Assignments 10

## Homework 10.1
Pinball is a type of arcade game (http://en.wikipedia.org/wiki/Pinball) that has been popular in the US for 
decades. The main objective of the game is to score as many points as possible by launching steel balls through various 
pegs until they reach the bottom drain. Points are earned whenever balls hit target pegs. To make this game simple we 
have the following 2D pyramid. The ball is launched from the top, then funneled through each row of the pyramid until 
it reaches the bottom. As the ball hits a target peg at position N of a given row, the ball will either get diverted 
to the Nth or (N+1)-th peg of the row below:

Each diversion earns you points of a various amount. For this problem, you will determine the route that earns you the 
maximum amount of points. The above example showcases the max points you may get by traversing from 2 -> 1 -> 8 -> 7.

Note certain routes aren't possible given the aforementioned routing constraint, such as 2 -> 1 -> 5 -> 1, because 1->5 
isn't possible since the ball can only travel to either 3 or 8 in the row below.

Write the following member function, getMaxPoints(vector<vector<int>> &maze), inside the specific class named CIS14:

```
class CIS14:
    def getMaxPoints(self, maze: list) -> int:
```

Your solution should produce the max amount of points possible by launching a ball to fall from the top to the bottom 
drain. Your maze can be populated in the following fashion, for example:

```
maze = [[2], [4, 1], [5, 3, 8], [1, 6, 7, 3]] 
```

**Examples:**

maze = [[0], [4, 1], [5, 3, 8], [1, 6, 7, 3]]  # output = 16

maze = [[1], [1, 1], [1, 1, 1], [1, 1, 1, 1]]  # output = 4

maze = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]  # output = 23

maze = [[1], [1, 22305], [1, 29394, 1], [1, 1, 1234, 1], [1, 1, 3, 1, 10]]  # output = 52937

**Assumptions & Constraints:**

* The pyramid is a triangle with each row having 1 more element than the row above
* Each row consists of an integer array
* You may have up to INT_MAX number of rows
* The steel ball always moves from the top of the pyramid to the bottom, one row at a time
* Elements in the array have values that are signed integer (either positive or negative) within the signed integer 
limits
* The ball at the Nth peg can only travel to either the Nth or (N+1)th peg in the row below
* Your input is an array of arrays. **Your member function should account for an empty array, and an array 
of any empty arrays! Remember each row in the pyramid must have one more element than the row preceding it.**
* __When input is empty, your function should return 0__

## Homework 10.2
GPS has become popular in recent decade. GPS systems are increasingly used to create and use waypoints in navigation of 
all kinds (http://en.wikipedia.org/wiki/Waypoint). Waypoints are sets of coordinates that 
identify a point in physical space. Some waypoints may be points of interest on the map specifying landmarks, 
businesses, etc. 

<br />

You are an Awesomeness engineer working on their latest indoor mapping system similar to Google's 
(https://www.google.com/maps/about/partners/indoormaps/) but way better for Pasadena City College. The online mapping 
system will identify various waypoints (e.g., library, Building C, Building R, Bookstore, Swimming Pool, Gym, Student 
Parking Lot, etc) to help people navigate the campus. 

<br />

Adding all of your waypoints gives you a linked list.

Your system is capable of routing people from different locations on the map to a common destination based on all 
available waypoints known in advance. Inevitably some of the routes your system detects share the "common" paths.

For example, we have two paths leading to the same destination, D: A->C->D and B->C->D. The closest 
common path begins at C.

**A (starting point):** Shatford Library

**B (starting point):** Boone Sculpture Garden

**C (closest common waypoint to the starting points A, B):** The Quad

**D (destination):** Jack in a Box

<br />

Generalizing this your system is capable of suggesting people to meet at the nearest common waypoint on the path to 
the same destination. Each path is a linked list.

Write the following program that outputs the closest common waypoint from any given two path input, Node A and Node B:

<pre>
class CIS14:
    def getClosestCommonWaypoint(self, Node A, Node B) -> Node:
</pre>

Supposedly each of these waypoints is represented in the Python class as follows, with each waypoint having just one 
value (integer) and the pointer pointing to the adjacent (next) waypoint:

<pre>
class Node:
    value: int
    next: Node
    Node(v: int) : value(v), next(NULL)
</pre>

**Hints:**

* How you create your test cases is completely up to you - this is just a suggestion. Your Node instance with any 
arbitrary value you want it to have can be instantiated on stack. Similarly, your link list of two nodes can be created 
as follows:

<pre>
a, a1 = Node(10), Node(11)
a.next=a1
a1.next=NULL
</pre>

**Constraints and Assumptions:**

* If two paths share no common path, return NULL
* The output should be the same node as the one in the original list; you shouldn't dynamically create one - return the 
same node from the original list
* There cannot be multiple common paths in your input
* Input can be NULL so be sure to check it!
* The input paths MUST retain their original structure and values after the function returns
* Each path is uni-directional (singly); it won't loop back to any prior node in the same path