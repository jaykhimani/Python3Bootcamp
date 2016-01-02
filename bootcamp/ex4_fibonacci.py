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
