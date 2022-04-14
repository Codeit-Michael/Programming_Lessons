### Chapter 1 The Bigger Picture
**.join**
```
list1 = ['hey','hello','hey']
tabber = '\t'
print(tabber.join(list1)) # applicable in str only
```


***
### Chapter 2 Separation of concerns
-In planning software, make sure each service contains its step only. Inventory 
just tracks all the items are in stock, the pricing is incharge of pricing and 
taxing them.

-Be observative. Always look on the lines if they can still do their job if you 
make them readable if trimmed.


***
### Chapter 3 Abstraction and Encapsulation
Part 2 Foundations of Design
Using Python's features for code organization & separation
Choosing how & when to separate code into distinct pieces
The levels of granularity in separating code

clear code - clean, understandable codes divided/put together by their 
concerns(-difficulties)

code decomposition - breaking code into scalable actions/codes.

-------------------------------------------------------------------------
| design, refactoring, and now decomposition and separation of concerns |
-------------------------------------------------------------------------
-Abstraction - taking something concrete and stripping it of specifics

Abstraction onion - the deeper the layer is through the center, the more 
complex it is

-Abstraction didn't work all the time because maybe because you found a better, 
shorter solution or abstraction doesn't fi all use cases. If it causes more 
trouble, don't refuse to eliminate it. 

If the fault is in package using, consider making an adapter class that has the 
interface of program you expects


Probabilistic modeling uses a large body of input testing data to determine the 
likely correctness of a particular result.


Refactoring - making your code more clean, restricted. Like a Greeter class 
where identifies what day it is and what part of day it is. Instead of putting 
Those 2 functions inside and privating them, you can put them outside and call 
'em when you needed. In that way, you make Greeter class more all about greeting
 and you can use those functions unlike when they are private.


**Paradigm examples**
1. Procedural Programming - step by step functions

2. Functional Programming - allows thinking every part of  the code as 
composition of functions. Instead of *for* loops, use functions operating lists

3. Declarative Programming - from the name itself, declaring from the start and 
not step by step phase of application


polymorphism - many forms; composition
-composition - still has the essence from the hierarchy but free from its 
limitation
-Composition is often done through a language feature called an interface. 
Interfaces are formal definitions of methods and data that a particular class 
must implement. A class can implement multiple interfaces to broadcast that it 
has the union of those interfaces’ behaviors.
-Mixins(mix-ins) - mixed methods; can inherit as many as you needed

polymorphism type examples
1. inbuilt polymorphic function - inbuilt;map(),len()
2. user-defined poly func - user-made
3. Poly w/ class methods - calling same name meths in diff classes
4. Poly Inheritance - method overriding means not all are used, some are changed
5. Poly w/ funcs,objs - meths/classes having diff vals throuh class funcs/objs


***
### Chapter 4 Designing for high performance
asymptotic - measurement for worst case scenario

If you think back to the equation for a line in mathematics, y = mx + b, you can
 think of x as the number of inputs and y as the time it takes your program to
execute. There may be some overhead for your program regardless of input (the 
b, or intercept, in the equation), and each additional input adds some amount of
 execution time (m, or the slope). Y = Time(mx) + input(b)

set, dictionary, list, tuple: ADDING,REMOVING END - O(1)time, O(n)space

built-in yield() - in an iteration, it holds the last value given/grabbed, so 
the next time you add something is much faster because it don't iterate the 
whole list anymore and just append next to what is left. 

iter() - iter from start to last
next() - return the next value

Lazy Evaluation - the idea of producing one value at a time, and that consuming 
code may not need all the values you can produce. It’s lazy because you’d like 
to do as little work as possible, and only once you’ve been asked explicitly to 
do so.

"Make it work, make it right, make it fast" -Kent Beck's programming rules

Refactor it when you implement this code 3 times on the same code you're working
 on. Means don't refactor things too early, making a hardcore revising on a code
 you can use only in a moment makes your work advancement slower.

You can tell a defaultdict the type of the values it stores, and it will default
 to a sensible value of that type if a new key is accessed:
	from collections import defaultdict
	# counts the most frequent number
	def most_frequent(numbers):
		counts = defaultdict(int)
		for number in numbers:
			counts[number] += 1

Counter() - counting number frequency (how many times was said the no. appear 
on the list)
	from collections import Counter
	numlist = [1,2,3,3,4]
	Counter(numlist)
	OUTPUT: Counter(1: 1, 2: 1, 3: 2, 4: 1)


max() - max(base,key)

functional programming mostly use lambdas:
	def get_number_with_highest_count(counts):
		return max(counts,key=lambda number: counts[number])
