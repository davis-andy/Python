# Homework Assignments 7

## Homework 7.1
Day trading involves buying and subsequently selling financial instruments (e.g. stocks, options, futures, derivatives, 
currencies) within the same trading day, such that all positions will usually be closed before the market close of the 
trading day. Depending on one's trading strategy, it may range from several to hundreds of orders a day.

You are a software engineer working for PCC, Inc. specializing in advising day traders with predicative triggers 
telling them when it's best time to buy/sell in a given day based on an instrument's historic data. This is a complex 
predicative system you are working on. All of the pricing data for this instrument are stored chronologically in a 
vector. 

<br />

Write the following function taking in an integer array (prices: list) consisting of all prices, in 
chronological order, for a hypothetical instrument. Your function recommends the maximum profit an investor can 
make by placing **AT MOST one buy and one sell order** in the time slice represented by your input array. Remember BUY 
LOW, SELL HIGH:

```
def getMaxProfit(prices: list) -> int:
```

<br />

**Examples:**

input: [1,2,4]

output: 3

_note on output: you'd buy $1, sell $4 => $3 profit_

<br />

input: [4,2,1]

output: 0

_note on output: you will not be able to buy low, sell high in this pricing order => no buy, no sell => $0 profit_

<br />

input: [1]

output: 0

_note on output: this may be the time slice at the end of the trading day; if you buy in at $1 you lose money since 
you won't be able to sell it before market closes_

<br />

input: [1,2,5,1,6]

output: 5

_note on output: you'd buy $1, sell $6 => profit $5_

<br />

input: [3,1,5,2,4]

output: 4

_note on output: you'd buy $1, sell $5 => profit $4_

<br />

**Constraints / Assumptions:**

* For this problem, there is **AT MOST** one buy and one sell (i.e., max of two orders, a "buy" order and a 
"sell" order)
* Prices are in USD ($) and are > 0
* Max Profit (output) is defined as the max price difference between your buy and sell prices ($profit = ($sell - $buy))
* __Input cannot be empty__ and it has at least one price data
* Output is your max profit based on the input
* Food for thought: can you get your solution to within O(n)?

## Homework 7.2
This problem is the same as #1, except you may complete as many buy/sell orders as you have to in a given time 
slice AND you must sell one before you can buy another (except for the very first buy order).

<br />

Write the following function taking in an integer array (prices: list) consisting of all prices, in 
chronological order, for a hypothetical instrument. Your function will suggest the maximum profit an investor can make 
by placing **AS MANY buy-sell orders as you may** in the given time slice your input array represents. Remember BUY 
LOW, SELL HIGH:

```
def getMaxProfit(prices: list) -> int:
```

<br />

**Examples:**

input: [1,2,4]

output: 3

_note on output: buy $1, sell $2, buy $2, sell $4 => $1+$2 = $3 profit_

<br />

input: [4,2,1]

output: 0

_note on output: you will not be able to buy low, sell high in this pricing order => no buy, no sell => $0 profit_

<br />

input: [1]

output: 0

_note on output: this may be the time slice at the end of the trading day; if you buy in at $1 you lose money since 
you won't be able to sell it before market closes_

<br />

input: [1,2,5,1,6]

output: 9

_note on output: buy $1, sell $2, buy $2, sell $5, buy $1, sell $6 => $1 + $3 + $5 = $9 profit_

<br />

input: [3,1,5,2,4]

output: 6

_note on output: buy $1, sell $5, buy $2, sell $4 => $4 + $2 = $6 profit_

<br />

**Constraints / Assumptions:**

* For this problem, you may have multiple buy-sell orders BUT you must sell one before you can buy again (except for 
the very first purchase)
* The multiple order requirement comes from the fact that you may just have enough money to buy one order to start 
with, and you are making small incremental profits by selling high like a day trader would for many times in a day
* Prices are in USD ($) and are > 0
* Input is passed in by reference
* Max Profit (output) is defined as the max price difference between your buy and sell prices ($profit = ($sell - $buy))
* __Input cannot be empty__ and it has at least one price data
* Output is your max profit based on the input
* Food for thought: can you get your solution to within O(n)?