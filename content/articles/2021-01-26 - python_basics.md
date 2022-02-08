Title: Python Basics
Date: 2021-01-31
Tags: Python, Software, Technology
Summary: Basic Python concepts

In some future posts, I will make worked examples of API interactions and some automations. My preferred programming language is [Python](https://python.org). I cannot remember why I chose to learn Python, but it was pretty strightforward to pick up. I initially learned about coding when recording macros within Excel, then trying to improve them by writing the VBA (Visual Basic). In this post, I will cover some of the basic concepts that I will use in later posts.

I won't cover installing Python or running Python on your system. There are lots of tutorials and guides out there and that's part of the fun of learning a new programming language. For reference, I mostly use Debian (operating system) and Python 3.

## General

Python uses whitespace to separate out code. Broadly, one piece of logic per line is best. It makes it easier to understand.

Python also uses indents to group code together:

~~~
def some_function(i):
	does something to i
	returns result
~~~

~~~	
def another_function(a):
	this function is different to above
	return result
~~~

## Variables

Any one that has taken GCSE maths would have come across variables. It's not a popular subject, but algebra is all variables. A variable is a container. In algebra it is a number, in programming it can be anything. For example, the formula *Y = X<sup>2</sup> + 4* both **Y** and **X** are variables. To plot a graph of **Y**, you would plug values into **X** and solve for **Y**.

Here's how you can assign a variable in Python:

~~~
# assign a string to a variable called "name"
name = 'guitar'
# assign a number to a variable
strings = 6
# assign a list to a variable
types = ['electric', 'acoustic']
~~~

## Arrays

An array is a collection of data. Python has several types. I mainly use lists and dicts.

### Lists

Lists are pretty simple. A list is a series of items that are separated by commas within square brackets. They can contain any data types, and can be mixed.
	
~~~
# list of strings
['hello', 'this', 'is', 'a', 'string']
# list of numbers
[1, 2, 3, 4.5, 6.7 ]
# list of variables
[first, second, third]
# mix list
['string', string, '1', 1]
~~~

### Dicts / JSON

A dict (or dictionary) is a more comprevensive data item. The syntax is reasonably easy to understand, and features heavily when dealing with API. Javascript has a similar array type called JSON (JavaScript Object Notation). Many API will return a JSON object for you to use.

Again, dicts can hold all different types of data. However, the most interesting part of a dict is that each data item has a key. The key refers to the data stored. A dict is how one might intuitively think of a database record. Of course, you can have lists of dicts.

Not all dicts in a list have to have the same keys, but it is useful if they do.

~~~
books = [
	{
		'title': '1984',
		'author': 'George Orwell'
	},
	{
		'title': 'Brave New World',
		'author': 'Aldous Huxley'
	}
]
~~~

## Functions

A function is an action that you regularly perform within a script. This saves you time in your code, as you only have to write the thing once. There are lots of built in functions in Python, you will definitely write your own.

Using the formula from above, we could write it as a function:
	
~~~
def solve_y(x):
	y = (x * x) + 4
	return y
~~~

Functions start *def* then the name of the function followed by brackets and a colon. In the example we can pass a number to the function and the function performs the action. The "return" part means that the function will give the result of the function back. This can be assigned to a variable or something else.

Here are some results for our function:

~~~	
>>> solve_y(4)
20
>>> solve_y(2)
8
~~~

Our *solve_y* function can be writted using the in-built power function. It raises any number to the power of another number:

~~~
def solve_y(x):
	y = pow(x, 2) + 4
	return y
~~~

In our particular case, it doesn't really make it a lot simpler. However, it a bit clearer from a BODMAS point of view.

### For Loop

**For loops** are used lots. A for loop iterates over an item, assigning each of results to a variable. It's kind of hard for non-programmers to get your head around, however, it very powerful. Here are some examples:

~~~
>>> for i in range(5):
...     i
... 
0
1
2
3
4
~~~

**range(x)** is a function that returns numbers incremented by 1. The range function starts at 0 by default and will count the number of items. Our for loop will assign the result of the range function to the variable i. This is then displayed on the screen.
