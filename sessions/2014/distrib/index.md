---
layout: presentation
year: 2014
title: Distributed Computing
instructors:
 - Carl
---
<section markdown="block">
## What is a computer?

<aside class="notes" markdown="block">
First, there is the serial notion of a computer.  Series of commands, executed
one after another until desired output achieved.

There is another perspective, however: the *internet* perspective - when you
visit a website, your computer talks to another computer.  When
you load two websites, the information does not arrive at the same time.

Many applications use the internet in this way: pulling information from
multiple sources.  Some applications are making more local use of a network of
machines - this is what happens with cluster computation.
</aside>
</section>

<section markdown="block">

## Synchronous

vs.

## Asynchronous

</section>

<section markdown="block">

##Exercise

Some teams series, some parallel: sums and products of random numbers.

</section>


<section markdown="block">
## What made the parallel version easy?

<aside class="notes" markdown="block">
Aside from simplicity of operation:

- None of the divided pieces depended on the others.
- the divided pieces were identical
- the integration step looked exactly like the divided steps

</aside>
</section>

<section markdown="block">
##Another Exercise

Find the schedule and results so far for Group G from 5 different news sites.
</section>

<section markdown="block">
##How did you approach problem?

##What did you notice?
</section>

<section markdown="block">
##Shared State Exercise

Same as previous exercise, slightly tweaked rules.

<aside class="notes" markdown="block">
Again, some pen-and-paper exercises.
Same as earlier exercise, but with a tweak on where they record results:

- everyone looks at central sheet of paper
- for each sum, they write down value they see, calculate
- then take central sheet, cross out value, and write result

</aside>
</section>

<section markdown="block">

##What went wrong?

</section>

<section markdown="block">
High level concepts available when shared state can be avoided:

- filter, map
- fold (plain; left and right sometimes), scan

* * *

Ways to avoid shared state

- zip, join
- flatten
- *monads*

<aside class="notes" markdown="block">
Q&A about the concepts.  Write a dummy API for these concepts, have them
implement something using it.
</aside>

</section>
