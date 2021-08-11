# Homework Assignment 12

## Homework 12
From your prior assignment you studied California's drought problem and came up with your solution to calculate how 
much water retention there is in a given topographic terrain whenever it rains. In that problem your 1D terrain was 
represented by an integer array such as

<pre>
int arr[5] = {10, 20, 30, 40, 42};
</pre>

Your current assignment is to calculate water retention in a 3D terrain.

For simplicity, you are given an R x C matrix of positive integers representing the elevation of each unit cell in that 
matrix. For example with a 3x3 matrix you form the following elevation map:

```
/* 3D Elevation Map */
 vector<vector<int>> map = {
    {2,2,4},
    {2,1,2},
    {2,2,2}
 };
```

For this assignment write the following function that takes in an R x C vector (namely, a vector of vectors) 
representing your terrain map, where R > 0 and C > 0, and outputs the total amount of water retention in that given map:

```
int getTotalWaterAmount(vector<vector<int>>& map)
```

**Examples:**

input (1x1 matrix): 

vector<vector<int>> map = {

{123}

};

output: 0

<br />

input (2x2 matrix): 

vector<vector<int>> map = {

{9,2},

{2,1}

};

output: 0

<br />

input (3x3 matrix): 

vector<vector<int>> map = {

{1,1,1},

{1,1,2},

{1,2,2}

};

output: 0

<br />

input (4x4 matrix): 

vector<vector<int>> map = {

                {6,2,4,123},

                {33,2,35,10},

                {12,3,0,23},

                {83,33,2,34}

};

output: 2

<br />

input (3x6 matrix): 

vector<vector<int>> map = {

{1,4,3,7,3,2},

{3,2,1,1,3,4},

{5,3,3,5,3,1}

};

output: 5

<br />

input (5x7 matrix): 

vector<vector<int>> map = {

{13,45,33,77,335,2,3},

{32,25,123,1,3,41,3},

{13,64,19,73,3,212,3},

{52,3,35,35,389,13,3},

{1,4,9,7,3,21,3}

};

output: 140

<br />

**Hints:**

* Why is the following true? 
  * R = map.size(); 
  * C = map[0].size();
* map[0][0] gives you the elevation at row=0 and column=0.
* You may use your typical FOR-loop as you would with any array to iterate through this 2D map.
* At any given cell in the terrain matrix, water accumulates only if all 4 neighbors of that cell are higher than it 
in elevation. Right?
* Depending on the height of a cell's neighbor, extra water may need to be spilled. What do I mean by that? 
* For every cell that gets wet, water can possibly spill. We need to check the water height against all of a cell's 4 
neighbors. If the water elevation is taller than any one of its 4 neighbors, we need to spill the extra water. If we 
spill water from any cell, then its 4 neighbors need to check themselves again. This is an iterative process that 
involves checking and re-checking by updating new heights, if applicable, on all cells until there is no more water to 
be spilled.

<br />

**Constraints / Assumptions:**

* The terrain map is never NULL, namely map.length is always > 0
* Your map is passed into the function by reference (why not by value)?
* Number of rows (R) > 0
* Number of columns (C) > 0
* Elevation height is a positive integer greater than 0 and < 1000
* There is enough water to fill every dip in the terrain