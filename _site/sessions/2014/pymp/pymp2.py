__author__ = 'cap10'

from multiprocessing import Process, Lock, Pool
from time import sleep, perf_counter


def hello_from(i):
    print("hello world %d" % i)

def f(l, i):
    l.acquire()
    if (i % 10 == 0):
        sleep(.5)
    print('hello world', i)
    l.release()

def sqr(x):
    return x*x

def hello():
    print('hello')

val = 1

def reduce(xs):
    print(sum(xs))

if __name__ == '__main__':
    lock = Lock()
    p = Pool()

    #[Process(target=f, args=(lock, num)).start() for num in range(100)]
    #comp = sum(p.map(sqr, range(1,10)))
    #print(comp)
