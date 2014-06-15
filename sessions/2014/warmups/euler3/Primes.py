__author__ = 'Deanne'
#To solve for the highest prime factor of a given number

n = 600851475143

#This works for small test cases but is too slow to
#solve for very large numbers
#Uncomment to run:

# for x in range(2, n + 1):
#     prime = True
#     for y in range(2, x):
#         if x % y == 0:
#             prime = False
#     if prime:
#         largestPrime = x
# print (largestPrime)

#This is the shorter length version, which enumerates all multiples of the large number and then determines
#which numbers were not added to a list, and these are the primes: This crashes due to not enough memory for
#large numbers
#uncomment to run

# import math
# noPrimes = [j for k in range(2, math.floor(math.sqrt(n))+1) for j in range(k*2, n, k)]
# Primes = [x for x in range(2, n) if x not in noPrimes]
# print(Primes[len(Primes)-1])


#recommended solution:
import math
factor = 1
if (n % 2) == 0:
    n /= 2
    lastFactor = 2
    while (n % 2) == 0:
        n /= 2
else:
    lastFactor = 1
factor = 3
maxFactor = math.sqrt(n)
while (n > 1) & (factor <= maxFactor):
    if (n % factor) == 0:
        n /= factor
        lastFactor = factor
    while (n % factor) == 0:
        n /= factor
    factor += 2
if n == 1:
    print(lastFactor)
else:
    print(n)