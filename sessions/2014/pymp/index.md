---
layout: presentation
year: 2014
title: Python Multiprocessing
instructors:
 - Carl
---
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
##Familiar?

<aside class="notes" markdown="block">
Looks like the Java `Executor` yields `Future` model.

What are examples in other languages?
</aside>
</section>

<section markdown="block">
##On a Compute Cluster
</section>

<section markdown="block">
Exercise to demonstrate speed advantage
</section>

<section markdown="block">
Exercise to demonstrate shared state concerns
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
