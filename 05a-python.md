# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Tuples are immutable, lists can be assigned values. Tuples are superior as dictionary keys because dictionaries have to be hashable -- i.e. the hash function of a value has to always return the same value. Since lists are mutable, they can be modified and return a different value.

Dictionary values, on the other hand, can be lists. Indeed, it's actually useful to store them that way for later editing. 
 
To use a real world analogy, natural language dictionaries frequently edit the definitions (values) of words, and they frequently add words (adding more key/value pairs), but they very very rarely change the spelling of existing words while keeping the definition constant (changing keys).

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Sets are immutable like tuples but, unlike tuples or lists, they're non-ordered and only consist of unique values. Lists are useful when the ordering and/or frequency of values matter -- the football scores table in exercise 8 is a great example, because the position of a value in each list shows what quantity that value represents.

Because lists are indexed, you can find exactly where values occur, and call the location of values, or compare values at locations:

In: A = [9,7,11,14,17]

In: A.index(14)

Out: 3

In: A[1]-A[2]

Out: -4

Lists can also be turned into sets and vice-versa:

In: A = [1,1,1,1,2,2,2,2,3,3,3]

In: set(A)

Out: {1, 2, 3}

In: list(set(A))

Out: [1, 2, 3]

Sets support operations like testing for intersections and subsets. Finding elements in sets is a lot faster since sets simply have less information; set(A) has 3 values vs the 11 in A, and also doesn't store information about the order of those values.

In: A = set([9,12,17])

In: B = set([8,9,11])

In: A&B

Out: {9}

i.e. 9 is the only value in both sets

In: C = set([9])

In: C<B

Out: True

i.e. the set {9} is completely contained within the set {8,9,11}

In: B<A

Out: False
˙
i.e. the set {8,9,11} is not completely contained within the set {9,12,17}

---

###Q3. Lambda Function

Describe Pythons `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

Lambda is a way of creating functions not bound to a function name, though they can be bound to a variable. This can be very handy.

In: g = lambda x: x+5*x**2-x**3

In: A = [0,1,2,3,4,5,6,7,8,9]

In: B = [None]*len(A)

In: i=0

In: while i<len(A):

In:     B[i]=g(A[i])

In:     i=i+1

In: print(B)

Out: [0, 5, 14, 21, 20, 5, -30, -91, -184, -315]

This is the value of x + 5x^2 - x^3 for each value in A.

We can also use this as a key to sort A without calling this stage

In: C = sorted(A,key=g,reverse=True)

In: print(C)

Out: [3, 4, 2, 1, 5, 0, 6, 7, 8, 9]

The values are now sorted in descending order by the values of x + 5x^2 - x^3.

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

List comprehensions are alternatives to for or while loops for performing lots of algorithmically defined operations. 

Like map, they can perform operations on lists of integers. For example, we can use both to generate that list of values of x + 5x^2 - x^3:

In: [x+5*x**2-x**3 for x in range(0,10)]#list comprehension

Out: [0, 5, 14, 21, 20, 5, -30, -91, -184, -315]

In: list(map(lambda x: x+5*x**2-x**3, range(0,10)))

Out: [0, 5, 14, 21, 20, 5, -30, -91, -184, -315]

Like filter, they can be used to give a subset of a list that meets a function-defined criteria. If we want to know which of these integers have positive values of x + 5x^2 - x^3, we can do that with either:

In: [x for x in range(0,9) if x+5*x**2-x**3>0]#list comprehension

Out: [1, 2, 3, 4, 5]

In: list(filter(lambda x: x+5*x**2-x**3>0, range(0,10)))

Out: [1, 2, 3, 4, 5]

List comprehensions match the funtionality of both map and filter in a single approach.

Set and dictionary comprehensions work analogously to list comprehensions, but for sets and dictionaries:

In: {x+5*x**2-x**3 for x in range(0,10)}

Out: {-315, -184, -91, -30, 0, 5, 14, 20, 21}

This is a set containing those same values of x + 5x^2 - x^3.

In: {x: x+5*x**2-x**3 for x in range(0,10)}

Out: {0: 0, 1: 5, 2: 14, 3: 21, 4: 20, 5: 5, 6: -30, 7: -91, 8: -184, 9: -315}

This is a dictionary containing those values of x + 5x^2 - x^3 with their corresponding x values.

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

There were 937 days between January 2, 2013 CE and July 28, 2015 CE.

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

There were 513 days between December 31, 2013 CE and May 28, 2015 CE.

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

There were 7850 days between January 15, 1994 CE and July 14, 2015 CE.

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





