__author__ = 'jay'

'''
A program that implements the Sieve of Eratosthenes to find primes up to 1.000.000. Use an array of 1.000.001 values of
True or False to indicate whether a number is still in the number set (that way, the index can climb up to 1.000.000,
to test even 1.000.000 for prime-ness).
'''

upper_limit = 1000001
bool_ary = [True] * upper_limit
# mark 0 and 1 as false
bool_ary[0] = bool_ary[1] = False
for idx, i in enumerate(bool_ary):
    if i:
        print(idx)
        for n in range(idx * idx, upper_limit, idx):
            bool_ary[n] = False
