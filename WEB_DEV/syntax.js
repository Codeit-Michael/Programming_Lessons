// 1. Comments
// - is called single line comments
/* - is called multi line comments */

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 2. Declare and store data in js variables

/* JavaScript provides eight different data types which are undefined, null,
boolean, string, symbol, bigint, number, and object. */
// Declaring  a variable(if empty):
var theValue;

// Store values w/ assignment operator (=)
theValue = 5;

// assign with value from others
var new1;
new1 = theValue;

// acceptable also
var var1 = 3;

/* define a variable what data type is it recieving, if str? = "",num? = 0. etc
undefined var gives has undefined value*/
var a1 = 0;
a1 += 5;

// due to its naming and case sensitivity, its recommended to use camelCaseVars

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// Arithmetic - same as python, using: +,-,*,/.
var sum = 3 + 7;

// In adding/ subtracting 1; just var ++/--; instead var = var - 1;

// floats can be solved too

// remainder operator(%) dissimilar to modulus even the same, but not if int is negative

// also uses +=,-=,etc.

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// Strings (single or double)
//can insert a " str inside " str using \" \" also applicable in \' \'
// single or double strs may join as long as they are escaped: "he\'s"'

/* Backslash uses
\'	single quote
\"	double quote
\\	backslash
\n	newline
\r	carriage return
\t	tab
\b	word boundary
\f	form feed
*/
// finding length - console.log("str".length);
// accessing different data: also varname[0]
// last objects varname[varname.length-1]

// Multiple quotes in javascript: ` `
// In quote ` `, you can also insert codes that works
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// Arrays-[] (just like python arrays). Also access by indexes
/* Array methods
.push() - append
.pop() - remove last added
.shift() - removes first added
.unshift() - append left
*/

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//Making function
function example(param1){
	return param1;
}
console.log(example(3));

// making global var - not adding var in the begginning is already a global
// same return method
