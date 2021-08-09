# Homework Assignments 6

## Homework 6.1
As you learned from this class there is no such thing as "circular array" since an array is a continuous block of 
memory. Its last index does not loop back to its beginning. For this problem you will simulate the effect of a 
circular array in that you'd be able to shift all of its elements to the RIGHT by M elements, where M is an 
integer >= 0.

<br />

Write the following function taking in an integer array (arr), its length (N), and the number of elements to 
right-shift (M):

<pre>
def rightShiftElements(arr: list, N: int, M: int):
</pre>

<br />

**Examples:**

input: {1,2}, 2, 1

resulting arr: {2,1}

<br />

input: {1}, 1, 0

resulting arr: {1}

<br />

input: {1}, 1, 12

resulting arr: {1}

<br />

input: {1, 2, 3, 4, 5, 6}, 6, 3

resulting arr: {4,5,6,1,2,3}

<br />

input: {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45}, 45, 56

resulting arr: {35,36,37,38,39,40,41,42,43,44,45,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34}

<br />

**How to test (example):**

```
def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    size = len(arr)
    rightShiftElements(arr, size, 1)
    print('[', end='')
    for i in range(size):
        print(arr[i], end='')
        if i == size-1:
            print("", end='')
        else:
            print(',', end=' ')
    print(']')
```

<br />

**Constraints / Assumptions:**

* Your inputs come straight from main(...) **NOT** cin, getline(...), etc., inside the above given function you have 
to write
* This problem tests your understanding of how array works in C/C++
* For this problem you will operate your solution directly on arr[]. **DO NOT create another array in 
rightShiftElements() for this problem.** This is the reason why rightShiftElements(...) is a void function. **NOTE:** 
recall array is passed into every function by "pointer", namely your function actually has a handle to where the 
original array is located. Any changes made to the array inside your function changes the original array outside of 
the function.
* Each right shift moves all of the elements to the right by one index, with the exception of the last element which 
moves into index 0
* The arr[] array is not empty, or N > 0
* The number of elements to right shift M >= 0
* There is nothing to print or return in the function, which should simply satisfy the logic requirement by shifting 
elements to right M times
* arr[], when passed into the function, is decayed to a pointer that points to the first element of the array which 
means if you make modification to it in the function the original arr[] in main() will also change

## Homework 6.2
std::vector (available via #include <vector>) is a template class and a C++ construct. Vector is a dynamic array 
that grows and shrinks dynamically as needed:

http://www.cplusplus.com/reference/vector/vector/

To overcome integral size limitation (INT_MAX, DOUBLE_MAX, etc) we want to devise a programmatic scheme to store a 
number that can be VERY LARGE. To do that we have a positive number (N >= 0) whose digits are stored in a vector. For 
instance 123 is stored as {1, 2, 3} in the vector. 54321 is stored as {5, 4, 3, 2, 1} in the vector. 

<br />

Write the following function that simulates ++N by taking in its vector representation as the function parameter. The 
function returns the result of ++N in its vector form:

```
vector<int> plusPlusN(vector<int> v)
```

**Examples:**

input: {1,2}

output: {1,3}

<br />

input: {0}

output: {1}

<br />

input: {1}

output: {2}

<br />

input: {9}

output: {1,0}

<br />

input: {9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9}

output: {1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}

<br />

input: {9,2,3,9}

output: {9,2,4,0}

<br />

input: {9,9,9,9}

output: {1,0,0,0,0}

<br />

input: {2,9,9}

output: {3,0,0}

<br />

**Constraints / Assumptions:**

* This problem tests your understanding of how templated dynamic array (i.e., vector) works in C++
* Your inputs come straight from main(...) **NOT** cin, getline(...), etc., inside the above given function you have to 
write
* N >= 0; the input vector<int> v is **NOT** empty
* N can be very large, exceeding all integral limits in C++
* You may use any vector member functions (http://www.cplusplus.com/reference/vector/vector/) for this problem
* You may create your local copy of vector<int> as the value to return from the function. **OR** you may modify the 
vector<int> v that is passed-by-value into the function and return the modified v from the function. Either way it's 
completely up to you how you handle your return value
* Your main() function isn't graded; only the above referenced function is.
* Failure to follow the same exact function signature receives -1 logic point deduction
* You may have your test code in main(). The following is just an example using v = {9, 9}:

```
int main() {
    vector<int> v {9, 9};
    vector <int> retVal = plusPlusN(v); // retVal = {1, 0, 0}
    // insert you own assert or other test code here
    return 0;
}
```