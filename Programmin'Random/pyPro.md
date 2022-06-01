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

timeit module - use to measure your code's time complexity in CLI or directly on
 your code:
	ex. 1
	python -m timeit "total = sum(range(5000))"

	ex. 2
	from timeit import timeit
	setup = 'from datetime import datetime'
	statement = 'datetime.now()'
	print(timeit(setup=setup, stmt=statement))

>> We can see here that lists are fasters than sets:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
| >> python3 -m timeit "he = list(range(1000))"	|
| 10000 loops, best of 5: 38.1 usec per loop	|
|						|
| >> python3 -m timeit "he = set(range(1000))"	|
| 5000 loops, best of 5: 55.9 usec per loop	|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

CPU profiling - lets you see which parts of your code perform expensive 
calculations, as well as how often they’re called. It's useful because it allows
 you to know where to start speeding up your code.

cProfile/profile module - modules for cpu profiling works;
 (ncalls) - The number of times the call occurred
 (tottime) - The time spent in that call alone, not including things it calls 
in turn
 (percall) - The average time spent in that call alone, across the ncalls times
 (cumtime) - The cumulative time spent in that call, including any time spent 
in subcalls

-To run:
  python3 -m cProfile --sort cumtime cpu_profiling.py

Summary
 Design for performance both up front and iteratively throughout your 
development.
 Think carefully about the right data type for the task.
 Prefer generators over lists when you don’t need all the values at once, to 
save on memory usage.
 Use the timeit and cProfile/profile Python modules to test your hypotheses 
about complexity and performance.

***
### Chapter 5 Testing your software
software testing is the practice of verifying that software behaves the way you 
expect. This can range from making sure a function produces the expected output 
when given a specific input to making sure your application can handle the 
stress of 100 users at once.

functional testing - testings that can make sure software produces the right 
output for a given input.

basic anatomy of functional testing
1. Prepare the inputs to the software. (determined by you)
2. Identify the expected output of the software. (by you)
3. Obtain the actual output of the software. (by code execution)
4. Compare the actual and the expected outputs to see if they match. (are they 
the same? good, or different? failed)
