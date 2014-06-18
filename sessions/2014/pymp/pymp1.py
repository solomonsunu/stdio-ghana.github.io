__author__ = 'cap10'

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
    print("parallel, w/ chopping up job: {0:f}".format(perf_counter() - start))

    start = perf_counter()
    sum(p.map(sum, input_list))
    print("straight parallel: {0:f}".format(perf_counter() - start))