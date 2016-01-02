# Imagine you have a function fib(n) that returns the n’th Fibonacci number. This number is defined as follows:
# ● fib(0) is 0
# ● fib(1) is 1
# ● fib(2) is fib(1) + fib(0)
# ● fib(3) is fib(2) + fib(1)
# ● etc..
# The function code is:
# def fib(n):
#     if n in (0, 1):
#     return n
# return fib(n ­ 1) + fib(n ­ 2)
# Here is the exercise.
# 1. Use the function to compute the 40th Fibonacci number.
# 2. How long does this take? Why? (Hint: add print() statements to see what’s going on.)
# 3. Write a wrapper generator called cached() that caches previously obtained results in a local dictionary.
#    Use the wrapper on the above function fib().
# 4. How long does it take now to compute the 40th Fibonacci number?

from time import clock


def cached_fib(fn):
    cached = {}

    def jak(arg):
        if arg in cached:
            return cached[arg]
        result = fn(arg)
        cached[arg] = result
        return result

    return jak


@cached_fib
def fib(n: int):
    if n in (0, 1):
        return n
    return fib(n - 1) + fib(n - 2)


start = clock()
print(fib(40))
end = clock()
print("Cached: Time taken %.4f seconds" % (end - start))
