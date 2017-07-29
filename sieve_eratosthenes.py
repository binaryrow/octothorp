"""Sieve of Eratosthenes – computes the primes less than n.
"""

import math

n = 1000
numbers = range(2, n)
results = []

while numbers != []:
    results.append(numbers[0])
    numbers = [n for n in numbers if n % numbers[0] != 0]

print (results)



