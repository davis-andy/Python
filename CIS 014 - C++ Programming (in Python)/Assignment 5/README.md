# Homework Assignments 5

## Homework 5.1
Software versioning is the process of assigning either unique version names or unique version numbers to unique 
states of computer software. Software companies typically use incrementing sequences 
to version their software products. For example, they may have:

<pre>
major#.minor#.revision#
</pre>

In principle the major number is increased when there are significant jumps in functionality such as changing the 
framework which could cause incompatibility with interfacing systems, the minor number is incremented when only 
minor features or significant fixes have been added, and the revision number is incremented when minor bugs are 
fixed (for more information see http://en.wikipedia.org/wiki/Software_versioning).

Write the following function (please follow the **EXACT** function signature) that compares the two version strings, 
ver1 and ver2, of a software product to determine which product version is the latest:

<pre>
int compareVersions(string ver1, string ver2)
</pre>

* If ver1 > ver2: return 1
* If ver1 < ver2: return -1
* Otherwise, return 0. 

**Examples:**

* 7.1.1 is the 7th major production with the first minor release and revision number 1.
* 0.1 < 0.2
* 0.13.1 < 0.13.2
* 1.0 = 1.0
* 6 = 6
* 0 = 0
* 1.1.0 < 1.1.1 < 1.1.2 < 1.2.0 <  1.2.1 < 1.3.1 < 8.8.8
* 1 < 1.1
* 1.1 = 1.1.0
* 256 < 300.2.1
* 0.1 < 1
* 3 < 3.1.1
* 3.1.1 < 4
* .0.4 < .1
* .2 > .1.1

**Constraints / Assumptions:**

* The version strings are non-empty

* The version strings contain only digits '0'-'9' and the '.' (dot) character

* The '.' (dot) character is not a decimal point; it is used to separate major/minor/build sequences (see Wiki above 
for more information

* The major # is assumed to be 0 when followed by a '.' dot  (namely .1 is the same as 0.1, .3.1 is the same as 0.3.1)

* You may test your function in the following fashion, for example:

<pre>
int main()  
{
   cout << compareVersions("1.0", "1.1") << endl;
   cout << compareVersions("2.0", "2.0.1") << endl;
   ...
   return 0;
}
</pre>

**EXTRA CREDIT:** Extend your compareVerisions(string, string) function to support long version numbers 
containing **more than** major, minor, and release #s. For example, you may have your input version as 
"2.3.2.2.3.1.1.5.3.5.6.2", "1.1.1.1.1.1.1", etc.

## Homework 5.2
Your professor needs your help to decipher some secret message in a sentence. The secret message is formed by taking 
the first letter of each word in the sentence, in the order of their appearance. Write the following **EXACT** 
function:

<pre>
/**
* FUNCTION SIGNATURE: string getSecretMessage(string str)
 * PURPOSE: get secret message by taking the first character from each word in the input sentence, in the order they appear
 * PARAMETER:
 *     str, the input sentence 
 * RETURN VALUE:
 *     The secret message
*/
</pre>
 

Examples:

**Input str: "professor can code"**

**Secret Message: "pcc"**

(Note: input consists of 3 words separated by single space. Taking the first character of each word gets you "pcc")

<br />

**Input str: "professor         can        code"**

**Secret Message: "pcc"**

(Note: input consists of 3 words separated by multiple spaces. Taking the first character of each word gets you "pcc")

<br />

**Input str: "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"**

**Secret Message: ""**

(Note: input is "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" - there are no words there. This is what we called an empty string (not NULL string). The 
secret message is "" since there are no words in the input sentence) 

<br />

**Constraints / Assumptions:**

* For this problem, you may use ANY C/C++ libraries
* Your input sentence is a collection of words consisting of only lowercase English characters ('a' - 'z') and spaces (' ').
* There may be multiple spaces between words.
* A sentence may consist of only spaces
* If there is no secret message to be generated, the function returns ""
* Failure to follow the same exact function signature receives -1 logic point deduction
* A sentence will contain between 1 and 50 characters
* Your main() function isn't graded; only the above-referenced function is
* Failure to follow the same exact function signature receives -1 logic point deduction
* You can test your function in the following fashion, for example:

<pre>
int main()  
{
   cout << getSecretMessage("professor can code") << endl; // prints "pcc"
   cout << getSecretMessage("                ") << endl;  // prints nothing
   cout << getSecretMessage("pasadena") << endl;  // prints "p"
   ...
   return 0;
}
</pre>
