def needs_int(fn):
    def wrapper(arg):
        if type(arg) != int:
            raise Exception('Function needs int argument, received %r' % type(arg))
        return fn(arg)

    return wrapper


def needs_positive_nr(fn):
    def jak(arg):
        if arg < 1:
            raise Exception('Function needs positive number as argument, received %r' % arg)
        return fn(arg)

    return jak


@needs_int
@needs_positive_nr
def fact(n):
    if n < 3:
        return n
    result = n * fact(n - 1)
    # print("Returning %d" % result)
    return result


# Example of generator functions
wrapped_1 = needs_positive_nr(fact)
wrapped_2 = needs_int(wrapped_1)
print("Generator: Factorial of 5 is %d" % wrapped_2(5))

# Example of decorator functions
print("Decorator: Factorial of 5 is %d" % fact(5))
