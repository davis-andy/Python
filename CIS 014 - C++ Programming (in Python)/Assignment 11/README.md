# Homework Assignments 11

## Homework 11.1
Just a few years ago, California experienced the worst drought of the century. According to the latest study from 
NASA, California needs 11 trillion gallons of water to end drought 
(http://www.nbcnews.com/storyline/california-drought/california-needs-11-trillion-gallons-water-end-drought-nasa-n269546).
That is a lot of water. Unfortunately California does not get much rain water annually.

As an employee of Awesomeness, Inc specializing in providing environmental intelligence to government agencies, you are 
asked to write a software to calculate how much water retention there is in a given topographic terrain whenever it 
rains.

<br />

You are given an integer array consisting of integers representing the continuous elevation of the above (or any) 
terrain from A to B, namely

<br />

arr = [10, 20, 30 , 40, 42, 40, 30, 20, 40, 50, 55, 50, 40, 30, 20, 10, 3]

<br />

Water retention in the above example starts from 42 on left to 42 on right.

For this assignment write the following function that takes in a pointer reference to an array of any arbitrary 
elevation and its array size, and outputs the total amount of water retention in that given terrain:

<pre>
def getTotalWaterAmount(arr: list, size: int) -> int:
</pre>

**Examples:**

input: [10, 20, 30 , 40, 42, 40, 30, 20, 40, 50, 55, 50, 40, 30, 20, 10, 3]

output: 38

<br />

input: [5, 2, 1, 2, 1, 5]

output: 14

<br />

input: [0, 1, 0]

output: 0

<br /> 

input: [1, 2, 3, 4, 5, 6, 5, 4, 3, 6, 22, 3, 2]

output: 6 

<br />

input: [0, 1, 2, 5, 4, 2, 6, 4, 3, 2, 1, 1, 1, 1, 1, 1, 8]

output: 43

<br />

input: [5, 4, 1, 2]

output: 1

<br />

input: [5, 2, 1, 3, 1, 5]

output: 13

<br />

**Constraints / Assumptions:**

* The terrain map is never NULL, namely len(arr) is always > 0
* X-axis represents width (distance); the distance between two adjacent elevation (height) points is one unit
* Y-axis represents elevation (height) in the same unit as x-axis
* There is enough water to fill every hole in the terrain

## Homework 11.2
The State of California is interested in creating ways to retain precious rain water so it doesn't drain to ground or 
to the Pac Blue completely. The Department wants to arrive at metrics to help determine the best way to preserve rain 
water. One metric calls for excavating soil out of the ground to create "pockets" or retention ponds that can hold the 
most amount of rain water. No terrain is flat so this task involves measuring elevation profile of the terrain.

The terrain profile in 2D can be represented by data inside an array of [0, 5, 3, 1, 2, 0, 4, 6, 9, 0, 0, 0]. Each 
square box is of 1x1 unit. The max amount of water retention occurs if we dig into ground 5 units deep at array index 
1, and extend the space out to array index 8 forming a rectangle of 7x5 = 35 square units. Thus, a retention pond of 
cross-sectional area of 35 units is the max one we can create out of this elevation profile.

<br />

Another example:

The elevation profile for the above plot of land is [1, 2, 3, 1, 2, 1, 4, 8, 2, 2, 2, 0]. One can form the largest 
cross-sectional area by excavating soil at array index 1 and extend that area all the way to array index 10 forming a 
rectangle of area 2x9 = 18 square units. Thus, this is the largest retention pond cross-sectional one can create from 
this terrain.

<br />

Remember the proposal calls for digging into the ground, not setting up above-ground containers which can be more 
costly. Your goal is to determine that cross-sectional area of the future retention pond based on any terrain profile 
as input. 

<br />

For this assignment write the following function that takes in an array of any arbitrary elevation profile and its 
array size, and outputs the max cross-sectional area of the biggest pond based on this profile:

<pre>
def getMaxPond(arr: list, size: int) -> int:
</pre>

**Examples:**

input: [22,31,1,23]

output: 66

<br />

input: [1]

output: 0

<br />

input: [1,3,5]

output: 3 

<br />

input: [3,2,1]

output: 2

<br />

input: [1,1,1,1,1,1,1,1,1]

output: 8

<br />

input: [1,99,1]

output: 2

<br />

**Constraints / Assumptions:**

* The terrain map is never NULL, namely len(arr) is always > 0
* X-axis represents width (distance); the distance between two adjacent elevation (height) points is one unit
* Y-axis represents elevation (height) in the same unit as x-axis
* The function returns 0 if there is not enough soil to create that cross-sectional area (namely array containing just 
1 unit width)
