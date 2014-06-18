---
layout: presentation
year: 2014
title: Python Multiprocessing
instructors:
 - Carl
---
<section markdown="block">
###OPINION:

Support for developers using parallelization directly in Python is poor.

If your problem cannot fit into a neat parallelization scheme, *do not use Python
to solve it*.

Many libraries accomplish parallel tasks by deferring to native code, so that
can be another option.
</section>

<section markdown="block">
##From AM session:

{% highlight python %}
from multiprocessing import Pool
from time import perf_counter

if __name__ == '__main__':
    p = Pool()
    ulim = 1000000000
    start = perf_counter()
    sum(range(1,ulim))
    print("serial: {0:f}".format(perf_counter() - start))

    start = perf_counter()
    input_list = [range(x,x+1000) for x in range(1,ulim,1000)]
    sum(p.map(sum, input_list))
    print("parallel, inc. alloc.: {0:f}".format(perf_counter() - start))

    start = perf_counter()
    sum(p.map(sum, input_list))
    print("straight parallel: {0:f}".format(perf_counter() - start))
{% endhighlight %}

slightly more \#\'s than you had
</section>

<section>

<section markdown="block">
##Guess Run Times?
</section>

<section markdown="block">
##[Try it and move on](pymp1.py)
</section>

<section markdown="block">
##How Parallelized?
</section>

</section>


<section markdown="block">
##a few fundamental approaches

Shared data containers that look a lot like atomic / synchronized vals in Java

explicit shared state management via `Manager`

`Process`: looks basically like Thread in Java
`Pool`: very similar to OpenMP approach: execute some loop structure in
parallel, ignore details of how it gets divvied up

Uses `map`, `map_async`, and `apply`, `apply_async` for single items
</section>

<section markdown="block">
##[Explore Some Other Structures](pymp2.py)
</section>

<section markdown="block">
##Python + Multiprocessing vs. C++?

<aside class="notes" markdown="block">
When does it make sense to deal with parallelizing your code vs finding a c/cpp
library and using it?
</aside>
</section>

<section markdown="block">
##Alternative: [Parallel Python Quickstart](http://www.parallelpython.com/content/view/15/30/#QUICKSMP)
</section>
