from functools import reduce

nrs = range(1, 21)


def isodd(x: int) -> bool: return x % 2 == 1


for i in filter(isodd, nrs):
    print('filtered: %d' % i)


def addhundred(x: int) -> int: return x + 100


for i in map(addhundred, nrs):
    print('mapped: %d' % i)


def sumelem(x: int, y: int) -> int: return x + y


sum = reduce(sumelem, nrs)
print('reduced: %d' % sum)
